"""Regression checks for separate branding and subscription journeys."""

import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
VERSIONS = ("", "auto-plus", "bleu")
PAGES = ("index.html", "paiement.html")


class Document(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.source = path.read_text()
        self.nodes = []
        self.feed(self.source)

    def handle_starttag(self, tag, attributes):
        self.nodes.append((tag, dict(attributes)))

    def attributes(self, tag, keys):
        return [tuple(attrs.get(key) for key in keys)
                for node, attrs in self.nodes if node == tag]


class SiteTests(unittest.TestCase):
    def test_local_links_assets_and_anchors_stay_in_their_version(self):
        for version in VERSIONS:
            folder = ROOT / version
            for name in PAGES:
                with self.subTest(version=version, page=name):
                    page = Document(folder / name)
                    ids = [attrs["id"] for _, attrs in page.nodes if "id" in attrs]
                    self.assertEqual(len(ids), len(set(ids)), "Duplicate IDs")
                    for tag, attrs in page.nodes:
                        for key in ("href", "src"):
                            address = attrs.get(key)
                            if not address:
                                continue
                            url = urlsplit(address)
                            if url.scheme or url.netloc:
                                continue
                            if not url.path:
                                if url.fragment:
                                    self.assertIn(url.fragment, ids)
                                continue
                            target = (folder / unquote(url.path)).resolve()
                            self.assertTrue(target.is_relative_to(folder.resolve()),
                                            f"Cross-version resource: {address}")
                            self.assertTrue(target.is_file(), f"Missing {address}")
                            if tag == "a" and url.fragment:
                                linked = Document(target)
                                target_ids = [a["id"] for _, a in linked.nodes if "id" in a]
                                self.assertIn(url.fragment, target_ids)

    def test_subscription_scripts_and_controls_are_preserved(self):
        for name in PAGES:
            reference = Document(ROOT / "bleu" / name)
            scripts = re.findall(r"<script>(.*?)</script>", reference.source, re.S)
            for version in VERSIONS:
                with self.subTest(version=version, page=name):
                    page = Document(ROOT / version / name)
                    self.assertEqual(re.findall(r"<script>(.*?)</script>", page.source, re.S),
                                     scripts)
                    for tag, keys in (("input", ("id", "name", "type", "value", "required")),
                                      ("form", ("id", "action", "method")),
                                      ("button", ("type",))):
                        self.assertEqual(page.attributes(tag, keys),
                                         reference.attributes(tag, keys))

    def test_brand_names_do_not_leak_to_another_version(self):
        for version, brand in (("", "Maison et Jardin"), ("auto-plus", "Auto Plus"),
                               ("bleu", "Maison et Jardin")):
            for name in PAGES:
                with self.subTest(version=version, page=name):
                    source = (ROOT / version / name).read_text()
                    title = re.search(r"<title>(.*?)</title>", source, re.S).group(1)
                    self.assertIn("Rain Info by " + brand, title)
                    self.assertNotIn("<", title)
                    self.assertIn("19,99 €", source)
                    self.assertIn("1,99 €", source)
                    other = "Maison et Jardin" if version == "auto-plus" else "Auto Plus"
                    self.assertNotIn(other, source)

    def test_blue_archive_matches_the_version_before_redesign(self):
        checksums = json.loads((ROOT / "tests" / "blue-8273167-sha256.json").read_text())
        for name, expected in checksums.items():
            with self.subTest(file=name):
                actual = hashlib.sha256((ROOT / "bleu" / name).read_bytes()).hexdigest()
                self.assertEqual(actual, expected, "The preserved blue version changed")


if __name__ == "__main__":
    unittest.main()

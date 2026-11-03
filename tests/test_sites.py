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
                               ("bleu", None)):
            for name in PAGES:
                with self.subTest(version=version, page=name):
                    source = (ROOT / version / name).read_text()
                    title = re.search(r"<title>(.*?)</title>", source, re.S).group(1)
                    if brand:
                        self.assertIn("Rain Info by " + brand, title)
                    else:
                        self.assertTrue(title.startswith("Rain Info"))
                        self.assertNotRegex(source.lower(), r"maison|jardin")
                        self.assertFalse(any(tag == "img" and "publisher-logo" in attrs.get("class", "")
                                             for tag, attrs in Document(ROOT / version / name).nodes))
                    self.assertNotIn("<", title)
                    self.assertIn("16,99 €", source)
                    self.assertIn("1,42 €", source)
                    self.assertNotIn("19,99 €", source)
                    self.assertNotIn("1,67 €", source)
                    self.assertIn("1,99 €", source)
                    other = "Maison et Jardin" if version == "auto-plus" else "Auto Plus"
                    self.assertNotIn(other, source)

    def test_blue_visual_assets_match_the_version_before_redesign(self):
        checksums = json.loads((ROOT / "tests" / "blue-8273167-sha256.json").read_text())
        for name, expected in checksums.items():
            if not name.startswith("assets/"):
                continue
            with self.subTest(file=name):
                actual = hashlib.sha256((ROOT / "bleu" / name).read_bytes()).hexdigest()
                self.assertEqual(actual, expected, "The preserved blue version changed")

    def test_blue_authorized_free_download_and_unbranding_are_preserved(self):
        checksums = json.loads((ROOT / "tests" / "blue-rain-info-20261103-sha256.json").read_text())
        for name, expected in checksums.items():
            with self.subTest(file=name):
                self.assertEqual(hashlib.sha256((ROOT / "bleu" / name).read_bytes()).hexdigest(), expected)

    def test_free_downloads_use_the_official_stores_without_checkout(self):
        expected = {"ios": "https://apps.apple.com/app/id6535656223",
                    "android": "https://play.google.com/store/apps/details?id=com.raintoday.rainalerts"}
        for version in VERSIONS:
            with self.subTest(version=version):
                page = Document(ROOT / version / "index.html")
                stores = [(attrs.get("data-store"), attrs.get("href")) for tag, attrs in page.nodes
                          if tag == "a" and attrs.get("data-store")]
                for platform, address in expected.items():
                    self.assertIn((platform, address), stores)
                self.assertIn('id="telecharger"', page.source)
                self.assertLess(page.source.index('id="telecharger"'), page.source.index('<form id="pay-form"'))
                payment = Document(ROOT / version / "paiement.html")
                self.assertIn(("index.html#telecharger",), payment.attributes("a", ("href",)))

    def test_maison_et_jardin_keeps_the_gardening_focus(self):
        for name in PAGES:
            with self.subTest(page=name):
                source = (ROOT / name).read_text()
                self.assertNotRegex(source.lower(), r"\b(moto|motard|motards|trajets?)\b")
                self.assertRegex(source.lower(), r"\b(arrosage|arroser)\b")
                self.assertRegex(source.lower(), r"\b(tonte|tondre)\b")


if __name__ == "__main__":
    unittest.main()

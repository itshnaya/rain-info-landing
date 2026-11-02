# Rain Info by Maison et Jardin — landing page

Page d'accueil FR de l'application Rain Info by Maison et Jardin (alertes pluie à la minute). Site statique : `index.html`, `paiement.html` et `assets/`.

- Publication existante : https://itshnaya.github.io/rain-info-landing/ (GitHub Pages, branche `main`, racine du dépôt).
- Identité Maison et Jardin : `assets/brand.css` et `assets/maison-et-jardin.png`. Logo officiel récupéré le 02/11/2026 depuis le site https://maisonetjardin.co/ (logo déclaré dans les métadonnées de l'organisation). Les marges du fichier d'origine sont ajustées à l'affichage par CSS.
- Identité renforcée le 03/11/2026 : grand logo centré, bandeau magazine, palette blanche/noire/brune, typographies Inter/Montserrat/Playfair Display, signature « by Maison et Jardin » en premier plan sur l'accueil, les formules et le paiement. Présentation claire identique quel que soit le thème du téléphone.
- Palette corrigée le 03/11/2026 après comparaison du site de référence : blanc `#ffffff`, noir `#000000` / `#1a1a1a`, gris clairs `#fafafa` / `#f3f4f6`, brun `#8b7355`. Les fonds crème et les bruns adaptés ont été retirés. Les petits textes restent noirs pour leur lisibilité.

## Trois versions, trois adresses

| Version | Adresse | Sources |
| --- | --- | --- |
| Maison et Jardin | https://itshnaya.github.io/rain-info-landing/ | Racine et `assets/` |
| Auto Plus | https://itshnaya.github.io/rain-info-landing/auto-plus/ | `auto-plus/` |
| Bleue avant la refonte | https://itshnaya.github.io/rain-info-landing/bleu/ | `bleu/` |

Chaque version possède sa propre page de paiement et ses propres styles. Aucun lien de paiement ne renvoie vers une autre version. Le dépôt et la publication GitHub Pages sont communs.

La copie bleue conserve exactement les quatre fichiers publics du commit `8273167` : l'état immédiatement antérieur à la grande refonte Maison et Jardin, avec le petit logo et la mention « by Maison et Jardin ».

Le logo Auto Plus est celui fourni sur la page partenaire du Mondial de l'Auto 2026 : https://mondial.paris/partenaires/auto-plus ; fichier https://mondial.paris/wp-content/uploads/salons-pms/2026/06/logo-autoplus-150.jpg. Le rouge `#ca2835` est extrait de ce logo. L'accès automatique au site Auto Plus étant refusé, cette variante ne prétend pas reproduire sa feuille de styles exacte.

## Vérifications

`python3 -m unittest discover -s tests -v` vérifie les liens et ressources, l'isolation des trois parcours, les formulaires, ainsi que l'intégrité de la copie bleue. Compléter par une vérification visuelle mobile et ordinateur avant publication.

- Aperçu local : `python3 -m http.server 8000` puis http://localhost:8000
- Paiement : `paiement.html` (nom, e-mail, formule, CGV). Renseigner les Stripe Payment Links dans `PAYMENT_LINKS` de `paiement.html` ; sans lien, rien n est envoyé ni enregistré.
- Prix : 1,99 €/mois (confirmé par Claire le 2026-11-02) ; 19,99 €/an (provisoire, à confirmer).
- Reste à faire : prix définitifs, liens Stripe, liens App Store / Google Play, pages légales.

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

## Présentation trajets et motards — 03/11/2026

Les pages Maison et Jardin et Auto Plus présentent la préparation des trajets à moto, à vélo ou à pied : nouveau visuel, exemples d'usage, hiérarchie éditoriale et question dédiée aux motards. Les alertes restent décrites comme localisées autour de la position ; aucune prévision sur un itinéraire entier n'est annoncée. La version `bleu/` est inchangée.

- Styles propres à chaque version : `assets/travel.css` et `auto-plus/assets/travel.css`.
- Visuel livré : `assets/trajet-moto-averse-v1.jpg` et `auto-plus/assets/trajet-moto-averse-v1.jpg` ; même composition, enregistrée en JPEG pour réduire le poids de chargement, sans retouche de la scène.
- Création : outil intégré `image_gen` (mode par défaut de la compétence imagegen), sans appel CLI ni nouvelle clé API. Image d'illustration générée, sans marque ni personnage réel identifié ; l'alerte en surimpression est explicitement présentée comme un exemple.
- Original conservé dans le dossier des images générées de cette conversation : `exec-4e56c5d6-7ab0-4a75-b077-925d2cfdc31f.png`.

Prompt exact du visuel :

> Use case: photorealistic-natural. Asset type: premium editorial website hero photograph, portrait 4:5 composition, no text. Create a calm, authentic French countryside scene before an approaching rain shower. An adult motorcyclist wearing a matte black full-face helmet, practical black textile riding jacket, riding trousers and boots is standing safely on a wide dry gravel turnout, entirely off the road, beside a parked black touring motorcycle on its side stand. They are checking a smartphone before departure, not riding. The phone screen faces the person and is not readable. A quiet winding country lane, a leafy hedge, distant low hills and textured blue-grey rain clouds form the background. Soft natural daylight still illuminates the rider and motorcycle. Realistic fabric, gravel and foliage textures; refined magazine photography, subtle film grain, natural neutral whites, charcoal and greens, no heavy colour grade. Show the rider and most of the motorcycle together, with room around the subject for a tasteful web crop; centre the meaningful action and leave the lower quarter visually quiet for an HTML weather-card overlay. Eye-level three-quarter viewpoint, 50mm lens feeling, restrained depth of field. No logos, brand emblems, lettering, watermark, graphics or interface. No rain falling on the rider, no risky behaviour, no traffic in motion, no neon effects.

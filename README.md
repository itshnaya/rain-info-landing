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

La copie bleue conserve l'identité visuelle du commit `8273167`, avec le petit logo et la mention « by Maison et Jardin ». Le 03/11/2026, la demande explicite de téléchargement gratuit sur les trois sites autorise l'ajout des liens des stores, la correction du comparatif freemium et une sortie gratuite depuis le paiement. Son logo et sa feuille `assets/brand.css` restent identiques au commit d'origine.

Le logo Auto Plus est celui fourni sur la page partenaire du Mondial de l'Auto 2026 : https://mondial.paris/partenaires/auto-plus ; fichier https://mondial.paris/wp-content/uploads/salons-pms/2026/06/logo-autoplus-150.jpg. Le rouge `#ca2835` est extrait de ce logo. L'accès automatique au site Auto Plus étant refusé, cette variante ne prétend pas reproduire sa feuille de styles exacte.

## Vérifications

`python3 -m unittest discover -s tests -v` vérifie les liens et ressources, l'isolation des trois parcours, les formulaires, ainsi que l'intégrité de la copie bleue. Compléter par une vérification visuelle mobile et ordinateur avant publication.

- Aperçu local : `python3 -m http.server 8000` puis http://localhost:8000
- Paiement : `paiement.html` (nom, e-mail, formule, CGV). Renseigner les Stripe Payment Links dans `PAYMENT_LINKS` de `paiement.html` ; sans lien, rien n est envoyé ni enregistré.
- Prix : 1,99 €/mois (confirmé par Claire le 2026-11-02) ; 19,99 €/an (provisoire, à confirmer).
- Reste à faire : prix définitifs, liens Stripe, liens App Store / Google Play, pages légales.

## Identité et usages — 03/11/2026

Maison et Jardin présente les usages au jardin et à la maison : décider d'arroser ou d'attendre une pluie, repérer un créneau pour tondre, rentrer le linge et les coussins de terrasse, penser aux fenêtres ouvertes. Le comparatif gratuit/Premium est placé juste après l'introduction, avec des exemples concrets pour la maison et le jardin et une colonne Premium contrastée. Les contenus existants sont adaptés, sans ajout de section.

Auto Plus présente la préparation des trajets à moto, avec un exemple de début de pluie dans 12 minutes, intensité modérée et fin prévue à 08 h 45. Ce visuel est clairement illustratif, sans météo en direct ni calcul d'itinéraire.

- Styles propres à chaque version : `assets/garden.css` et, pour le retour Auto Plus à sa première version (`1096b00`), `auto-plus/assets/brand.css` et `auto-plus/assets/v1-return.css`. Le grand logo centré, le téléphone radar et les cartes V1 sont repris ; le téléchargement gratuit, les textes noirs et les informations produit vérifiées sont conservés. Tableau et répétitions retirés. Les anciennes compositions restent disponibles pour les pages en cache.
- Visuel actif : `assets/jardin-avant-pluie-v1.jpg` pour Maison et Jardin. Auto Plus utilise à nouveau les illustrations de téléphone en HTML/CSS de la V1. L'ancienne photo `auto-plus/assets/trajet-moto-averse-v1.jpg` reste archivée. Les JPEG ont été enregistrés sans retouche de la scène.
- Création : outil intégré `image_gen` (mode par défaut de la compétence imagegen), sans appel CLI ni nouvelle clé API. Image d'illustration générée, sans marque ni personnage réel identifié ; l'alerte en surimpression est explicitement présentée comme un exemple.
- Original conservé dans le dossier des images générées de cette conversation : `exec-4e56c5d6-7ab0-4a75-b077-925d2cfdc31f.png`.

Prompt exact du visuel motard, utilisé par Auto Plus :

> Use case: photorealistic-natural. Asset type: premium editorial website hero photograph, portrait 4:5 composition, no text. Create a calm, authentic French countryside scene before an approaching rain shower. An adult motorcyclist wearing a matte black full-face helmet, practical black textile riding jacket, riding trousers and boots is standing safely on a wide dry gravel turnout, entirely off the road, beside a parked black touring motorcycle on its side stand. They are checking a smartphone before departure, not riding. The phone screen faces the person and is not readable. A quiet winding country lane, a leafy hedge, distant low hills and textured blue-grey rain clouds form the background. Soft natural daylight still illuminates the rider and motorcycle. Realistic fabric, gravel and foliage textures; refined magazine photography, subtle film grain, natural neutral whites, charcoal and greens, no heavy colour grade. Show the rider and most of the motorcycle together, with room around the subject for a tasteful web crop; centre the meaningful action and leave the lower quarter visually quiet for an HTML weather-card overlay. Eye-level three-quarter viewpoint, 50mm lens feeling, restrained depth of field. No logos, brand emblems, lettering, watermark, graphics or interface. No rain falling on the rider, no risky behaviour, no traffic in motion, no neon effects.

Prompt exact du visuel jardin (outil intégré `image_gen`, original `exec-e8d2fffd-7a6c-4f93-90a7-47042cb79096.png` conservé dans les images générées de cette conversation) :

> Use case: photorealistic-natural. Asset type: elegant French home-and-garden magazine website hero photograph, portrait 4:5 composition, no text. Show a beautiful, believable well-kept home garden before an approaching light rain shower. A healthy green lawn, layered flower beds with subtle white and pale pink flowers, herbs and flowering plants in terracotta pots beside a pale stone terrace. A simple zinc watering can stands near the plants in the foreground, not pouring water. A compact unbranded push lawnmower is parked unobtrusively at the side of the lawn, illustrating a decision about when to mow. An attractive modest stone house with climbing greenery is softly visible in the background. Soft daylight on the foliage, textured grey rain clouds in the upper part of the image, no rain currently falling. Refined natural editorial photography, realistic leaves, soil, stone and grass, neutral whites and natural greens, no artificial colour grade. Keep the important plants, watering can and lawn within the central area so a landscape mobile crop remains legible, with a little quiet foreground for an HTML weather-card overlay. Calm and practical rather than dramatic. No people, motorcycle, car, logos, lettering, watermark, graphic overlays or interface.

## Téléchargement gratuit et référence produit — 03/11/2026

Les trois versions permettent d'installer gratuitement **Rain Now**, nom affiché sur les stores, sans utiliser le formulaire Premium :

- App Store : https://apps.apple.com/app/id6535656223 — `com.rain.today`, prix de téléchargement vérifié à 0 via l'API officielle Apple.
- Google Play : https://play.google.com/store/apps/details?id=com.raintoday.rainalerts.
- Source principale fournie par la propriétaire : https://nowinnov.com/ ; complétée par les fiches officielles Apple et Google Play.

Répartition affichée : gratuit avec 60 minutes de pluie à la minute, météo sur 7 jours et alertes pour la ville ; Premium avec jusqu'à 240 minutes, radar animé jusqu'à 2 h, alertes à la position exacte, prévisions étendues et suppression des publicités. Widgets et Live Activity sont décrits pour les iPhone compatibles. L'App Store et Nowinnov annoncent 30 jours, tandis que la fiche Android mentionne encore 16 jours dans ses nouveautés : l'affichage commun précise donc « jusqu'à 30 jours selon la version ». Aucun chiffre d'avis, d'utilisateurs ou de précision garantie n'est repris.

Les prix des formules web antérieurement autorisés restent inchangés. Les tarifs et offres des stores peuvent dépendre de la plateforme et du pays. Les scripts d'abonnement sont conservés ; aucun paiement réel n'est activé par cette modification.

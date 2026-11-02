# Rain Info by Maison et Jardin — landing page

Page d'accueil FR de l'application Rain Info by Maison et Jardin (alertes pluie à la minute). Site statique : `index.html`, `paiement.html` et `assets/`.

- Publication existante : https://itshnaya.github.io/rain-info-landing/ (GitHub Pages, branche `main`, racine du dépôt).
- Identité Maison et Jardin : `assets/brand.css` et `assets/maison-et-jardin.png`. Logo officiel récupéré le 02/11/2026 depuis le site https://maisonetjardin.co/ (logo déclaré dans les métadonnées de l'organisation). Les marges du fichier d'origine sont ajustées à l'affichage par CSS.
- Identité renforcée le 03/11/2026 : grand logo centré, bandeau magazine, palette blanche/noire/brune, typographies Inter/Montserrat/Playfair Display, signature « by Maison et Jardin » en premier plan sur l'accueil, les formules et le paiement. Présentation claire identique quel que soit le thème du téléphone.

- Aperçu local : `python3 -m http.server 8000` puis http://localhost:8000
- Paiement : `paiement.html` (nom, e-mail, formule, CGV). Renseigner les Stripe Payment Links dans `PAYMENT_LINKS` de `paiement.html` ; sans lien, rien n est envoyé ni enregistré.
- Prix : 1,99 €/mois (confirmé par Claire le 2026-11-02) ; 19,99 €/an (provisoire, à confirmer).
- Reste à faire : prix définitifs, liens Stripe, liens App Store / Google Play, pages légales.

# Rain Info by Auto Plus

Copie de la landing Rain Info avec identité Auto Plus, créée le 03/11/2026.

- Adresse : https://itshnaya.github.io/rain-info-landing/auto-plus/
- Paiement : `paiement.html`, dans ce même dossier.
- Ressources propres à cette version : `assets/brand.css` et `assets/auto-plus.jpg`.
- Logo : page partenaire Auto Plus du Mondial de l'Auto 2026, https://mondial.paris/partenaires/auto-plus.
- Rouge principal : `#ca2835`, relevé dans le logo publié. Les couleurs CSS du site Auto Plus n'ont pas pu être vérifiées, son accès automatique étant refusé.
- Prix, formulaires et fonctionnalités repris du site Rain Info. Les liens Stripe restent à renseigner avant tout paiement réel.

Lancer les vérifications depuis la racine : `python3 -m unittest discover -s tests -v`.

Retour à la V1 demandé par Claire le 03/11/2026 : l'accueil repart du fichier `auto-plus/index.html` du commit `1096b00` (première version Auto Plus). Grand logo centré, bandeau rouge, navigation, téléphone radar, cartes et galerie d'origine. `assets/brand.css` est identique à cette V1 ; `assets/v1-return.css` ajoute seulement les textes noirs, le téléchargement gratuit et des espacements resserrés.

La page conserve les quatre sections d'origine utiles : fonctionnalités, illustrations, formules visibles et FAQ. Le tableau contesté et les blocs répétitifs ne sont pas réintroduits. La composition compacte et la photo motard ne sont plus référencées par l'accueil, mais leurs fichiers sont conservés pour les pages en cache.

Le téléchargement gratuit mène aux stores officiels liés depuis https://nowinnov.com/. Les scripts d'abonnement, tarifs et contrôles des formulaires sont conservés ; le mode gratuit reste accessible sans paiement. Les anciennes promesses non vérifiées (renouvellement par e-mail, alertes uniquement payantes) ne sont pas réintroduites.

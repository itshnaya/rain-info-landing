# Rain Info by Auto Plus

Copie de la landing Rain Info avec identité Auto Plus, créée le 03/11/2026.

- Adresse : https://itshnaya.github.io/rain-info-landing/auto-plus/
- Paiement : `paiement.html`, dans ce même dossier.
- Ressources propres à cette version : `assets/brand.css` et `assets/auto-plus.jpg`.
- Logo : page partenaire Auto Plus du Mondial de l'Auto 2026, https://mondial.paris/partenaires/auto-plus.
- Rouge principal : `#ca2835`, relevé dans le logo publié. Les couleurs CSS du site Auto Plus n'ont pas pu être vérifiées, son accès automatique étant refusé.
- Prix, formulaires et fonctionnalités repris du site Rain Info. Les liens Stripe restent à renseigner avant tout paiement réel.

Lancer les vérifications depuis la racine : `python3 -m unittest discover -s tests -v`.

Présentation raccourcie à la demande de Claire le 03/11/2026 : une introduction moto avec le délai avant la pluie, trois bénéfices, le téléchargement gratuit et deux questions. Le tableau comparatif et les sections répétitives sont retirés. Premium se découvre dans un volet facultatif. Tous les paragraphes et titres courants sont noirs (`#111`), les accents reprennent le rouge du logo.

La page d'accueil utilise uniquement `assets/compact.css`. Les anciennes feuilles restent disponibles pour les pages en cache et le paiement. Le visuel existant est conservé dans `assets/trajet-moto-averse-v1.jpg` ; son prompt exact et sa provenance figurent dans le README principal. L'alerte dans la photo est un exemple illustratif (12 minutes, intensité modérée, fin à 08 h 45), pas une prévision en direct.

Le téléchargement gratuit mène directement aux stores officiels liés depuis https://nowinnov.com/. Les scripts d'abonnement, tarifs et contrôles des formulaires sont conservés. La page de paiement reste facultative. Détails, sources et différences de plateformes dans le README principal.

Vérifications de cette simplification : sept tests existants réussis ; affichage contrôlé de 320 à 1440 px, paragraphes noirs, aucun débordement ; téléchargement gratuit et formules annuelle/mensuelle vérifiés. Hauteur fermée : 1 389 px à 1440 px et 2 038 px à 375 px (contre 9 903 et 12 695 px avant correction).

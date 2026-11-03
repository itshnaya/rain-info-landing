# Rain Info : versions autorisées

- Dépôt connu : `itshnaya/rain-info-landing`, branche `main`. Publication GitHub Pages depuis la racine.
- Version Maison et Jardin actuelle : `/`, `index.html`, `paiement.html`, `assets/`. Usages : arrosage, tonte, plantes, linge, terrasse et vie à la maison ; aucun positionnement motard. À la demande de Claire, le comparatif gratuit/Premium est la première section après l'introduction.
- Version Auto Plus : `/auto-plus/`, avec ses propres pages et ressources. Dernière demande de Claire : conserver l'identité V1 (grand logo centré, palette blanche/noire/rouge), remettre une photo de motard roulant sous la pluie, ajouter un comparatif gratuit/Premium et des arguments concrets pour les motards. Le téléchargement gratuit, les textes noirs et les formules visibles restent présents. Utiliser le logo officiel haute définition sur l'accueil et le paiement ; ne plus remplacer la photo par un téléphone au nom du retour V1. L'accueil utilise `assets/brand.css` et `assets/v1-return.css`.
- Copie bleue : `/bleu/`, palette et styles issus du commit `8273167`. Dernière demande de Claire le 03/11/2026 : retirer le logo et toutes les mentions Maison et Jardin, y compris du paiement et des illustrations. Cette version porte uniquement le nom Rain Info. Conserver sa palette bleue, ses styles et le téléchargement gratuit direct demandé précédemment.
- Les trois versions proposent un téléchargement gratuit direct, sans passer par le formulaire d'abonnement. L'application se nomme Rain Now sur les stores ; les identifiants sont ceux liés depuis nowinnov.com.
- Référence produit : nowinnov.com, complétée par les fiches officielles App Store et Google Play. Ne pas présenter les alertes comme exclusivement payantes, ni promettre une mesure de l'humidité du sol ou des prévisions sur un itinéraire complet.
- Pour toute nouvelle déclinaison visuelle, créer une copie séparée avant de modifier l'identité. Conserver les adresses existantes.
- Les liens de navigation et de paiement restent relatifs au dossier de leur version.
- Créer un point de restauration avant modification importante, puis exécuter les tests, vérifier le diff et scanner les secrets avant un push.
- Vérifications : `python3 -m unittest discover -s tests -v`, puis contrôler les pages modifiées sur mobile et ordinateur. Après publication, vérifier les pages réellement servies.
- Ne pas activer un paiement réel ni modifier des données clients dans une tâche de présentation.

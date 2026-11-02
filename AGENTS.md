# Rain Info : versions autorisées

- Dépôt connu : `itshnaya/rain-info-landing`, branche `main`. Publication GitHub Pages depuis la racine.
- Version Maison et Jardin actuelle : `/`, `index.html`, `paiement.html`, `assets/`. Usages : arrosage, tonte, plantes et activités au jardin ; aucun positionnement motard.
- Version Auto Plus : `/auto-plus/`, avec ses propres pages et ressources. Usages : motards, préparation des trajets et délai avant la pluie.
- Copie bleue : `/bleu/`, identité visuelle issue du commit `8273167`. Le 03/11/2026, Claire a explicitement demandé le téléchargement gratuit sur les trois sites : les liens des stores, le comparatif freemium et la sortie gratuite du paiement peuvent donc être ajoutés à cette copie. Préserver sa palette, ses logos et son style initial.
- Les trois versions proposent un téléchargement gratuit direct, sans passer par le formulaire d'abonnement. L'application se nomme Rain Now sur les stores ; les identifiants sont ceux liés depuis nowinnov.com.
- Référence produit : nowinnov.com, complétée par les fiches officielles App Store et Google Play. Ne pas présenter les alertes comme exclusivement payantes, ni promettre une mesure de l'humidité du sol ou des prévisions sur un itinéraire complet.
- Pour toute nouvelle déclinaison visuelle, créer une copie séparée avant de modifier l'identité. Conserver les adresses existantes.
- Les liens de navigation et de paiement restent relatifs au dossier de leur version.
- Créer un point de restauration avant modification importante, puis exécuter les tests, vérifier le diff et scanner les secrets avant un push.
- Vérifications : `python3 -m unittest discover -s tests -v`, puis contrôler les pages modifiées sur mobile et ordinateur. Après publication, vérifier les pages réellement servies.
- Ne pas activer un paiement réel ni modifier des données clients dans une tâche de présentation.

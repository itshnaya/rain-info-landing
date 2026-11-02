# Rain Info : versions autorisées

- Dépôt connu : `itshnaya/rain-info-landing`, branche `main`. Publication GitHub Pages depuis la racine.
- Version Maison et Jardin actuelle : `/`, `index.html`, `paiement.html`, `assets/`.
- Version Auto Plus : `/auto-plus/`, avec ses propres pages et ressources.
- Copie bleue demandée par Claire : `/bleu/`, fichiers publics identiques au commit `8273167`. Préserver cette archive sauf nouvelle demande explicite.
- Pour toute nouvelle déclinaison visuelle, créer une copie séparée avant de modifier l'identité. Conserver les adresses existantes.
- Les liens de navigation et de paiement restent relatifs au dossier de leur version.
- Créer un point de restauration avant modification importante, puis exécuter les tests, vérifier le diff et scanner les secrets avant un push.
- Vérifications : `python3 -m unittest discover -s tests -v`, puis contrôler les pages modifiées sur mobile et ordinateur. Après publication, vérifier les pages réellement servies.
- Ne pas activer un paiement réel ni modifier des données clients dans une tâche de présentation.

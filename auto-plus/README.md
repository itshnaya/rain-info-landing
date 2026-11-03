# Rain Info by Auto Plus

Copie de la landing Rain Info avec identité Auto Plus, créée le 03/11/2026.

- Adresse : https://itshnaya.github.io/rain-info-landing/auto-plus/
- Paiement : `paiement.html`, dans ce même dossier.
- Ressources actives : `assets/brand.css`, `assets/v1-return.css`, `assets/auto-plus-hd-v2.jpg` et `assets/motard-sous-pluie-v2.jpg`.
- Logo haute définition : fichier officiel 512 × 512 fourni par Reworld Media Magazines pour son application Auto Plus, https://apps.apple.com/fr/app/auto-plus-actus-et-essais/id456203438. Récupéré via l'API publique Apple le 03/11/2026, sans agrandissement ni retouche. Source : https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/36/62/11/36621183-8dba-11fb-a4a5-0ab6e3875a75/AppIcon-AutoPlus-0-0-1x_U007emarketing-0-8-0-85-220.png/512x512bb.jpg. Le petit JPEG précédent reste archivé, non référencé par les pages actives.
- Rouge principal : `#ca2835`, relevé dans le logo publié. Les couleurs CSS du site Auto Plus n'ont pas pu être vérifiées, son accès automatique étant refusé.
- Prix, formulaires et fonctionnalités repris du site Rain Info. Les liens Stripe restent à renseigner avant tout paiement réel.

Lancer les vérifications depuis la racine : `python3 -m unittest discover -s tests -v`.

L'identité V1 (`1096b00`) est conservée : grand logo centré, bandeau rouge, navigation et typographies. Dernière correction demandée par Claire : remettre une photo de motard, cette fois en train de rouler sous la pluie, et le comparatif gratuit/Premium. La composition reste en quatre sections : trois bénéfices motards, comparatif, formules visibles et FAQ. La photo remplace le téléphone de l'introduction ; le comparatif remplace la galerie pour limiter la longueur.

Arguments : choisir son départ, prévoir sa tenue et adapter sa pause à la fin annoncée d'une averse. Le visuel de prévision est explicitement illustratif ; aucune promesse de suivi météo d'un itinéraire complet. Les textes courants restent noirs. Les anciennes compositions restent archivées pour les pages en cache.

Le téléchargement gratuit mène aux stores officiels liés depuis https://nowinnov.com/. Les scripts d'abonnement, tarifs et contrôles des formulaires sont conservés ; le mode gratuit reste accessible sans paiement. Les anciennes promesses non vérifiées (renouvellement par e-mail, alertes uniquement payantes) ne sont pas réintroduites.

## Photo motard sous la pluie

- Mode : outil intégré `image_gen`, génération d'une nouvelle photo d'illustration, sans CLI ni retouche de la scène.
- Original conservé : `/Users/claire/.codex/generated_images/01a19dc9-0fc9-7211-aa8b-0c40934beb09/exec-780bda3f-4325-4333-9c4e-e9d9fa5f67e1.png`.
- Fichier intégré : `assets/motard-sous-pluie-v2.jpg`, conversion JPEG pour le chargement web (1122 × 1402).

Prompt exact :

> Use case: photorealistic-natural. Asset type: portrait 4:5 editorial hero photograph for an Auto Plus-branded rain forecast app landing page. Primary request: a motorcyclist riding in the rain. Show a single adult rider in a full-face helmet with closed visor, black waterproof textile motorcycle jacket, trousers, gloves and boots, riding a dark unbranded touring motorcycle at a calm normal pace on a quiet wet French country road during a moderate rain shower. Both hands on the handlebars, eyes facing the road, no phone visible. Three-quarter front view at a natural roadside camera height, entire motorcycle and rider clearly visible within the central composition. Fine raindrops, a light spray from the tyres, realistic wet asphalt reflections, soft grey daylight and green countryside blurred gently in the distance. Attractive, authentic motoring magazine photography, realistic anatomy and motorcycle mechanics, restrained natural colours, no exaggerated storm, no racing pose or dramatic lean. Keep the action in the upper and middle portions of the frame and the lowest quarter visually simple for an HTML weather-card overlay. No logos, visible brand names, text, watermark, graphics or interface.

# ﻿Rapport TP1 : Mission Stéganographie

## Binôme : Anas TAGUI & Mehdi CHABAANE
## Date : 24/11/2025

### 1. Résumé du principe

La stéganographie LSB (Least Significant Bit) est une technique de dissimulation d'information qui exploite la faible sensibilité de l'œil humain aux variations mineures de couleur.

Une image numérique est composée de pixels, chacun étant défini par trois composantes (Rouge, Vert, Bleu) codées sur un octet (8 bits). Le principe consiste à remplacer le dernier bit (le bit de poids faible) de chaque composante par un bit de notre message secret.

Puisque ce bit ne vaut que "1" sur une échelle de 0 à 255, sa modification change la teinte du pixel de manière imperceptible visuellement, mais permet de stocker de l'information binaire récupérable par un programme informatique.

### 2. Résultats des analyses

**Comparaison Visuelle** 

**Observation** : En comparant l'image originale (mon_image.png) et l'image modifiée (image_secrete.png) côte à côte, aucune différence n'est visible à l'œil nu. Les couleurs semblent strictement identiques.

**Analyse Statistique**


Nombre de bits modifiés : 27875

Pourcentage de modification : 21,33%

MSE (Mean Squared Error) : 4.823151125401929e-05

**Carte de Chaleur (Heatmap)**

La carte de chaleur générée par le script d'analyse montre clairement la zone où le message est écrit. Contrairement à l'image normale où tout semble uniforme, la heatmap révèle les pixels exacts dont le LSB a été inversé, concentrés généralement en haut de l'image (puisque le script écrit de gauche à droite, ligne par ligne).

### 3. Limites identifiées

Bien que cette méthode soit efficace pour cacher un message à un observateur humain, elle présente plusieurs faiblesses majeures :

**Fragilité (Compression)** : Si l'image est convertie en JPEG, redimensionnée ou compressée, les bits de poids faible sont altérés ("écrasés" par la compression). Le message est alors définitivement détruit. C'est pourquoi le format PNG est obligatoire.

**Sécurité nulle** : Le message n'est pas chiffré. N'importe qui soupçonnant une stéganographie peut extraire les LSB et lire le texte (ou voir l'en-tête du fichier caché). Pour sécuriser l'échange, il faudrait chiffrer le message (ex: AES) avant de le cacher.

**Détectabilité statistique** : Une analyse statistique poussée (histogramme des couleurs) peut révéler une distribution anormale des bits pairs et impairs, trahissant la présence d'un message caché.


## Mode Opératoire - Mission Stégano

Ce projet permet de dissimuler et d'extraire des messages secrets dans des images via la technique LSB.

### Prérequis

Assurez-vous d'avoir Python installé ainsi que les librairies suivantes :

`pip install pillow numpy matplotlib`


### Structure du projet

**encode.py** : Script pour cacher le message.

**decode.py** : Script pour lire le message.

**analyse.py** : Script pour vérifier les modifications.

**mon_image.png** : Votre image source .

### Guide d'utilisation

**1. Cacher un message (Mehdi)**

Lancez le script d'encodage. Vous pouvez modifier le message directement dans le code ou suivre les instructions si le script est interactif.

`python encode.py`


**Entrée** : mon_image.png

**Sortie** : Crée un fichier image_secrete.png contenant le message.

**2. Lire un message (Anas)**

Si vous recevez une image suspecte, utilisez le script de décodage pour révéler son contenu.

`python decode.py`


**Entrée** : image_secrete.png

**Sortie** : Affiche le texte caché dans le terminal.

**3. Analyser l'image (Expert)**

Pour vérifier la discrétion de la modification, lancez l'outil d'analyse.

`python analyse.py`


**Action** : Compare l'originale et la copie modifiée.

**Sortie** : Affiche le taux d'erreur (MSE) et ouvre une fenêtre montrant la carte des pixels modifiés (Heatmap).


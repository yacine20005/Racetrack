# Projet-AP2

## Structure du projet

Le projet est structuré comme suit :

### Description des fichiers

- `affichage.py` : Ce fichier gère l'affichage du jeu.
- `boutons.py` : Ce fichier contient le code pour les boutons du jeu.
- `conversion.py` : Ce fichier est utilisé pour la conversion des données du jeu.
- `fltk.py` : Ce fichier contient le code pour l'interface utilisateur du jeu.
- `grillage.py` : Ce fichier gère le grillage du jeu.
- `jeu.py` : Ce fichier contient la logique principale du jeu.
- `main.py` : C'est le point d'entrée du jeu.
- `menu.py` : Ce fichier gère le menu du jeu.
- `mouvement.py` : Ce fichier gère les mouvements dans le jeu.
- `sauvegarde.py` : Ce fichier gère la sauvegarde du jeu.
- `solveur.py` : Ce fichier contient le code pour le solveur du jeu.
- `utilitaire.py` : Ce fichier contient des fonctions utilitaires pour le jeu.

## Comment exécuter le projet

Pour exécuter le projet, utilisez la commande suivante dans votre terminal :
python main.py

## Règles du jeu

Le jeu consiste à déplacer un pion sur un plateau de jeu en évitant les obstacles et en atteignant la case d'arrivée. Le pion peut se déplacer dans les huit directions (haut, bas, gauche, droite et les quatre diagonales). Le jeu propose deux modes de règles : "souple" et "strict". Dans le mode "souple", le pion peut se déplacer librement tant qu'il ne rencontre pas d'obstacle. Dans le mode "strict", le pion doit éviter les obstacles en respectant certaines contraintes de mouvement.

## Modes de jeu

Le jeu propose plusieurs modes de jeu :
- Mode "Jouer" : Permet de jouer une nouvelle partie ou de charger une partie sauvegardée.
- Mode "Solveur" : Permet de résoudre automatiquement une partie en utilisant différents algorithmes de résolution (Profondeur, Largeur, Random, Bidirectionnel).
- Mode "Options" : Permet de configurer les options du jeu (choix de la carte, règle du jeu, affichage, choix du solveur).

## Dépendances

Le projet nécessite les dépendances suivantes pour fonctionner :
- Python 3.x
- Tkinter (inclus avec Python)
- PIL (Python Imaging Library) pour la gestion des images

## Captures d'écran

Voici quelques captures d'écran du jeu pour vous aider à mieux comprendre son fonctionnement :

![Capture d'écran 1](images/screenshot1.png)
![Capture d'écran 2](images/screenshot2.png)
![Capture d'écran 3](images/screenshot3.png)

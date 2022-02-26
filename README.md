# 🔫 Gunner 1v1 🔫:

__Comment jouer ? 🎮__



⬇️**Tout d’abord il vous faut des pré-requis:**
- [Python 3.7](https://www.python.org/downloads/, "Téléchargement de python") ou version supérieure
- La dernière version de [Pygame](https://www.pygame.org/download.shtml, "pip install pygame")
##

**📂 Ensuite il va falloir télécharger le jeu:**
- 🖱Cliquez sur le bouton code en haut à droite de la page GitHub:

![🔫 Gunner 1v1 🔫-](https://i.ibb.co/XkmJNVV/Capture-d-e-cran-2022-02-23-a-10-29-46.png)

- 🖱Ensuite cliquer sur « Download Zip »:

![🔫 Gunner 1v1 🔫--1](https://i.ibb.co/bgcgG9t/Capture-d-e-cran-2022-02-23-a-10-32-29.png)

- 🔄Et enfin il faut extraire le fichier compressé 

##

Si vous avez suivis toutes les étapes il vous suffit maintenant de double cliquer sur le fichier « start.bat » (si vous êtes sur windows), si vous êtes sur MacOS vous devez exécuter le programme depuis le terminale avec la commande « python3 main.py ».

##

Gunner 1v1 est un jeu qui se joue à deux sur le meme ordinateur, c’est un jeu de tir en 2D avec un style en pixel art. 🖼 

- Vous devrez tout d’abord cliquer sur le bouton play 🖱

- Ensuite choisissez la couleur de personnage 🎨

- Puis vous atterriez dans l’arène, à vous maintenant d’affronter vos amis pour voire qui sera le champion⚔️

- Les touches pour le personnage de gauche sont: ⌨️

	- W, A, S, D: pour les déplacements
	- E: pour tirer
- Les touches pour le personnage de droite sont: ⌨️

	- Les flèches: pour les déplacements
	- Ctrl gauche: pour tirer
- En haut à gauche vous verrez la vie et le cooldown de l’arme (entièrement réglable):💻

![🔫 Gunner 1v1 🔫--2](https://i.ibb.co/vLPmmww/Capture-d-e-cran-2022-02-23-a-11-17-50.png)

- Dans l’arène des power up pourront spawn: ☄️

	- Il y a deux type de power up:
		- Les coeurs qui permettent de gagner de la vie ❤️

		- Les armes qui vous permettent de tirer instantanément sans attendre la fin du cooldown 🔫

- Une fois un des deux personnages mort il vous suffit d’attendre et une partie sera automatiquement relancer 😄

##

**Maintenant que vous savez comment jouer, comment modifier le jeux ?**

##

**Pour changer la taille de la fenêtre: ↕️**

- Il vous suffit d’ouvrir le fichier « settings » avec un éditeur de texte 📂

- Ensuite rendez vous à la ligne 2:

![🔫 Gunner 1v1 🔫--3](https://i.ibb.co/jRCBz3q/Capture-d-e-cran-2022-02-23-a-19-14-46.png)

- Au niveau de « screen_res_array[« 4 »] », il vous suffira de changer le 4 avec un nombre entre 2 et 5 ou alors « hd »

##

**Pour changer la vie maximum d’un personnage: ❤️**

- Il vous suffit d’ouvrir le fichier « config.ini » avec un éditeur de texte 📂

- Ensuite rendez vous à la ligne 2:

![🔫 Gunner 1v1 🔫--4](https://i.ibb.co/smCW412/Capture-d-e-cran-2022-02-23-a-19-19-12.png)

- Au niveau de « MAX_HEALTH = 4 », il vous suffit de changer le 4 avec n’importe quelle nombre/chiffre entre 1 et l’infinie (le nombre/chiffre correspond au nombre de balle que le personnage pourra se prendre avant de mourir)

##

**Pour changer le temps de rechargement de l’arme: ⌛️**

- Toujours dans le fichier « config.ini » 📂

- Rendez vous à la ligne 3:

![🔫 Gunner 1v1 🔫--5](https://i.ibb.co/XFSDxV5/Capture-d-e-cran-2022-02-23-a-19-30-41.png)

- Au niveau de « WEAPON_CD », il vous suffit de changer le 90 avec n’importe quelle nombre/chiffre entre 1 et l’infinie (cette valeur correspond au nombre d’images durant lesquelles le personnage va recharger et le jeu tourne à 60 FPS sur n’importe quel ordinateur. Donc pour avoir un cooldown de 3 secondes par exemple il suffit de faire 3 * 60 = 180 frames)

##

**Pour changer la gravité: 🌍**

- Toujours dans le fichier « config.ini » 📂

- Rendez vous à la ligne 4:

![🔫 Gunner 1v1 🔫--6](https://i.ibb.co/5F8v0ts/Capture-d-e-cran-2022-02-23-a-20-59-49.png)

- Au niveau de « GRAVITY_MODE », il vous suffit de changer « normal » avec « low ». Cela aura pour effets de diminuer la gravité par 4

##

**⚠️ Le reste ne doit pas êtres changer ⚠️**

# Profitez du jeu !! 😄

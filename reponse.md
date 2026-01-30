# Réponses aux exercices

## Exercice 1 : La map du jeu

1. Combien y a t-il de lieux ?
6
2. Combien y a t-il de passages entre les différents lieux ?
7
3. Quel est le lieu au nord ouest ?
une grotte profonde et sombre
4. Quel est le lieu au nord est ?
un petit chalet pittoresque avec un toit de chaume
5. Quel est le lieu au sud est ?
un marécage sombre et ténébreux
6. Quel est le lieu au sud ouest ?
un énorme château fort avec des douves et un pont levis
7. On peut aller directement de la grotte au château fort
Faux
8. On peut aller directement de la grotte au chalet
Vrai
9. On peut aller directement du marécage au château fort
Vrai
10. On peut aller directement du marécage au chalet
Faux

## Exercice 2 : Structure de game.py

1. Quelle est la classe principale définie dans ce fichier ?
Game
2. Combien a t-elle d’attributs ?
4
3. Combien a t-elle de méthodes ?
5
4. Quel est le constructeur ?
__init__()
5. Quelle est la méthode principale ?
play()
6. A quelle ligne demande t-on le nom du joueur ?
57
7. A quelle ligne demande t-on la commande du joueur ?
67
8. A quelle ligne traite t-on la commande du joueur ?
67
9. A quelle ligne affiche t-on la localisation du joueur au démarrage du jeu ?
91
10. Quelle est la première ligne de code exécutée par l’instruction $ python game.py ?
99
11. Quelles sont les lignes qui définissent les différents lieux ?
33, 35, 37, 39, 41, 43
12. Quel est le type de l’objet qui les regroupe ?
list
13. Quelle est le nom de la variable qui permet d’y faire référence dans ce fichier ?
self.rooms
14. Quelles sont les lignes qui définissent les différents passages entre les lieux ?
48-53
15. A quelle ligne définit on le lieu où est placé le joueur au démarrage du jeu ?
58
16. Combien y a t-il de commandes dans cette version du jeu ?
3
17. A quelles lignes sont elles définies ?
24, 26, 28
18. Quelle est le type de l’objet qui les regroupe ?
dict
19. Quelle est le nom de la variable qui permet d’y faire référence dans ce fichier
self.commands
Pour la ligne 5, room fait référence au fichier
room.py
et Room fait référence à la classe
Room
20. Pour la ligne 5, room fait référence au fichier
room.py
et Room fait référence à la classe
Room
21. Pour la ligne 8, actions fait référence au fichier
actions.py
22. est la méthode qui initialise le jeu.
setup()
23. est le type de l’objet qui permet de stocker les instructions que fournit le joueur au moteur du jeu.
str
24. Il est transformé en un objet de type
list
 par la méthode
split()
 à la ligne
74
 de la méthode
process_command
25. La vérification que la commande est reconnue par le moteur de jeu ou non est faite à la ligne
79
26. Si la commande n’est pas valide, un message d’erreur est affiché à la ligne
80
27. Si la commande est valide, un élément de la chaine de caractère entrée au clavier par le joueur est transformée en un objet de type
Command
 à la ligne
83
28. Si la commande est valide, l’action correspondante est déclenchée à la ligne
84
29. La ligne 96 crée une instance de la classe Game.
Vrai
30. La ligne 96 crée une référence vers une instance de la classe Game.
Faux
31. La ligne 96 appelle la méthode
play()
 sur une instance de la classe
Game

## Exercice 3 : Structure de room.py

1. Quelle est la classe principale définie dans ce fichier ?
Room
2. Combien a t-elle d’attributs ?
3
3. Combien a t-elle de méthodes ?
4
4. Quel est le constructeur ?
__init__()
5. Quelle est le type de l’objet utilisé pour la description du lieu ? Observer un exemple d’appel au constructeur de cette classe dans le fichier game.py.
str
6. Quelle est la variable qui permet d’y faire référence dans ce fichier ?
self.description
7. Quel est le type de l’objet qui regroupe les différentes sorties d’un lieu ?
dict
8. Quelle est la variable qui permet d’y faire référence ?
self.exits
9. Que retourne la méthode get_exit() si la direction passée en paramètre est valide ?
Room
10. Que retourne la méthode get_exit() si la direction passée en paramètre n’est pas valide ?
None
11. Pour la méthode get_exit_string(), quel est le type de la valeur de retour ?
str

## Exercice 4 : Structure de player.py

1. Quelle est la classe principale définie dans ce fichier ?
Player
2. Combien a t-elle d’attributs ?
2
3. Combien a t-elle de méthodes ?
2
4. Quel est le constructeur ?
__init__()
5. Quel est le type de l’objet qui stocke le nom du joueur ?
str
6. Quelle est la variable qui permet d’y faire référence ?
self.name
7. Quel est le type de l’objet qui stocke le lieu dans lequel se trouve le joueur ?
Room
8. Quelle est la variable qui permet d’y faire référence ?
self.current_room
9. Que retourne la méthode move() si le déplacement est valide ?
True
10. Que retourne la méthode move() si le déplacement n’est pas valide ?
False
11. Quelle est la ligne qui permet de déplacer le joueur dans le lieu de destination ?
20

## Exercice 5 : Structure de actions.py

1. Quelle est la classe principale définie dans ce fichier ?
Action
2. Combien a t-elle d’attributs ?
0
3. Combien a t-elle de méthodes d’instance ?
0
4. Combien a t-elle de méthodes de classe ?
0
5. Combien a t-elle de fonctions ?
3
6. Y a t-il un constructeur ?
Faux
7. Les fonctions ont elles toutes la même signature ?
Vrai
8. Combien ont elles de paramètres ?
3
9. De quel type est le premier paramètre ?
Game
10. De quel type est le deuxième paramètre ?
list
11. De quel type est le troisième paramètre ?
int
12. De quel type est la valeur de retour ?
bool

Les fonctions de ce fichier sont des fonctions dites de callback. Elles sont associées à la commande correspondante avec l’attribut Command.action() de la classe Command.

1. Quelle est la fonction de callback associée à la commande help ?
<function Actions.help>
2. Quelle est la fonction de callback associée à la commande quit ?
<function Actions.quit>
3. Quelle est la fonction de callback associée à la commande go ?
<function Actions.go>

Les fonctions de callback ont en argument un objet de type Game et ont donc accès à tous les attributs et toutes les méthodes de cette classe. Pour ces fonctions…

1. Quelle est la variable qui permet d’accéder à la salle courante ?
game.player.current_room
2. Quelle est la variable qui permet d’accéder au nom de la salle courante ?
game.player.current_room.name
3. Quelle est la variable qui permet d’accéder à la description de la salle courante ?
game.player.current_room.description
4. Quelle est la variable qui permet d’accéder aux sorties de la salle courante ?
game.player.current_room.exits

## Exercice 6 : Structure de command.py

1. Quelle est la classe principale définie dans ce fichier ?
Command
2. Combien a t-elle d’attributs ?
4
3. Combien a t-elle de méthodes ?
2
4. Quel est le constructeur ?
__init__()
5. Quel est le type de l’objet qui stocke le nom de la commande ?
str
6. Quelle est la variable qui permet d’y faire référence ?
self.command_word
7. Quel est le type de l’objet qui stocke l’information de ce que fait la commande ?
str
8. Quelle est la variable qui permet d’y faire référence ?
self.help_string
9. Quel est le type de l’objet qui stocke l’action déclenchée par la commande ?
function
10. Quelle est la variable qui permet d’y faire référence ?
self.action
11. Quel est le type de l’objet qui stocke le nombre de paramètres que nécessite par la commande ?
int
12. Quelle est la variable qui permet d’y faire référence ?
self.number_of_parameters
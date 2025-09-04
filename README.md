# ViviEngine : Python 2D Game Engine

Un moteur de jeu 2D simple inspiré de GameMaker Studio, construit avec pygame.

## Installation

Assurez-vous d'avoir Python 3.7+ et pygame installé :

```bash
pip install pygame
pip install -e .
```

## Structure du projet

```
.
├── ViviEngine/
│   ├── __init__.py
│   ├── entity.py
│   ├── game.py
│   ├── scene.py
│   └── utils.py
├── Example/
│   ├── assets/
│   │   ├── fonts/
│   │   ├── images/
│   │   └── sounds/
│   ├── entities/
│   │   ├── bullet.py
│   │   ├── enemy.py
│   │   └── player.py
│   ├── scenes/
│   │   └── gameScene.py
│   └── main.py
├── setup.py
└── README.md

```

## Utilisation de base

### 1. Créer un jeu simple

```python
from utils import *

# Créer le jeu
game = Game(800, 600, "Mon Jeu", 60)

# Créer une scène
class MenuScene(Scene):
    def create(self):
        # Initialisation de la scène
        pass
        
    def step(self):
        super().step()
        # Logique de mise à jour
        
    def draw(self):
        super().draw()
        # Rendu personnalisé

# Ajouter la scène au jeu
menu = MenuScene()
game.add_scene("menu", menu)

# Démarrer le jeu
game.init_scene("menu")
game.run()
```

### 2. Créer des entités

```python
class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = 200
        self.sprite_index = "player_sprite"
        
    def create(self):
        super().create()
        # Initialisation de l'entité
        
    def step(self):
        super().step()
        
        # Déplacement avec les flèches
        if keyboard_check(pygame.K_LEFT):
            self.x -= self.speed * self.scene.game.get_delta_time()
        if keyboard_check(pygame.K_RIGHT):
            self.x += self.speed * self.scene.game.get_delta_time()
            
    def draw(self):
        super().draw()
        # Rendu personnalisé si nécessaire
```

## Classes principales

### Game

La classe principale qui gère tout le jeu.

```python
game = Game(width=800, height=600, title="Mon Jeu", fps=60)
```

**Méthodes principales :**
- `add_scene(name, scene)` : Ajoute une scène au jeu
- `switch_scene(name)` : Change de scène (à la fin du frame)
- `init_scene(name)` : Initialise et active une scène immédiatement
- `run()` : Lance la boucle de jeu
- `quit()` : Ferme le jeu proprement

### Scene

Représente une "room" ou niveau de jeu.

**Méthodes à override :**
- `create()` : Appelé lors de l'initialisation
- `step()` : Appelé chaque frame pour la logique
- `draw()` : Appelé chaque frame pour le rendu
- `cleanup()` : Appelé lors de la fermeture

**Méthodes utiles :**
- `add_entity(entity)` : Ajoute une entité à la scène
- `remove_entity(entity)` : Supprime une entité
- `get_entities_of_type(type)` : Trouve toutes les entités d'un type
- `count_entities_of_type(type)` : Compte les entités d'un type

### Entity

Classe de base pour tous les objets de jeu.

**Propriétés importantes :**
- `x, y` : Position
- `sprite_index` : Nom du sprite à utiliser
- `sprite_width, sprite_height` : Dimensions du sprite
- `image_xscale, image_yscale` : Échelles de rendu
- `image_angle` : Rotation en degrés
- `image_alpha` : Transparence (0.0 à 1.0)
- `depth` : Profondeur pour l'ordre de rendu
- `active` : Si false, step() n'est pas appelé
- `visible` : Si false, draw() n'est pas appelé

**Méthodes à override :**
- `create()` : Initialisation
- `step()` : Logique de mise à jour
- `draw()` : Rendu personnalisé
- `cleanup()` : Nettoyage

**Méthodes utiles :**
- `destroy()` : Marque l'entité pour suppression
- `set_sprite(name)` : Change le sprite
- `distance_to(other)` : Distance vers une autre entité
- `direction_to(other)` : Angle vers une autre entité
- `bbox_collision(other)` : Test de collision avec une autre entité

## Fonctions utilitaires (utils.py)

### Gestion des assets

```python
# Charger tous les assets depuis le dossier "assets"
load_assets("assets")

# Récupérer des assets
sprite = get_sprite("player")
sound = get_sound("explosion")
font = get_font("main_font")
```

### Rendu

```python
# Effacer l'écran
draw_clear((64, 128, 255))  # RGB

# Dessiner un sprite
draw_sprite(x, y, "sprite_name", xscale=1, yscale=1, angle=0)

# Dessiner du texte
draw_text(x, y, "Hello World", scale=1, font_name="main_font")

# Définir couleur et alpha
draw_set_color((255, 0, 0))  # Rouge
draw_set_alpha(0.5)  # Semi-transparent

# Formes géométriques
draw_rectangle(x, y, width, height, filled=True)
draw_circle(x, y, radius, filled=True)
draw_line(x1, y1, x2, y2, width=1)
```

### Surfaces

```python
# Créer une surface
surface = surface_create(width, height)

# Changer la cible de rendu
surface_set_target(surface)
# ... dessiner sur la surface ...
surface_reset_target()

# Dessiner la surface
surface_draw(x, y, surface, xscale=1, yscale=1)
```

### Fenêtre

```python
# Taille de la fenêtre
width, height = window_get_size()
window_set_size(1024, 768)
```

### Caméra

```python
# Créer une caméra
cam = camera_create()

# Configurer la caméra
camera_set_view_size(cam, 800, 600)
camera_set_view_port(cam, 0, 0, 800, 600)
camera_set_view_pos(cam, x, y)
camera_set_active(cam)

# Récupérer infos caméra
x, y = camera_get_view_pos()
w, h = camera_get_view_size()
```

### Entrées clavier

```python
# Vérifier les touches
if keyboard_check_pressed(pygame.K_SPACE):  # Vient d'être pressé
    print("Espace pressé!")
    
if keyboard_check(pygame.K_LEFT):  # Maintenu
    player.x -= 5
    
if keyboard_check_released(pygame.K_ENTER):  # Vient d'être relâché
    print("Entrée relâchée!")

# Utiliser des caractères
if keyboard_check('a'):  # Touche 'a'
    print("A maintenu")
```

### Entrées souris

```python
# Boutons souris (1=gauche, 2=milieu, 3=droite)
if mouse_check_pressed(1):
    print("Clic gauche!")
    
if mouse_check(1):
    print("Bouton gauche maintenu")
    
# Position souris
x, y = mouse_get_x(), mouse_get_y()
```

### Entités

```python
# Créer une entité dans la scène courante
player = entity_create(x, y, Player)

# Détruire une entité
entity_destroy(enemy)
```

### Sons

```python
# Jouer un son
play_sound("explosion", volume=0.8)

# Arrêter un son
stop_sound("music")
```

### Fonctions mathématiques

```python
# Nombres aléatoires
val = random_range(0.0, 10.0)  # Float
num = random_int(1, 6)  # Entier (dé)

# Utilitaires
val = clamp(value, 0, 100)  # Limiter une valeur
interpolated = lerp(start, end, 0.5)  # Interpolation

# Géométrie
dist = distance(x1, y1, x2, y2)
angle = point_direction(x1, y1, x2, y2)  # En degrés

# Vecteurs
vx = lengthdir_x(speed, direction)
vy = lengthdir_y(speed, direction)
```

## Exemple complet

Voir `example.py` pour un exemple complet avec :
- Un joueur contrôlable avec les flèches/WASD
- Des ennemis qui suivent le joueur
- Un système de tir avec la souris
- Génération d'ennemis automatique

Pour lancer l'exemple :

```bash
python Example/main.py
```

## Structure des assets

Le moteur peut charger automatiquement vos assets si vous organisez votre dossier ainsi :

```
Example/assets/
├── images/
│   ├── player.png
│   ├── enemy.png
│   └── bullet.png
├── sounds/
│   ├── shoot.wav
│   └── explosion.mp3
└── fonts/
    └── main_font.ttf
```

Utilisez `load_assets("assets")` pour tout charger automatiquement.

## Conseils d'optimisation

1. **Delta Time** : Utilisez `self.scene.game.get_delta_time()` pour des mouvements indépendants du framerate
2. **Profondeur** : Utilisez la propriété `depth` pour contrôler l'ordre de rendu
3. **États d'entité** : Utilisez `active` et `visible` pour optimiser les performances
4. **Surfaces** : Utilisez les surfaces pour des effets complexes ou du caching
5. **Collisions** : Implémentez vos propres systèmes de collision selon vos besoins

## Fonctionnalités avancées

### Gestion des collisions

```python
# Dans votre entité
if self.bbox_collision(other_entity):
    # Collision détectée
    
# Vérifier un point
if self.point_in_bbox(mouse_x, mouse_y):
    # Souris sur l'entité
```

### Système de particules simple

```python
class Particle(Entity):
    def __init__(self, x, y, vx, vy, life):
        super().__init__(x, y)
        self.vx = vx
        self.vy = vy
        self.life = life
        self.max_life = life
        
    def step(self):
        super().step()
        dt = self.scene.game.get_delta_time()
        
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.life -= dt
        
        self.image_alpha = self.life / self.max_life
        
        if self.life <= 0:
            self.destroy()
```

### Changement de scènes avec transition

```python
class FadeTransition(Entity):
    def __init__(self, target_scene, fade_speed=2.0):
        super().__init__(0, 0)
        self.target_scene = target_scene
        self.fade_speed = fade_speed
        self.alpha = 0
        self.fading_out = True
        
    def step(self):
        dt = self.scene.game.get_delta_time()
        
        if self.fading_out:
            self.alpha += self.fade_speed * dt
            if self.alpha >= 1:
                self.alpha = 1
                self.scene.game.switch_scene(self.target_scene)
                self.fading_out = False
        else:
            self.alpha -= self.fade_speed * dt
            if self.alpha <= 0:
                self.destroy()
                
    def draw(self):
        w, h = window_get_size()
        draw_set_color((0, 0, 0))
        draw_set_alpha(self.alpha)
        draw_rectangle(0, 0, w, h, True)
        draw_set_alpha(1.0)
```

## Licence

Ce moteur est fourni tel quel pour des fins éducatives et de prototypage. Utilisez pygame selon sa propre licence.

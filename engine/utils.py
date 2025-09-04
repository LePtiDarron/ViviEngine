import pygame
import os
from typing import Dict, Any, Tuple, Optional, Union
import math

# Variables globales du moteur (initialisées par Game)
_game_instance = None
_screen = None
_clock = None

# Stockage des assets
_sprites: Dict[str, pygame.Surface] = {}
_sounds: Dict[str, pygame.mixer.Sound] = {}
_fonts: Dict[str, pygame.font.Font] = {}

# État du rendu
_current_surface = None
_render_color = (255, 255, 255)
_render_alpha = 255

# Gestion de la caméra
_cameras: Dict[int, Dict[str, Any]] = {}
_active_camera = None
_next_camera_id = 0

# État des entrées
_keys_pressed = set()
_keys_held = set()
_keys_released = set()
_mouse_pressed = set()
_mouse_held = set()
_mouse_released = set()
_mouse_x = 0
_mouse_y = 0

def load_assets(assets_folder: str = "assets"):
    """
    Charge tous les assets depuis un dossier.
    
    Args:
        assets_folder: Chemin vers le dossier des assets
    """
    global _sprites, _sounds, _fonts
    
    if not os.path.exists(assets_folder):
        print(f"Warning: Assets folder '{assets_folder}' not found!")
        return
    
    # Charger les images
    images_folder = os.path.join(assets_folder, "images")
    if os.path.exists(images_folder):
        for filename in os.listdir(images_folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                name = os.path.splitext(filename)[0]
                path = os.path.join(images_folder, filename)
                try:
                    _sprites[name] = pygame.image.load(path).convert_alpha()
                    print(f"Loaded sprite: {name}")
                except pygame.error as e:
                    print(f"Error loading sprite {filename}: {e}")
    
    # Charger les sons
    sounds_folder = os.path.join(assets_folder, "sounds")
    if os.path.exists(sounds_folder):
        for filename in os.listdir(sounds_folder):
            if filename.lower().endswith(('.wav', '.mp3', '.ogg')):
                name = os.path.splitext(filename)[0]
                path = os.path.join(sounds_folder, filename)
                try:
                    _sounds[name] = pygame.mixer.Sound(path)
                    print(f"Loaded sound: {name}")
                except pygame.error as e:
                    print(f"Error loading sound {filename}: {e}")
    
    # Charger les polices
    fonts_folder = os.path.join(assets_folder, "fonts")
    if os.path.exists(fonts_folder):
        for filename in os.listdir(fonts_folder):
            if filename.lower().endswith(('.ttf', '.otf')):
                name = os.path.splitext(filename)[0]
                path = os.path.join(fonts_folder, filename)
                try:
                    _fonts[name] = pygame.font.Font(path, 24)  # Taille par défaut
                    print(f"Loaded font: {name}")
                except pygame.error as e:
                    print(f"Error loading font {filename}: {e}")

def get_sprite(name: str) -> Optional[pygame.Surface]:
    """Récupère un sprite par son nom."""
    return _sprites.get(name)

def get_sound(name: str) -> Optional[pygame.mixer.Sound]:
    """Récupère un son par son nom."""
    return _sounds.get(name)

def get_font(name: str) -> Optional[pygame.font.Font]:
    """Récupère une police par son nom."""
    return _fonts.get(name)

# Fonctions de rendu
def draw_clear(color: Tuple[int, int, int]):
    """
    Efface l'écran avec une couleur.
    
    Args:
        color: Couleur RGB (r, g, b)
    """
    surface = _current_surface or _screen
    if surface:
        surface.fill(color)

def draw_sprite(x: float, y: float, sprite_name: str, xscale: float = 1, yscale: float = 1, angle: float = 0):
    """
    Dessine un sprite.
    
    Args:
        x, y: Position
        sprite_name: Nom du sprite
        xscale, yscale: Échelles
        angle: Angle de rotation en degrés
    """
    sprite = get_sprite(sprite_name)
    if not sprite:
        return
        
    surface = _current_surface or _screen
    if not surface:
        return
    
    # Appliquer les transformations
    if xscale != 1 or yscale != 1:
        new_width = int(sprite.get_width() * abs(xscale))
        new_height = int(sprite.get_height() * abs(yscale))
        sprite = pygame.transform.scale(sprite, (new_width, new_height))
        
        # Gérer le flip horizontal/vertical
        if xscale < 0 and yscale < 0:
            sprite = pygame.transform.flip(sprite, True, True)
        elif xscale < 0:
            sprite = pygame.transform.flip(sprite, True, False)
        elif yscale < 0:
            sprite = pygame.transform.flip(sprite, False, True)
    
    if angle != 0:
        sprite = pygame.transform.rotate(sprite, -angle)  # Pygame utilise le sens contraire
    
    # Appliquer la couleur et l'alpha
    if _render_color != (255, 255, 255) or _render_alpha != 255:
        sprite = sprite.copy()
        if _render_color != (255, 255, 255):
            sprite.fill(_render_color, special_flags=pygame.BLEND_MULT)
        if _render_alpha != 255:
            sprite.set_alpha(_render_alpha)
    
    # Calculer la position finale (centré sur x,y)
    rect = sprite.get_rect()
    rect.center = (int(x), int(y))
    
    surface.blit(sprite, rect)

def draw_text(x: float, y: float, text: str, scale: float = 1, font_name: str = None):
    """
    Dessine du texte.
    
    Args:
        x, y: Position
        text: Texte à dessiner
        scale: Échelle du texte
        font_name: Nom de la police (par défaut: police système)
    """
    surface = _current_surface or _screen
    if not surface:
        return
    
    # Sélectionner la police
    font = None
    if font_name:
        font = get_font(font_name)
    if not font:
        size = int(24 * scale)
        font = pygame.font.Font(None, size)
    
    # Créer la surface de texte
    text_surface = font.render(str(text), True, _render_color)
    
    # Appliquer l'alpha
    if _render_alpha != 255:
        text_surface.set_alpha(_render_alpha)
    
    # Appliquer l'échelle si nécessaire
    if scale != 1 and font_name:  # Seulement si on utilise une police chargée
        new_width = int(text_surface.get_width() * scale)
        new_height = int(text_surface.get_height() * scale)
        text_surface = pygame.transform.scale(text_surface, (new_width, new_height))
    
    surface.blit(text_surface, (int(x), int(y)))

def draw_set_color(color: Tuple[int, int, int]):
    """
    Définit la couleur de rendu.
    
    Args:
        color: Couleur RGB (r, g, b)
    """
    global _render_color
    _render_color = color

def draw_set_alpha(alpha: float):
    """
    Définit l'alpha de rendu.
    
    Args:
        alpha: Valeur alpha (0.0 à 1.0)
    """
    global _render_alpha
    _render_alpha = int(alpha * 255)

# Gestion des surfaces
def surface_create(width: int, height: int) -> pygame.Surface:
    """
    Crée une nouvelle surface.
    
    Args:
        width, height: Dimensions de la surface
        
    Returns:
        Nouvelle surface
    """
    return pygame.Surface((width, height), pygame.SRCALPHA)

def surface_set_target(surface: pygame.Surface):
    """
    Définit la surface de rendu cible.
    
    Args:
        surface: Surface cible (None pour l'écran)
    """
    global _current_surface
    _current_surface = surface

def surface_reset_target():
    """Remet l'écran comme cible de rendu."""
    global _current_surface
    _current_surface = None

def surface_destroy(surface: pygame.Surface):
    """
    Détruit une surface (libère la mémoire).
    
    Args:
        surface: Surface à détruire
    """
    # En Python, on peut juste supprimer la référence
    # Le garbage collector s'en occupera
    pass

def surface_draw(x: float, y: float, surface: pygame.Surface, xscale: float = 1, yscale: float = 1):
    """
    Dessine une surface.
    
    Args:
        x, y: Position
        surface: Surface à dessiner
        xscale, yscale: Échelles
    """
    target = _current_surface or _screen
    if not target or not surface:
        return
    
    draw_surface = surface
    
    # Appliquer les transformations
    if xscale != 1 or yscale != 1:
        new_width = int(surface.get_width() * abs(xscale))
        new_height = int(surface.get_height() * abs(yscale))
        draw_surface = pygame.transform.scale(surface, (new_width, new_height))
        
        if xscale < 0 and yscale < 0:
            draw_surface = pygame.transform.flip(draw_surface, True, True)
        elif xscale < 0:
            draw_surface = pygame.transform.flip(draw_surface, True, False)
        elif yscale < 0:
            draw_surface = pygame.transform.flip(draw_surface, False, True)
    
    # Appliquer la couleur et l'alpha
    if _render_color != (255, 255, 255) or _render_alpha != 255:
        draw_surface = draw_surface.copy()
        if _render_color != (255, 255, 255):
            draw_surface.fill(_render_color, special_flags=pygame.BLEND_MULT)
        if _render_alpha != 255:
            draw_surface.set_alpha(_render_alpha)
    
    target.blit(draw_surface, (int(x), int(y)))

# Gestion de la fenêtre
def window_get_size() -> Tuple[int, int]:
    """
    Retourne la taille de la fenêtre.
    
    Returns:
        Tuple (largeur, hauteur)
    """
    if _screen:
        return _screen.get_size()
    return (0, 0)

def window_set_size(width: int, height: int):
    """
    Change la taille de la fenêtre.
    
    Args:
        width, height: Nouvelles dimensions
    """
    global _screen
    if _game_instance:
        _screen = pygame.display.set_mode((width, height))
        _game_instance.screen = _screen
        _game_instance.width = width
        _game_instance.height = height

# Gestion de la caméra
def camera_create() -> int:
    """
    Crée une nouvelle caméra.
    
    Returns:
        ID de la caméra créée
    """
    global _next_camera_id
    camera_id = _next_camera_id
    _next_camera_id += 1
    
    _cameras[camera_id] = {
        'view_x': 0,
        'view_y': 0,
        'view_width': 800,
        'view_height': 600,
        'port_x': 0,
        'port_y': 0,
        'port_width': 800,
        'port_height': 600
    }
    
    return camera_id

def camera_set_view_size(camera_id: int, width: int, height: int):
    """
    Définit la taille de la vue de la caméra.
    
    Args:
        camera_id: ID de la caméra
        width, height: Dimensions de la vue
    """
    if camera_id in _cameras:
        _cameras[camera_id]['view_width'] = width
        _cameras[camera_id]['view_height'] = height

def camera_set_view_port(camera_id: int, x: int, y: int, width: int, height: int):
    """
    Définit le viewport de la caméra sur l'écran.
    
    Args:
        camera_id: ID de la caméra
        x, y: Position du viewport
        width, height: Dimensions du viewport
    """
    if camera_id in _cameras:
        cam = _cameras[camera_id]
        cam['port_x'] = x
        cam['port_y'] = y
        cam['port_width'] = width
        cam['port_height'] = height

def camera_set_active(camera_id: int):
    """
    Active une caméra.
    
    Args:
        camera_id: ID de la caméra à activer
    """
    global _active_camera
    if camera_id in _cameras:
        _active_camera = camera_id

def camera_set_view_pos(camera_id: int, x: float, y: float):
    """
    Définit la position de la vue de la caméra.
    
    Args:
        camera_id: ID de la caméra
        x, y: Position de la vue
    """
    if camera_id in _cameras:
        _cameras[camera_id]['view_x'] = x
        _cameras[camera_id]['view_y'] = y

def camera_get_view_pos(camera_id: int = None) -> Tuple[float, float]:
    """
    Retourne la position de la vue de la caméra.
    
    Args:
        camera_id: ID de la caméra (None pour la caméra active)
        
    Returns:
        Tuple (x, y)
    """
    cam_id = camera_id or _active_camera
    if cam_id and cam_id in _cameras:
        cam = _cameras[cam_id]
        return (cam['view_x'], cam['view_y'])
    return (0, 0)

def camera_get_view_size(camera_id: int = None) -> Tuple[int, int]:
    """
    Retourne la taille de la vue de la caméra.
    
    Args:
        camera_id: ID de la caméra (None pour la caméra active)
        
    Returns:
        Tuple (largeur, hauteur)
    """
    cam_id = camera_id or _active_camera
    if cam_id and cam_id in _cameras:
        cam = _cameras[cam_id]
        return (cam['view_width'], cam['view_height'])
    return (800, 600)

def camera_get_view_port(camera_id: int = None) -> Tuple[int, int, int, int]:
    """
    Retourne le viewport de la caméra.
    
    Args:
        camera_id: ID de la caméra (None pour la caméra active)
        
    Returns:
        Tuple (x, y, largeur, hauteur)
    """
    cam_id = camera_id or _active_camera
    if cam_id and cam_id in _cameras:
        cam = _cameras[cam_id]
        return (cam['port_x'], cam['port_y'], cam['port_width'], cam['port_height'])
    return (0, 0, 800, 600)

# Gestion des entités
def entity_create(x: float, y: float, entity_class) -> 'Entity':
    """
    Crée une nouvelle entité.
    
    Args:
        x, y: Position initiale
        entity_class: Classe de l'entité à créer
        
    Returns:
        L'entité créée
    """
    entity = entity_class(x, y)
    
    # Ajouter à la scène courante si possible
    if _game_instance and _game_instance.current_scene:
        _game_instance.current_scene.add_entity(entity)
    
    return entity

def entity_destroy(entity: 'Entity'):
    """
    Détruit une entité.
    
    Args:
        entity: L'entité à détruire
    """
    entity.destroy()

# Gestion des entrées clavier
def keyboard_check_pressed(key: Union[int, str]) -> bool:
    """
    Vérifie si une touche vient d'être pressée.
    
    Args:
        key: Code de la touche ou caractère
        
    Returns:
        True si la touche vient d'être pressée
    """
    if isinstance(key, str):
        key = ord(key.lower())
    return key in _keys_pressed

def keyboard_check(key: Union[int, str]) -> bool:
    """
    Vérifie si une touche est maintenue.
    
    Args:
        key: Code de la touche ou caractère
        
    Returns:
        True si la touche est maintenue
    """
    if isinstance(key, str):
        key = ord(key.lower())
    return key in _keys_held

def keyboard_check_released(key: Union[int, str]) -> bool:
    """
    Vérifie si une touche vient d'être relâchée.
    
    Args:
        key: Code de la touche ou caractère
        
    Returns:
        True si la touche vient d'être relâchée
    """
    if isinstance(key, str):
        key = ord(key.lower())
    return key in _keys_released

# Gestion des entrées souris
def mouse_check_pressed(button: int) -> bool:
    """
    Vérifie si un bouton de souris vient d'être pressé.
    
    Args:
        button: Numéro du bouton (1=gauche, 2=milieu, 3=droite)
        
    Returns:
        True si le bouton vient d'être pressé
    """
    return button in _mouse_pressed

def mouse_check(button: int) -> bool:
    """
    Vérifie si un bouton de souris est maintenu.
    
    Args:
        button: Numéro du bouton (1=gauche, 2=milieu, 3=droite)
        
    Returns:
        True si le bouton est maintenu
    """
    return button in _mouse_held

def mouse_check_released(button: int) -> bool:
    """
    Vérifie si un bouton de souris vient d'être relâché.
    
    Args:
        button: Numéro du bouton (1=gauche, 2=milieu, 3=droite)
        
    Returns:
        True si le bouton vient d'être relâché
    """
    return button in _mouse_released

def mouse_get_x() -> int:
    """
    Retourne la position X de la souris.
    
    Returns:
        Position X de la souris
    """
    return _mouse_x

def mouse_get_y() -> int:
    """
    Retourne la position Y de la souris.
    
    Returns:
        Position Y de la souris
    """
    return _mouse_y

# Fonctions utilitaires supplémentaires
def play_sound(sound_name: str, volume: float = 1.0):
    """
    Joue un son.
    
    Args:
        sound_name: Nom du son
        volume: Volume (0.0 à 1.0)
    """
    sound = get_sound(sound_name)
    if sound:
        sound.set_volume(volume)
        sound.play()

def stop_sound(sound_name: str):
    """
    Arrête un son.
    
    Args:
        sound_name: Nom du son
    """
    sound = get_sound(sound_name)
    if sound:
        sound.stop()

def draw_rectangle(x: float, y: float, width: float, height: float, filled: bool = True):
    """
    Dessine un rectangle.
    
    Args:
        x, y: Position du coin supérieur gauche
        width, height: Dimensions
        filled: Si True, rectangle plein, sinon contour
    """
    surface = _current_surface or _screen
    if not surface:
        return
    
    rect = pygame.Rect(int(x), int(y), int(width), int(height))
    
    if filled:
        pygame.draw.rect(surface, _render_color, rect)
    else:
        pygame.draw.rect(surface, _render_color, rect, 1)

def draw_circle(x: float, y: float, radius: float, filled: bool = True):
    """
    Dessine un cercle.
    
    Args:
        x, y: Position du centre
        radius: Rayon
        filled: Si True, cercle plein, sinon contour
    """
    surface = _current_surface or _screen
    if not surface:
        return
    
    if filled:
        pygame.draw.circle(surface, _render_color, (int(x), int(y)), int(radius))
    else:
        pygame.draw.circle(surface, _render_color, (int(x), int(y)), int(radius), 1)

def draw_line(x1: float, y1: float, x2: float, y2: float, width: int = 1):
    """
    Dessine une ligne.
    
    Args:
        x1, y1: Point de départ
        x2, y2: Point d'arrivée
        width: Épaisseur de la ligne
    """
    surface = _current_surface or _screen
    if not surface:
        return
    
    pygame.draw.line(surface, _render_color, (int(x1), int(y1)), (int(x2), int(y2)), width)

def random_range(min_val: float, max_val: float) -> float:
    """
    Génère un nombre aléatoire dans une plage.
    
    Args:
        min_val: Valeur minimale
        max_val: Valeur maximale
        
    Returns:
        Nombre aléatoire entre min_val et max_val
    """
    import random
    return random.uniform(min_val, max_val)

def random_int(min_val: int, max_val: int) -> int:
    """
    Génère un entier aléatoire dans une plage.
    
    Args:
        min_val: Valeur minimale
        max_val: Valeur maximale
        
    Returns:
        Entier aléatoire entre min_val et max_val (inclus)
    """
    import random
    return random.randint(min_val, max_val)

def clamp(value: float, min_val: float, max_val: float) -> float:
    """
    Limite une valeur dans une plage.
    
    Args:
        value: Valeur à limiter
        min_val: Valeur minimale
        max_val: Valeur maximale
        
    Returns:
        Valeur limitée
    """
    return max(min_val, min(max_val, value))

def lerp(start: float, end: float, factor: float) -> float:
    """
    Interpolation linéaire entre deux valeurs.
    
    Args:
        start: Valeur de départ
        end: Valeur d'arrivée
        factor: Facteur d'interpolation (0.0 à 1.0)
        
    Returns:
        Valeur interpolée
    """
    return start + (end - start) * factor

def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Calcule la distance euclidienne entre deux points.
    
    Args:
        x1, y1: Premier point
        x2, y2: Deuxième point
        
    Returns:
        Distance en pixels
    """
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx * dx + dy * dy)

def point_direction(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Calcule l'angle entre deux points.
    
    Args:
        x1, y1: Premier point
        x2, y2: Deuxième point
        
    Returns:
        Angle en degrés (0-360)
    """
    dx = x2 - x1
    dy = y2 - y1
    angle_rad = math.atan2(-dy, dx)  # -dy car l'axe Y est inversé à l'écran
    angle_deg = math.degrees(angle_rad)
    return (angle_deg + 360) % 360

def lengthdir_x(length: float, direction: float) -> float:
    """
    Calcule la composante X d'un vecteur.
    
    Args:
        length: Longueur du vecteur
        direction: Direction en degrés
        
    Returns:
        Composante X
    """
    return length * math.cos(math.radians(direction))

def lengthdir_y(length: float, direction: float) -> float:
    """
    Calcule la composante Y d'un vecteur.
    
    Args:
        length: Longueur du vecteur
        direction: Direction en degrés
        
    Returns:
        Composante Y
    """
    return -length * math.sin(math.radians(direction))  # -sin car l'axe Y est inversé

# Fonction interne pour gérer les événements pygame
def _handle_pygame_event(event):
    """Gère les événements pygame pour les entrées."""
    global _keys_pressed, _keys_held, _keys_released
    global _mouse_pressed, _mouse_held, _mouse_released, _mouse_x, _mouse_y
    
    # Réinitialiser les états "pressé" et "relâché"
    if event.type == pygame.KEYDOWN:
        _keys_pressed.add(event.key)
        _keys_held.add(event.key)
        if event.key in _keys_released:
            _keys_released.remove(event.key)
    elif event.type == pygame.KEYUP:
        _keys_released.add(event.key)
        if event.key in _keys_held:
            _keys_held.remove(event.key)
        if event.key in _keys_pressed:
            _keys_pressed.remove(event.key)
    elif event.type == pygame.MOUSEBUTTONDOWN:
        _mouse_pressed.add(event.button)
        _mouse_held.add(event.button)
        if event.button in _mouse_released:
            _mouse_released.remove(event.button)
    elif event.type == pygame.MOUSEBUTTONUP:
        _mouse_released.add(event.button)
        if event.button in _mouse_held:
            _mouse_held.remove(event.button)
        if event.button in _mouse_pressed:
            _mouse_pressed.remove(event.button)
    elif event.type == pygame.MOUSEMOTION:
        _mouse_x, _mouse_y = event.pos

def _clear_input_states():
    """Nettoie les états d'entrée à la fin de chaque frame."""
    global _keys_pressed, _keys_released, _mouse_pressed, _mouse_released
    _keys_pressed.clear()
    _keys_released.clear()
    _mouse_pressed.clear()
    _mouse_released.clear()

def _end_frame_cleanup():
    """Nettoyage de fin de frame."""
    _clear_input_states()
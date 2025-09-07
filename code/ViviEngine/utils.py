import pygame
import os
from typing import Dict, List, Any, Tuple, Optional, Union
import math

_sprites: Dict[str, 'Sprite'] = {}
_sounds: Dict[str, pygame.mixer.Sound] = {}
_fonts: Dict[str, pygame.font.Font] = {}

class Sprite:
    """Classe pour gérer les sprites avec support multi-images et centre personnalisé."""
    
    def __init__(self, surface: pygame.Surface, name: str, image_count: int = 1):
        self.name = name
        self.full_surface = surface
        self.image_count = image_count
        self.images: List[pygame.Surface] = []
        
        # Calculer les dimensions d'une seule image
        self.image_width = surface.get_width() // image_count
        self.image_height = surface.get_height()
        
        # Centre par défaut (haut-gauche)
        self.center_x = 0
        self.center_y = 0
        
        # Diviser la surface en images individuelles
        self._split_images()
    
    def _split_images(self):
        """Divise la surface principale en images individuelles."""
        self.images.clear()
        
        for i in range(self.image_count):
            x = i * self.image_width
            # Vérifier que l'image rentre dans la surface
            if x + self.image_width <= self.full_surface.get_width():
                image_rect = pygame.Rect(x, 0, self.image_width, self.image_height)
                image = self.full_surface.subsurface(image_rect).copy()
                self.images.append(image)
            else:
                # Si l'image ne rentre pas, prendre ce qui reste
                remaining_width = self.full_surface.get_width() - x
                if remaining_width > 0:
                    image_rect = pygame.Rect(x, 0, remaining_width, self.image_height)
                    image = self.full_surface.subsurface(image_rect).copy()
                    self.images.append(image)
    
    def get_image(self, index: int = 0) -> pygame.Surface:
        """Retourne l'image à l'index spécifié."""
        if 0 <= index < len(self.images):
            return self.images[index]
        return self.images[0] if self.images else self.full_surface
    
    def set_center(self, x: int, y: int):
        """Définit le centre du sprite (en pixel)."""
        self.center_x = x
        self.center_y = y
    
    def get_width(self) -> int:
        """Retourne la largeur d'une image."""
        return self.image_width
    
    def get_height(self) -> int:
        """Retourne la hauteur d'une image."""
        return self.image_height

def load_sprite(filepath: str, name: Optional[str] = None) -> bool:
    """
    Charge un sprite depuis un fichier.
    
    Args:
        filepath: Chemin vers le fichier image
        name: Nom du sprite (optionnel, utilise le nom du fichier par défaut)
    
    Returns:
        True si le chargement a réussi
    """
    try:
        if name is None:
            name = os.path.splitext(os.path.basename(filepath))[0]
        
        # Charger la surface
        surface = pygame.image.load(filepath).convert_alpha()
        
        # Détecter si c'est un sprite strip
        image_count = 1
        if "_strip" in name:
            try:
                # Extraire le nombre d'images depuis le nom
                strip_part = name.split("_strip")[1]
                image_count = int(strip_part)
                # Enlever la partie _stripN du nom
                name = name.split("_strip")[0]
            except (IndexError, ValueError):
                image_count = 1
        
        # Créer et stocker le sprite
        sprite = Sprite(surface, name, image_count)
        _sprites[name] = sprite
        
        print(f"Sprite '{name}' chargé avec {image_count} image(s)")
        return True
        
    except pygame.error as e:
        print(f"Erreur lors du chargement du sprite '{filepath}': {e}")
        return False

def load_sound(filepath: str, name: Optional[str] = None) -> bool:
    """
    Charge un son depuis un fichier.
    
    Args:
        filepath: Chemin vers le fichier audio
        name: Nom du son (optionnel, utilise le nom du fichier par défaut)
    
    Returns:
        True si le chargement a réussi
    """
    try:
        if name is None:
            name = os.path.splitext(os.path.basename(filepath))[0]
        
        sound = pygame.mixer.Sound(filepath)
        _sounds[name] = sound
        
        print(f"Son '{name}' chargé")
        return True
        
    except pygame.error as e:
        print(f"Erreur lors du chargement du son '{filepath}': {e}")
        return False

def load_font(filepath: str, size: int = 24, name: Optional[str] = None) -> bool:
    """
    Charge une police depuis un fichier.
    
    Args:
        filepath: Chemin vers le fichier de police
        size: Taille de la police
        name: Nom de la police (optionnel, utilise le nom du fichier par défaut)
    
    Returns:
        True si le chargement a réussi
    """
    try:
        if name is None:
            name = os.path.splitext(os.path.basename(filepath))[0]
        
        font = pygame.font.Font(filepath, size)
        _fonts[name] = font
        
        print(f"Police '{name}' chargée (taille {size})")
        return True
        
    except pygame.error as e:
        print(f"Erreur lors du chargement de la police '{filepath}': {e}")
        return False

def get_sprite(name: str) -> Optional[Sprite]:
    """Retourne le sprite avec le nom donné."""
    return _sprites.get(name)

def get_sound(name: str) -> Optional[pygame.mixer.Sound]:
    """Retourne le son avec le nom donné."""
    return _sounds.get(name)

def get_font(name: str) -> Optional[pygame.font.Font]:
    """Retourne la police avec le nom donné."""
    return _fonts.get(name)

def sprite_set_center(name: str, x: int, y: int) -> bool:
    """
    Définit le centre d'un sprite.
    
    Args:
        name: Nom du sprite
        x: Position X du centre
        y: Position Y du centre
    
    Returns:
        True si le sprite existe et que le centre a été défini
    """
    sprite = get_sprite(name)
    if sprite:
        sprite.set_center(x, y)
        return True
    return False

_draw_color = (255, 255, 255)
_draw_alpha = 1.0

def draw_set_color(color):
    """Définit la couleur de dessin."""
    global _draw_color
    _draw_color = color

def draw_set_alpha(alpha):
    """Définit la transparence de dessin."""
    global _draw_alpha
    _draw_alpha = alpha

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
_camera_surfaces: Dict[int, pygame.Surface] = {}
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

    base_path = os.path.dirname(os.path.abspath(__file__))
    assets_path = os.path.join(base_path, assets_folder)
    
    if not os.path.exists(assets_path):
        print(f"Warning: Assets folder '{assets_path}' not found!")
        return
    
    # Charger les images
    images_folder = os.path.join(assets_path, "images")
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
    else:
        print(f"Warning: Assets folder '{images_folder}' not found!")
    
    # Charger les sons
    sounds_folder = os.path.join(assets_path, "sounds")
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
    else:
        print(f"Warning: Assets folder '{sounds_folder}' not found!")
    
    # Charger les polices
    fonts_folder = os.path.join(assets_path, "fonts")
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
    else:
        print(f"Warning: Assets folder '{fonts_folder}' not found!")

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

def _begin_camera_render():
    """Commence le rendu vers la surface de la caméra active."""
    global _current_surface
    if _active_camera != None and _active_camera in _camera_surfaces:
        _current_surface = _camera_surfaces[_active_camera]
        # Effacer la surface de la caméra
        _current_surface.fill((0, 0, 0, 0))  # Transparent par défaut)

def _end_camera_render():
    """Termine le rendu de caméra et affiche le résultat sur l'écran."""
    global _current_surface
    
    if _active_camera != None and _active_camera in _cameras and _active_camera in _camera_surfaces:
        cam = _cameras[_active_camera]
        camera_surface = _camera_surfaces[_active_camera]
        
        # Remettre l'écran comme cible
        _current_surface = None
        
        # Calculer le scaling entre view et port
        view_width = cam['view_width']
        view_height = cam['view_height']
        port_width = cam['port_width']
        port_height = cam['port_height']
        
        # Redimensionner la surface de caméra pour le viewport
        if view_width != port_width or view_height != port_height:
            scaled_surface = pygame.transform.scale(camera_surface, (port_width, port_height))
        else:
            scaled_surface = camera_surface
        
        # Dessiner sur l'écran au bon endroit
        _screen.blit(scaled_surface, (cam['port_x'], cam['port_y']))

def draw_sprite(x: float, y: float, name: str, image_index: int, xscale: float = 1.0, yscale: float = 1.0, angle: float = 0.0):
    """
    Dessine un sprite à la position donnée.
    
    Args:
        x, y: Position de dessin
        name: Nom du sprite
        image_index: Index de l'image à dessiner (pour les sprites multi-images)
        xscale, yscale: Facteurs d'échelle
        angle: Angle de rotation en degrés
    """
    sprite = get_sprite(name)
    if not sprite:
        return
    
    # Calculer la position relative à la caméra
    final_x = x
    final_y = y
    
    if _active_camera != None and _active_camera in _cameras:
        cam = _cameras[_active_camera]
        final_x = x - cam['view_x']
        final_y = y - cam['view_y']
        
        # Culling : ne pas dessiner si hors de la vue de la caméra
        sprite_width = sprite.get_width() * abs(xscale)
        sprite_height = sprite.get_height() * abs(yscale)
        
        if (final_x + sprite_width < 0 or final_x > cam['view_width'] or
            final_y + sprite_height < 0 or final_y > cam['view_height']):
            return  # Hors de vue, ne pas dessiner
    
    # Obtenir l'image à l'index spécifié
    image = sprite.get_image(image_index)
    original_center_x = sprite.center_x
    original_center_y = sprite.center_y
    
    # Appliquer l'échelle
    if xscale != 1.0 or yscale != 1.0:
        new_width = int(image.get_width() * abs(xscale))
        new_height = int(image.get_height() * abs(yscale))
        image = pygame.transform.scale(image, (new_width, new_height))
        
        # Ajuster le centre avec l'échelle
        original_center_x *= abs(xscale)
        original_center_y *= abs(yscale)
        
        # Flip si échelle négative
        if xscale < 0:
            image = pygame.transform.flip(image, True, False)
            original_center_x = image.get_width() - original_center_x
        if yscale < 0:
            image = pygame.transform.flip(image, False, True)
            original_center_y = image.get_height() - original_center_y
    
    # Appliquer la rotation si nécessaire
    if angle != 0:
        # Sauvegarder les dimensions avant rotation
        old_center = (original_center_x, original_center_y)
        
        # Appliquer la rotation
        rotated_image = pygame.transform.rotate(image, angle)
        
        # Calculer le nouveau centre après rotation
        old_rect = image.get_rect(center=(final_x, final_y))
        new_rect = rotated_image.get_rect(center=old_rect.center)
        
        # La position de dessin est maintenant le coin supérieur gauche du nouveau rectangle
        draw_x = new_rect.x
        draw_y = new_rect.y
        
        image = rotated_image
    else:
        # Pas de rotation, utiliser le calcul normal du centre
        draw_x = final_x - original_center_x
        draw_y = final_y - original_center_y
    
    # Dessiner l'image sur la surface appropriée (caméra ou écran)
    target_surface = _current_surface or _screen
    target_surface.blit(image, (draw_x, draw_y))

def draw_text(x: float, y: float, text: str, scale: float = 1, font_name: Optional[str] = None):
    """Dessine du texte en tenant compte de la caméra."""
    # Appliquer la transformation de caméra
    final_x = x
    final_y = y
    
    if _active_camera != None and _active_camera in _cameras:
        cam = _cameras[_active_camera]
        final_x = x - cam['view_x']
        final_y = y - cam['view_y']
    
    font = None
    if font_name:
        font = get_font(font_name)
    
    if font is None:
        font = pygame.font.Font(None, int(24 * scale))
    
    color = _draw_color
    text_surface = font.render(str(text), True, color)
    
    if scale != 1:
        new_width = int(text_surface.get_width() * scale)
        new_height = int(text_surface.get_height() * scale)
        text_surface = pygame.transform.scale(text_surface, (new_width, new_height))
    
    target_surface = _current_surface or _screen
    target_surface.blit(text_surface, (final_x, final_y))

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
    Crée une nouvelle caméra avec sa propre surface de rendu.
    
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
    
    # Créer la surface de rendu pour cette caméra
    _camera_surfaces[camera_id] = pygame.Surface((800, 600), pygame.SRCALPHA)
    
    return camera_id

def camera_set_view_size(camera_id: int, width: int, height: int):
    """
    Définit la taille de la vue de la caméra et recrée sa surface.
    
    Args:
        camera_id: ID de la caméra
        width, height: Dimensions de la vue
    """
    if camera_id in _cameras:
        _cameras[camera_id]['view_width'] = width
        _cameras[camera_id]['view_height'] = height
        # Recréer la surface avec la nouvelle taille
        _camera_surfaces[camera_id] = pygame.Surface((width, height), pygame.SRCALPHA)

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
    if cam_id != None and cam_id in _cameras:
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

def mouse_get_x() -> float:
    """
    Retourne la position X de la souris dans le monde du jeu (tenant compte de la caméra).
    
    Returns:
        Position X de la souris dans le monde
    """
    screen_x = _mouse_x
    
    if _active_camera is not None and _active_camera in _cameras:
        cam = _cameras[_active_camera]
        
        # Convertir de l'écran vers le viewport de caméra
        viewport_x = screen_x - cam['port_x']
        
        # Convertir du viewport vers la vue de caméra (tenir compte du scaling)
        scale_x = cam['view_width'] / cam['port_width']
        camera_x = viewport_x * scale_x
        
        # Convertir de la vue de caméra vers le monde
        world_x = camera_x + cam['view_x']
        
        return world_x
    
    return screen_x

def mouse_get_y() -> float:
    """
    Retourne la position Y de la souris dans le monde du jeu (tenant compte de la caméra).
    
    Returns:
        Position Y de la souris dans le monde
    """
    screen_y = _mouse_y
    
    if _active_camera is not None and _active_camera in _cameras:
        cam = _cameras[_active_camera]
        
        # Convertir de l'écran vers le viewport de caméra
        viewport_y = screen_y - cam['port_y']
        
        # Convertir du viewport vers la vue de caméra (tenir compte du scaling)
        scale_y = cam['view_height'] / cam['port_height']
        camera_y = viewport_y * scale_y
        
        # Convertir de la vue de caméra vers le monde
        world_y = camera_y + cam['view_y']
        
        return world_y
    
    return screen_y

def mouse_get_screen_x() -> int:
    """
    Retourne la position X de la souris sur l'écran (sans transformation caméra).
    
    Returns:
        Position X de la souris sur l'écran
    """
    return _mouse_x

def mouse_get_screen_y() -> int:
    """
    Retourne la position Y de la souris sur l'écran (sans transformation caméra).
    
    Returns:
        Position Y de la souris sur l'écran
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
    Dessine un rectangle en tenant compte de la caméra.
    
    Args:
        x, y: Position du coin supérieur gauche
        width, height: Dimensions
        filled: Si True, rectangle plein, sinon contour
    """
    # Appliquer la transformation de caméra
    final_x = x
    final_y = y
    
    if _active_camera != None and _active_camera in _cameras:
        cam = _cameras[_active_camera]
        final_x = x - cam['view_x']
        final_y = y - cam['view_y']
    
    surface = _current_surface or _screen
    if not surface:
        return
    
    rect = pygame.Rect(int(final_x), int(final_y), int(width), int(height))
    
    if filled:
        pygame.draw.rect(surface, _render_color, rect)
    else:
        pygame.draw.rect(surface, _render_color, rect, 1)

def draw_circle(x: float, y: float, radius: float, filled: bool = True):
    """
    Dessine un cercle en tenant compte de la caméra.
    
    Args:
        x, y: Position du centre
        radius: Rayon
        filled: Si True, cercle plein, sinon contour
    """
    # Appliquer la transformation de caméra
    final_x = x
    final_y = y
    
    if _active_camera != None and _active_camera in _cameras:
        cam = _cameras[_active_camera]
        final_x = x - cam['view_x']
        final_y = y - cam['view_y']
    
    surface = _current_surface or _screen
    if not surface:
        return
    
    if filled:
        pygame.draw.circle(surface, _render_color, (int(final_x), int(final_y)), int(radius))
    else:
        pygame.draw.circle(surface, _render_color, (int(final_x), int(final_y)), int(radius), 1)

def draw_line(x1: float, y1: float, x2: float, y2: float, width: int = 1):
    """
    Dessine une ligne en tenant compte de la caméra.
    
    Args:
        x1, y1: Point de départ
        x2, y2: Point d'arrivée
        width: Épaisseur de la ligne
    """
    # Appliquer la transformation de caméra
    final_x1 = x1
    final_y1 = y1
    final_x2 = x2
    final_y2 = y2
    
    if _active_camera != None and _active_camera in _cameras:
        cam = _cameras[_active_camera]
        final_x1 = x1 - cam['view_x']
        final_y1 = y1 - cam['view_y']
        final_x2 = x2 - cam['view_x']
        final_y2 = y2 - cam['view_y']
    
    surface = _current_surface or _screen
    if not surface:
        return
    
    pygame.draw.line(surface, _render_color, (int(final_x1), int(final_y1)), (int(final_x2), int(final_y2)), width)

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

def sign(x):
    """
    Retourne le signe d'un nombre.
    
    Args:
        x: Nombre à tester
        
    Returns:
        -1, 0, ou 1
    """
    return math.copysign(1, x)

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

def go_to(scene):
    """Change la scène."""
    _game_instance.init_scene(scene)

def scene_restart():
    """Réinitialise la scène."""
    _game_instance.current_scene.cleanup()
    _game_instance.current_scene.create()

def entity_number(entity_type):
    """Compte le nombre d'entité d'un type."""
    return _game_instance.current_scene.count_entities_of_type(entity_type)

def get_entities(entity_type):
    """Retourne la liste d'entité d'un type."""
    return _game_instance.current_scene.get_entities_of_type(entity_type)

def get_delta_time():
    """Retourne le delta time du frame actuel."""
    return _game_instance.get_delta_time()

def game_stop():
    """Arrête le jeu."""
    _game_instance._stop_game()
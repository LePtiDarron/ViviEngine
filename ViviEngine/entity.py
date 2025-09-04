from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from scene import Scene

class Entity:
    """
    Classe de base pour tous les objets de jeu (équivalent d'un object dans GameMaker).
    """
    
    def __init__(self, x: float = 0, y: float = 0):
        """
        Initialise une nouvelle entité.
        
        Args:
            x: Position X initiale
            y: Position Y initiale
        """
        # Position et transformation
        self.x = x
        self.y = y
        self.xprevious = x
        self.yprevious = y
        
        # Sprite et rendu
        self.sprite_index: Optional[str] = None
        self.sprite_width = 0
        self.sprite_height = 0
        self.image_xscale = 1.0
        self.image_yscale = 1.0
        self.image_angle = 0.0  # En degrés
        self.image_alpha = 1.0
        self.image_blend = (255, 255, 255)  # Couleur de teinte
        
        # Profondeur pour l'ordre de rendu (plus grand = devant)
        self.depth = 0
        
        # États
        self.active = True   # Si false, step() n'est pas appelé
        self.visible = True  # Si false, draw() n'est pas appelé
        
        # Références
        self.scene: Optional['Scene'] = None
        self.id = -1  # Sera assigné par la scène
        
        # Masque de collision (optionnel)
        self.mask_left = 0
        self.mask_right = 0
        self.mask_top = 0
        self.mask_bottom = 0
        
    def create(self):
        """
        Appelé lors de la création de l'entité.
        Override cette méthode pour initialiser votre entité.
        """
        self._update_sprite_dimensions()
        
    def step(self):
        """
        Appelé à chaque frame pour la logique de mise à jour.
        Override cette méthode pour votre logique de jeu.
        """
        # Sauvegarder la position précédente
        self.xprevious = self.x
        self.yprevious = self.y
        
    def draw(self):
        """
        Appelé à chaque frame pour le rendu.
        Override cette méthode pour un rendu personnalisé.
        """
        if self.sprite_index and self.visible:
            from . import utils
            
            # Sauvegarder les paramètres de rendu actuels
            utils.draw_set_alpha(self.image_alpha)
            utils.draw_set_color(self.image_blend)
            
            # Dessiner le sprite
            utils.draw_sprite(self.x, self.y, self.sprite_index, 
                            self.image_xscale, self.image_yscale, self.image_angle)
            
            # Restaurer les paramètres par défaut
            utils.draw_set_alpha(1.0)
            utils.draw_set_color((255, 255, 255))
            
    def cleanup(self):
        """
        Appelé lors de la destruction de l'entité.
        Override cette méthode pour nettoyer les ressources.
        """
        pass
        
    def destroy(self):
        """Marque l'entité pour destruction."""
        if self.scene:
            self.scene.remove_entity(self)
            
    def set_sprite(self, sprite_name: str):
        """
        Change le sprite de l'entité.
        
        Args:
            sprite_name: Nom du sprite à utiliser
        """
        self.sprite_index = sprite_name
        self._update_sprite_dimensions()
        
    def _update_sprite_dimensions(self):
        """Met à jour les dimensions du sprite."""
        if self.sprite_index:
            from . import utils
            sprite = utils.get_sprite(self.sprite_index)
            if sprite:
                self.sprite_width = sprite.get_width()
                self.sprite_height = sprite.get_height()
                
                # Mettre à jour le masque de collision par défaut
                self.mask_left = 0
                self.mask_right = self.sprite_width
                self.mask_top = 0
                self.mask_bottom = self.sprite_height
                
    # Méthodes utilitaires pour les collisions
    def get_bbox_left(self) -> float:
        """Retourne la coordonnée gauche de la boîte de collision."""
        return self.x + self.mask_left * self.image_xscale
        
    def get_bbox_right(self) -> float:
        """Retourne la coordonnée droite de la boîte de collision."""
        return self.x + self.mask_right * self.image_xscale
        
    def get_bbox_top(self) -> float:
        """Retourne la coordonnée supérieure de la boîte de collision."""
        return self.y + self.mask_top * self.image_yscale
        
    def get_bbox_bottom(self) -> float:
        """Retourne la coordonnée inférieure de la boîte de collision."""
        return self.y + self.mask_bottom * self.image_yscale
        
    def point_in_bbox(self, px: float, py: float) -> bool:
        """
        Vérifie si un point est dans la boîte de collision de l'entité.
        
        Args:
            px: Coordonnée X du point
            py: Coordonnée Y du point
            
        Returns:
            True si le point est dans la boîte de collision
        """
        return (self.get_bbox_left() <= px <= self.get_bbox_right() and
                self.get_bbox_top() <= py <= self.get_bbox_bottom())
                
    def bbox_collision(self, other: 'Entity') -> bool:
        """
        Vérifie la collision entre les boîtes de collision de deux entités.
        
        Args:
            other: L'autre entité à tester
            
        Returns:
            True s'il y a collision
        """
        return not (self.get_bbox_right() < other.get_bbox_left() or
                   self.get_bbox_left() > other.get_bbox_right() or
                   self.get_bbox_bottom() < other.get_bbox_top() or
                   self.get_bbox_top() > other.get_bbox_bottom())
                   
    def distance_to(self, other: 'Entity') -> float:
        """
        Calcule la distance euclidienne vers une autre entité.
        
        Args:
            other: L'autre entité
            
        Returns:
            Distance en pixels
        """
        import math
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt(dx * dx + dy * dy)
        
    def direction_to(self, other: 'Entity') -> float:
        """
        Calcule l'angle (en degrés) vers une autre entité.
        
        Args:
            other: L'autre entité
            
        Returns:
            Angle en degrés (0-360)
        """
        import math
        dx = other.x - self.x
        dy = other.y - self.y
        angle_rad = math.atan2(-dy, dx)  # -dy car l'axe Y est inversé à l'écran
        angle_deg = math.degrees(angle_rad)
        return (angle_deg + 360) % 360  # Normaliser entre 0 et 360
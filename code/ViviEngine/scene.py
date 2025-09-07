from typing import List, Optional, TYPE_CHECKING
from .entity import Entity

if TYPE_CHECKING:
    from .game import Game

class Scene:
    """
    Représente une scène de jeu (équivalent d'une room dans GameMaker).
    Contient et gère une liste d'entités.
    """
    
    def __init__(self):
        """Initialise une nouvelle scène."""
        self.entities: List[Entity] = []
        self.game: Optional['Game'] = None
        self._entities_to_add: List[Entity] = []
        self._entities_to_remove: List[Entity] = []
        self._next_entity_id = 0
        
        # Variables de la scène
        self.background_color = (64, 128, 255)  # Couleur de fond par défaut
        
    def create(self):
        """
        Appelé lors de l'initialisation de la scène.
        Override cette méthode pour initialiser votre scène.
        """
        pass
        
    def step(self):
        """
        Appelé à chaque frame pour la logique de mise à jour.
        """
        # Ajouter les nouvelles entités
        self._process_entity_additions()
        
        # Mettre à jour toutes les entités
        for entity in self.entities:
            if entity.active:
                entity.step()
                
        # Supprimer les entités marquées pour suppression
        self._process_entity_removals()
        
    def draw(self):
        """
        Appelé à chaque frame pour le rendu avec support caméra.
        """
        from . import utils
        
        # Commencer le rendu de caméra
        utils._begin_camera_render()
        
        # Effacer la surface de caméra avec la couleur de fond
        utils.draw_clear(self.background_color)
        
        # Trier les entités par profondeur (depth) pour l'ordre de rendu
        sorted_entities = sorted([e for e in self.entities if e.visible], 
                               key=lambda x: x.depth, reverse=True)
        
        # Dessiner toutes les entités visibles
        for entity in sorted_entities:
            entity.draw()
        
        # Terminer le rendu de caméra et l'afficher à l'écran
        utils._end_camera_render()
            
    def cleanup(self):
        """
        Appelé lors de la fermeture de la scène.
        Override cette méthode pour nettoyer les ressources.
        """
        # Nettoyer toutes les entités
        for entity in self.entities:
            entity.cleanup()
        self.entities.clear()
        self._entities_to_add.clear()
        self._entities_to_remove.clear()
        
    def add_entity(self, entity: Entity):
        """
        Ajoute une entité à la scène.
        
        Args:
            entity: L'entité à ajouter
        """
        entity.scene = self
        entity.id = self._get_next_entity_id()
        self._entities_to_add.append(entity)
        
    def remove_entity(self, entity: Entity):
        """
        Marque une entité pour suppression de la scène.
        
        Args:
            entity: L'entité à supprimer
        """
        if entity in self.entities and entity not in self._entities_to_remove:
            self._entities_to_remove.append(entity)
            
    def get_entity_by_id(self, entity_id: int) -> Optional[Entity]:
        """
        Trouve une entité par son ID.
        
        Args:
            entity_id: ID de l'entité recherchée
            
        Returns:
            L'entité trouvée ou None
        """
        for entity in self.entities:
            if entity.id == entity_id:
                return entity
        return None
        
    def get_entities_of_type(self, entity_type) -> List[Entity]:
        """
        Retourne toutes les entités d'un type donné.
        
        Args:
            entity_type: Type/classe d'entité recherché
            
        Returns:
            Liste des entités du type spécifié
        """
        return [entity for entity in self.entities if isinstance(entity, entity_type)]
        
    def count_entities_of_type(self, entity_type) -> int:
        """
        Compte le nombre d'entités d'un type donné.
        
        Args:
            entity_type: Type/classe d'entité à compter
            
        Returns:
            Nombre d'entités du type spécifié
        """
        return len(self.get_entities_of_type(entity_type))
        
    def _get_next_entity_id(self) -> int:
        """Génère un ID unique pour une nouvelle entité."""
        entity_id = self._next_entity_id
        self._next_entity_id += 1
        return entity_id
        
    def _process_entity_additions(self):
        """Traite les entités en attente d'ajout."""
        for entity in self._entities_to_add:
            self.entities.append(entity)
            entity.create()  # Appeler create() après l'ajout à la scène
        self._entities_to_add.clear()
        
    def _process_entity_removals(self):
        """Traite les entités en attente de suppression."""
        for entity in self._entities_to_remove:
            if entity in self.entities:
                entity.cleanup()
                self.entities.remove(entity)
        self._entities_to_remove.clear()
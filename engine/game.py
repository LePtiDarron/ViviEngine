import pygame
import sys
from typing import Dict, Optional
from .scene import Scene

class Game:
    """
    Classe principale du moteur de jeu.
    Gère les scènes, la boucle de jeu principale et l'initialisation de pygame.
    """
    
    def __init__(self, width: int = 800, height: int = 600, title: str = "Game Engine", fps: int = 60):
        """
        Initialise le moteur de jeu.
        
        Args:
            width: Largeur de la fenêtre
            height: Hauteur de la fenêtre  
            title: Titre de la fenêtre
            fps: FPS cible du jeu
        """
        self.width = width
        self.height = height
        self.title = title
        self.fps = fps
        
        # État du jeu
        self.running = False
        self.clock = None
        self.screen = None
        
        # Gestion des scènes
        self.scenes: Dict[str, Scene] = {}
        self.current_scene: Optional[Scene] = None
        self.next_scene: Optional[str] = None
        
        # Variables globales accessibles
        self._delta_time = 0
        
    def initialize(self):
        """Initialise pygame et crée la fenêtre de jeu."""
        pygame.init()
        pygame.mixer.init()
        
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        
        # Initialise les variables globales du moteur
        from . import utils
        utils._game_instance = self
        utils._screen = self.screen
        utils._clock = self.clock
        
        self.running = True
        
    def add_scene(self, name: str, scene: Scene):
        """
        Ajoute une scène au jeu.
        
        Args:
            name: Nom de la scène
            scene: Instance de la scène
        """
        scene.game = self
        self.scenes[name] = scene
        
    def switch_scene(self, scene_name: str):
        """
        Planifie le changement vers une nouvelle scène.
        Le changement s'effectuera à la fin du frame actuel.
        
        Args:
            scene_name: Nom de la scène vers laquelle switcher
        """
        if scene_name in self.scenes:
            self.next_scene = scene_name
        else:
            print(f"Warning: Scene '{scene_name}' not found!")
            
    def init_scene(self, scene_name: str):
        """
        Initialise et active directement une scène.
        
        Args:
            scene_name: Nom de la scène à initialiser
        """
        if scene_name in self.scenes:
            if self.current_scene:
                self.current_scene.cleanup()
                
            self.current_scene = self.scenes[scene_name]
            self.current_scene.create()
            self.next_scene = None
        else:
            print(f"Error: Cannot init scene '{scene_name}' - scene not found!")
    
    def _handle_scene_switch(self):
        """Gère le changement de scène si nécessaire."""
        if self.next_scene:
            self.init_scene(self.next_scene)
    
    def run(self):
        """Lance la boucle de jeu principale."""
        if not self.running:
            self.initialize()
            
        while self.running:
            # Calcul du delta time
            dt = self.clock.tick(self.fps)
            self._delta_time = dt / 1000.0  # Convertir en secondes
            
            # Gestion des événements pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
                # Mise à jour des états clavier/souris
                from . import utils
                utils._handle_pygame_event(event)
            
            # Mise à jour de la scène actuelle
            if self.current_scene:
                self.current_scene.step()
                
            # Rendu de la scène actuelle
            if self.current_scene:
                self.current_scene.draw()
                
            # Gestion du changement de scène
            self._handle_scene_switch()
            
            # Affichage
            pygame.display.flip()
            
            # Nettoyage de fin de frame
            from . import utils
            utils._end_frame_cleanup()
            
        self.quit()
        
    def quit(self):
        """Ferme proprement le jeu."""
        if self.current_scene:
            self.current_scene.cleanup()
        pygame.quit()
        sys.exit()
        
    def get_delta_time(self) -> float:
        """Retourne le delta time du frame actuel."""
        return self._delta_time

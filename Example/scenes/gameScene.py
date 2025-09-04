from engine import *
from entities.enemy import Enemy
from entities.player import Player
from entities.bullet import Bullet

class GameScene(Scene):
    def __init__(self):
        super().__init__()
        self.background_color = (20, 30, 40)
        self.enemy_spawn_timer = 0
        self.enemy_spawn_delay = 2.0
        
    def create(self):
        super().create()
        w, h = window_get_size()
        player = Player(w // 2, h // 2)
        self.add_entity(player)
        for i in range(3):
            enemy_x = random_range(50, w - 50)
            enemy_y = random_range(50, h - 50)
            if distance(enemy_x, enemy_y, w // 2, h // 2) < 100:
                enemy_x = 50 if enemy_x < w // 2 else w - 50
            
            enemy = Enemy(enemy_x, enemy_y)
            self.add_entity(enemy)
            
    def step(self):
        super().step()
        if hasattr(self.game, '_delta_time'):
            dt = self.game.get_delta_time()
            self.enemy_spawn_timer += dt
        else:
            self.enemy_spawn_timer += 1/60
            
        if self.enemy_spawn_timer >= self.enemy_spawn_delay:
            self.enemy_spawn_timer = 0
            self._spawn_enemy()
        if keyboard_check_pressed(pygame.K_SPACE):
            self._player_shoot()
        if keyboard_check_pressed(pygame.K_r):
            self.game.switch_scene("game")
            
    def draw(self):
        super().draw()
        draw_set_color((255, 255, 255))
        draw_text(10, 10, "Flèches/WASD: Déplacer", 1)
        draw_text(10, 35, "Espace: Tirer", 1)
        draw_text(10, 60, "R: Redémarrer", 1)
        enemy_count = self.count_entities_of_type(Enemy)
        draw_text(10, 100, f"Ennemis: {enemy_count}", 1)
        
    def _spawn_enemy(self):
        w, h = window_get_size()
        side = random_int(0, 3)
        if side == 0:
            x, y = random_range(0, w), -20
        elif side == 1:
            x, y = w + 20, random_range(0, h)
        elif side == 2:
            x, y = random_range(0, w), h + 20
        else:
            x, y = -20, random_range(0, h)
            
        enemy = Enemy(x, y)
        self.add_entity(enemy)
        
    def _player_shoot(self):
        players = self.get_entities_of_type(Player)
        if players:
            player = players[0]
            mouse_x, mouse_y = mouse_get_x(), mouse_get_y()
            direction = point_direction(player.x, player.y, mouse_x, mouse_y)
            
            bullet = Bullet(player.x, player.y, direction)
            self.add_entity(bullet)
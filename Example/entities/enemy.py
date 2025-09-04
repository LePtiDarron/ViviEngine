from engine import *
from entities.player import Player

class Enemy(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = 80
        self.sprite_index = "enemy"
        self.player = None
        
    def create(self):
        super().create()
        if not get_sprite(self.sprite_index):
            self.sprite_width = 24
            self.sprite_height = 24
            self.mask_right = self.sprite_width
            self.mask_bottom = self.sprite_height
            
        if self.scene:
            players = self.scene.get_entities_of_type(Player)
            if players:
                self.player = players[0]
        
    def step(self):
        super().step()
        
        if self.player:
            dist = self.distance_to(self.player)
            if dist > 5:
                direction = self.direction_to(self.player)
                if hasattr(self.scene.game, '_delta_time'):
                    dt = self.scene.game.get_delta_time()
                    self.x += lengthdir_x(self.speed * dt, direction)
                    self.y += lengthdir_y(self.speed * dt, direction)
                else:
                    self.x += lengthdir_x(self.speed / 60, direction)
                    self.y += lengthdir_y(self.speed / 60, direction)
        
    def draw(self):
        if not get_sprite(self.sprite_index):
            draw_set_color((255, 50, 50))
            draw_rectangle(self.x - self.sprite_width//2, self.y - self.sprite_height//2, self.sprite_width, self.sprite_height, True)
        else:
            super().draw()
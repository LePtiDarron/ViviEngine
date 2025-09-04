from engine import *
from entities.enemy import Enemy

class Bullet(Entity):
    def __init__(self, x, y, direction, speed=300):
        super().__init__(x, y)
        self.direction = direction
        self.speed = speed
        self.sprite_index = "bullet"
        
    def create(self):
        super().create()
        if not get_sprite(self.sprite_index):
            self.sprite_width = 8
            self.sprite_height = 8
            self.mask_right = self.sprite_width
            self.mask_bottom = self.sprite_height
            
    def step(self):
        super().step()
        if hasattr(self.scene.game, '_delta_time'):
            dt = self.scene.game.get_delta_time()
            self.x += lengthdir_x(self.speed * dt, self.direction)
            self.y += lengthdir_y(self.speed * dt, self.direction)
        else:
            self.x += lengthdir_x(self.speed / 60, self.direction)
            self.y += lengthdir_y(self.speed / 60, self.direction)
        w, h = window_get_size()
        if self.x < -50 or self.x > w + 50 or self.y < -50 or self.y > h + 50:
            self.destroy()
        if self.scene:
            enemies = self.scene.get_entities_of_type(Enemy)
            for enemy in enemies:
                if self.bbox_collision(enemy):
                    enemy.destroy()
                    self.destroy()
                    break

    def draw(self):
        if not get_sprite(self.sprite_index):
            draw_set_color((255, 255, 0))
            draw_circle(self.x, self.y, 4, True)
        else:
            super().draw()
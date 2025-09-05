from ViviEngine import *
from entities.enemy import Enemy

class Bullet(Entity):
    def create(self):
        super().create()
        self.speed = 300
        self.set_sprite("bullet")
            
    def step(self):
        super().step()
        if hasattr(self.scene.game, '_delta_time'):
            dt = get_delta_time()
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
        super().draw()
from ViviEngine import *
from entities.player import Player

class Enemy(Entity):
    def create(self):
        super().create()
        self.speed = 80
        self.set_sprite("enemy")
        self.player = None
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
                    dt = get_delta_time()
                    self.x += lengthdir_x(self.speed * dt, direction)
                    self.y += lengthdir_y(self.speed * dt, direction)
                else:
                    self.x += lengthdir_x(self.speed / 60, direction)
                    self.y += lengthdir_y(self.speed / 60, direction)
        
    def draw(self):
        super().draw()
    
    def destroy(self):
        play_sound("explosion")
        super().destroy()
from ViviEngine import *

class Player(Entity):
    def step(self):
        super().step()
        if keyboard_check(KEY_S):
            self.y += self.speed * get_delta_time()
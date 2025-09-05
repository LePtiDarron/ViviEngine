from ViviEngine import *

class Player(Entity):
    def create(self):
        super().create()
        self.speed = 200
        self.set_sprite("player")

    def step(self):
        super().step()
        dx = 0
        dy = 0
        
        if keyboard_check(KEY_LEFT) or keyboard_check(KEY_Q):
            dx = -1
        if keyboard_check(KEY_RIGHT) or keyboard_check(KEY_D):
            dx = 1
        if keyboard_check(KEY_UP) or keyboard_check(KEY_Z):
            dy = -1
        if keyboard_check(KEY_DOWN) or keyboard_check(KEY_S):
            dy = 1
            
        if dx != 0 and dy != 0:
            dx *= 0.707
            dy *= 0.707
            
        if hasattr(self.scene.game, '_delta_time'):
            dt = get_delta_time()
            self.x += dx * self.speed * dt
            self.y += dy * self.speed * dt
        else:
            self.x += dx * self.speed / 60
            self.y += dy * self.speed / 60
            
        w, h = window_get_size()
        self.x = clamp(self.x, self.sprite_width//2, w - self.sprite_width//2)
        self.y = clamp(self.y, self.sprite_height//2, h - self.sprite_height//2)
        
    def draw(self):
        super().draw()
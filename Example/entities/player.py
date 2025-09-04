from ViviEngine import *

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = 200
        self.sprite_index = "player"
        
    def create(self):
        super().create()
        if not get_sprite(self.sprite_index):
            self.sprite_width = 32
            self.sprite_height = 32
            self.mask_right = self.sprite_width
            self.mask_bottom = self.sprite_height

    def step(self):
        super().step()
        dx = 0
        dy = 0
        
        if keyboard_check(pygame.K_LEFT) or keyboard_check(pygame.K_a):
            dx = -1
        if keyboard_check(pygame.K_RIGHT) or keyboard_check(pygame.K_d):
            dx = 1
        if keyboard_check(pygame.K_UP) or keyboard_check(pygame.K_w):
            dy = -1
        if keyboard_check(pygame.K_DOWN) or keyboard_check(pygame.K_s):
            dy = 1
            
        if dx != 0 and dy != 0:
            dx *= 0.707
            dy *= 0.707
            
        if hasattr(self.scene.game, '_delta_time'):
            dt = self.scene.game.get_delta_time()
            self.x += dx * self.speed * dt
            self.y += dy * self.speed * dt
        else:
            self.x += dx * self.speed / 60
            self.y += dy * self.speed / 60
            
        w, h = window_get_size()
        self.x = clamp(self.x, self.sprite_width//2, w - self.sprite_width//2)
        self.y = clamp(self.y, self.sprite_height//2, h - self.sprite_height//2)
        
    def draw(self):
        if not get_sprite(self.sprite_index):
            draw_set_color((0, 100, 255))
            draw_rectangle(self.x - self.sprite_width//2, self.y - self.sprite_height//2, self.sprite_width, self.sprite_height, True)
        else:
            super().draw()
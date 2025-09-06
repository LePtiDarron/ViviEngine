from ViviEngine import *

class Object(Entity):
    def draw(self):
        draw_sprite(self.x, self.y, self.sprite_index, self.image_xscale, self.image_yscale, self.image_angle)
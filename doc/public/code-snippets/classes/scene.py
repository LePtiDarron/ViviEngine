from ViviEngine import *

class ColorfullScene(Scene):
    def create(self):
        super().create()
        self.red = 0
        self.green = 100
        self.blue = 200
        self.r = 5
        self.g = 5
        self.b = 5
        self.background_color = (self.red, self.green, self.blue)
            
    def step(self):
        super().step()
        self.red += self.r
        if (self.red >= 255):
            self.red = 255
            self.r *= -1
        self.green += self.g
        if (self.green >= 255):
            self.green = 255
            self.g *= -1
        self.blue += self.g
        if (self.blue >= 255):
            self.blue = 255
            self.g *= -1
        self.background_color = (self.red, self.green, self.blue)
            
    def draw(self):
        super().draw()

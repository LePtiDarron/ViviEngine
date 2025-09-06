from ViviEngine import *

# Define a simple scene
class MenuScene(Scene):
    def create(self):
        self.background_color = (random_int(0, 255), random_int(0, 255), random_int(0, 255))
    
    def step(self):
        super().step()
        if keyboard_check_pressed(KEY_SPACE):
            self.background_color = (random_int(0, 255), random_int(0, 255), random_int(0, 255))
    
    def draw(self):
        super().draw()
        draw_text(400, 300, "Press SPACE to interact!", scale=2, "font.ttf")

# Setup and run
game = Game(800, 600, "My First Game", 60)
menu = MenuScene()
game.add_scene("menu", menu)
game.init_scene("menu")
game.run()

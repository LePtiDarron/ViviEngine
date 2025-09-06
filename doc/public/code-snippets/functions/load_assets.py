from ViviEngine import *
import os

game = Game(800, 600, "ViviEngine Example", 60)
game.initialize()
assets_path = os.path.join(os.path.dirname(__file__), "assets")
load_assets(assets_path)
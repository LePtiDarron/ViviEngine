from ViviEngine import *
from scenes.gameScene import GameScene

def main():
    game = Game(800, 600, "ViviEngine Example", 60)
    game.initialize()
    assets_path = os.path.join(os.path.dirname(__file__), "assets")
    load_assets(assets_path)
    game_scene = GameScene()
    game.add_scene("game", game_scene)
    game.init_scene("game")
    game.run()

if __name__ == "__main__":
    main()
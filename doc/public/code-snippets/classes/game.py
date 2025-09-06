from ViviEngine import *
from scenes.myScene import MyScene

def main():
    game = Game(800, 600, "ViviEngine Example", 60)
    game.initialize()

    assets_path = os.path.join(os.path.dirname(__file__), "assets")
    load_assets(assets_path)

    game.add_scene("game", MyScene())
    go_to("game")

    game.run()


if __name__ == "__main__":
    main()
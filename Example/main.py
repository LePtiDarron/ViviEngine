from ViviEngine import *

def main():
    game = Game(800, 600, "My First Game", 60)
    game.initialize()
    assets_path = os.path.join(os.path.dirname(__file__), "assets")
    load_assets(assets_path)
    game.run()

if __name__ == "__main__":
    main()
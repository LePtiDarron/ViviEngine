# ViviEngine : Python 2D Game Engine

Un moteur de jeu 2D simple inspiré de GameMaker Studio, construit avec pygame.

## Installation

Assurez-vous d'avoir Python 3.7+ et pygame installé :

```bash
pip install pygame
pip install -e .
```

## Structure du projet

```
.
├── ViviEngine/
│   ├── __init__.py
│   ├── entity.py
│   ├── game.py
│   ├── scene.py
│   └── utils.py
├── Example/
│   ├── assets/
│   │   ├── fonts/
│   │   ├── images/
│   │   └── sounds/
│   ├── entities/
│   │   ├── bullet.py
│   │   ├── enemy.py
│   │   └── player.py
│   ├── scenes/
│   │   └── gameScene.py
│   └── main.py
├── setup.py
└── README.md
```

## Licence

Ce moteur est fourni tel quel pour des fins éducatives et de prototypage. Utilisez pygame selon sa propre licence.

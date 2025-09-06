const classes = [
  {
    name: 'Game',
    description: 'The main engine class that manages the game loop, window, and scene transitions.',
    properties: [
      {
        category: 'Key methods',
        items: [
          {
            name: 'initialize()',
            description: 'Initialize the game'
          },
          {
            name: 'add_scene(name, scene)',
            description: 'Register a scene with a name'
          },
          {
            name: 'run()',
            description: 'Start the main game loop'
          }
        ]
      }
    ],
    example: "code-snippets/classes/game.py"
  },
  {
    name: 'Scene',
    description: 'Represents a game screen or level. Manages entities and handles game logic.',
    properties: [
      {
        category: 'Override Methods',
        items: [
          {
            name: 'create()',
            description: 'Called when scene is initialized'
          },
          {
            name: 'step()',
            description: 'Called every frame for logic updates'
          }
        ]
      }
    ],
    example: "code-snippets/classes/scene.py"
  },
  {
    name: 'Entity',
    description: 'Base class for all game objects. Provides position, sprites, collision detection, and lifecycle management.',
    properties: [
      {
        category: 'Override Methods',
        items: [
          {
            name: 'create()',
            description: 'Override for initialization'
          },
          {
            name: 'step()',
            description: 'Override for per-frame logic'
          },
          {
            name: 'draw()',
            description: 'Override for custom rendering'
          },
          {
            name: 'destroy()',
            description: 'Mark for destruction'
          },
          {
            name: 'set_sprite(name)',
            description: 'Change sprite'
          }
        ]
      },
      {
        category: 'Collision Detection',
        items: [
          {
            name: 'bbox_collision(other)',
            description: 'Check collision with another entity'
          },
          {
            name: 'point_in_bbox(x, y)',
            description: 'Check if point is inside entity'
          },
          {
            name: 'distance_to(other)',
            description: 'Calculate distance to another entity'
          },
          {
            name: 'direction_to(other)',
            description: 'Calculate angle to another entity'
          }
        ]
      },
      {
        category: 'Properties',
        items: [
          {
            name: 'x, y',
            description: 'Current position'
          },
          {
            name: 'xprevious, yprevious',
            description: 'Previous frame position'
          },
          {
            name: 'image_xscale, image_yscale',
            description: 'Sprite scaling (1.0 = normal)'
          },
          {
            name: 'image_angle',
            description: 'Rotation in degrees'
          },
          {
            name: 'image_alpha',
            description: 'Transparency (0.0 to 1.0)'
          },
          {
            name: 'sprite_index',
            description: 'Name of sprite to display'
          },
          {
            name: 'depth',
            description: 'Render depth (higher = in front)'
          },
          {
            name: 'visible',
            description: 'Whether entity is drawn'
          },
          {
            name: 'active',
            description: 'Whether step() is called'
          },
          {
            name: 'id',
            description: 'Unique identifier'
          }
        ]
      }
    ],
    example: "code-snippets/classes/entity.py"
  }
];

export { classes }
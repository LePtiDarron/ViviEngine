const classes = [
  {
    name: 'Game',
    description: 'The main engine class that manages the game loop, window, and scene transitions.',
    properties: [
      {
        category: 'Constructor',
        items: [
          {
            name: '__init__(width, height, title, fps)',
            description: 'Create a new game instance with window dimensions, title and target FPS'
          }
        ]
      },
      {
        category: 'Core Methods',
        items: [
          {
            name: 'initialize()',
            description: 'Initialize pygame, create window and setup game systems'
          },
          {
            name: 'add_scene(name, scene)',
            description: 'Register a scene with a unique name for later activation'
          },
          {
            name: 'init_scene(scene_name)',
            description: 'Switch to and initialize the specified scene'
          },
          {
            name: 'run()',
            description: 'Start the main game loop with event handling and rendering'
          },
          {
            name: 'get_delta_time()',
            description: 'Return the time in seconds elapsed since the last frame'
          },
          {
            name: '_stop_game()',
            description: 'Stop the game loop and prepare for shutdown'
          }
        ]
      },
      {
        category: 'Entity Management',
        items: [
          {
            name: 'count_entities_of_type(entity_type)',
            description: 'Count the number of entities of a specific type in current scene'
          }
        ]
      },
      {
        category: 'Properties',
        items: [
          {
            name: 'width, height',
            description: 'Window dimensions in pixels'
          },
          {
            name: 'title',
            description: 'Window title text'
          },
          {
            name: 'fps',
            description: 'Target frames per second'
          },
          {
            name: 'current_scene',
            description: 'Reference to the currently active scene'
          },
          {
            name: 'scenes',
            description: 'Dictionary of registered scenes by name'
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
        category: 'Constructor',
        items: [
          {
            name: '__init__()',
            description: 'Initialize a new scene with empty entity list and default settings'
          }
        ]
      },
      {
        category: 'Override Methods',
        items: [
          {
            name: 'create()',
            description: 'Called when scene is initialized - override for custom setup'
          },
          {
            name: 'step()',
            description: 'Called every frame for logic updates - processes entity additions/removals and updates'
          },
          {
            name: 'draw()',
            description: 'Called every frame for rendering - clears screen and draws all visible entities'
          },
          {
            name: 'cleanup()',
            description: 'Called when scene is destroyed - override for custom cleanup'
          }
        ]
      },
      {
        category: 'Entity Management',
        items: [
          {
            name: 'add_entity(entity)',
            description: 'Add an entity to the scene (will be processed next frame)'
          },
          {
            name: 'remove_entity(entity)',
            description: 'Mark an entity for removal from the scene'
          },
          {
            name: 'get_entity_by_id(entity_id)',
            description: 'Find and return an entity by its unique ID, or None if not found'
          },
          {
            name: 'get_entities_of_type(entity_type)',
            description: 'Return a list of all entities of the specified type/class'
          },
          {
            name: 'count_entities_of_type(entity_type)',
            description: 'Count the number of entities of the specified type/class'
          },
          {
            name: '_get_next_entity_id()',
            description: 'Generate a unique ID for a new entity (internal method)'
          },
          {
            name: '_process_entity_additions()',
            description: 'Process entities pending addition (internal method)'
          },
          {
            name: '_process_entity_removals()',
            description: 'Process entities pending removal (internal method)'
          }
        ]
      },
      {
        category: 'Properties',
        items: [
          {
            name: 'entities',
            description: 'List of all active entities in the scene'
          },
          {
            name: 'game',
            description: 'Reference to the parent game instance'
          },
          {
            name: 'background_color',
            description: 'RGB tuple for scene background color (default: light blue)'
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
        category: 'Constructor',
        items: [
          {
            name: '__init__(x=0, y=0)',
            description: 'Create entity at specified position with default properties'
          }
        ]
      },
      {
        category: 'Override Methods',
        items: [
          {
            name: 'create()',
            description: 'Called when entity is added to scene - override for initialization'
          },
          {
            name: 'step()',
            description: 'Called every frame for logic updates - saves previous position by default'
          },
          {
            name: 'draw()',
            description: 'Called every frame for rendering - draws sprite if set'
          },
          {
            name: 'cleanup()',
            description: 'Called when entity is destroyed - override for resource cleanup'
          },
          {
            name: 'destroy()',
            description: 'Mark entity for destruction (will be removed next frame)'
          }
        ]
      },
      {
        category: 'Sprite Methods',
        items: [
          {
            name: 'set_sprite(name)',
            description: 'Change the current sprite and update dimensions'
          },
          {
            name: '_update_sprite_dimensions()',
            description: 'Update sprite_width and sprite_height from current sprite'
          }
        ]
      },
      {
        category: 'Collision Detection',
        items: [
          {
            name: 'bbox_collision(x, y, entity_type)',
            description: 'Check collision between this entity at given position and entities of specified type'
          },
          {
            name: 'point_in_bbox(x, y)',
            description: 'Check if a point is inside this entity\'s bounding box'
          },
          {
            name: 'get_bbox_left()',
            description: 'Return the left coordinate of the collision box'
          },
          {
            name: 'get_bbox_right()',
            description: 'Return the right coordinate of the collision box'
          },
          {
            name: 'get_bbox_top()',
            description: 'Return the top coordinate of the collision box'
          },
          {
            name: 'get_bbox_bottom()',
            description: 'Return the bottom coordinate of the collision box'
          },
          {
            name: 'distance_to(other)',
            description: 'Calculate Euclidean distance to another entity'
          },
          {
            name: 'direction_to(other)',
            description: 'Calculate angle in degrees from this entity to another'
          }
        ]
      },
      {
        category: 'Position Properties',
        items: [
          {
            name: 'x, y',
            description: 'Current position coordinates'
          },
          {
            name: 'xprevious, yprevious',
            description: 'Position from the previous frame'
          }
        ]
      },
      {
        category: 'Sprite Properties',
        items: [
          {
            name: 'sprite_index',
            description: 'Name of the current sprite to display'
          },
          {
            name: 'sprite_width, sprite_height',
            description: 'Dimensions of a single image in the sprite'
          },
          {
            name: 'image_xscale, image_yscale',
            description: 'Sprite scaling factors (1.0 = normal size)'
          },
          {
            name: 'image_angle',
            description: 'Rotation angle in degrees'
          },
          {
            name: 'image_alpha',
            description: 'Transparency level (0.0 = invisible, 1.0 = opaque)'
          },
          {
            name: 'image_blend',
            description: 'RGB color tuple for sprite tinting (255,255,255 = normal)'
          }
        ]
      },
      {
        category: 'Animation Properties',
        items: [
          {
            name: 'image_index',
            description: 'Current image index in sprite sheet (float for smooth animation)'
          },
          {
            name: 'image_speed',
            description: 'Animation speed in images per frame (0 = stopped)'
          },
          {
            name: 'image_number',
            description: 'Total number of images in the current sprite (auto-detected)'
          }
        ]
      },
      {
        category: 'Animation Methods',
        items: [
          {
            name: 'animation_set(sprite_name, speed, start_index)',
            description: 'Configure a new animation with sprite, speed and starting frame'
          },
          {
            name: 'animation_stop()',
            description: 'Stop the current animation'
          },
          {
            name: 'animation_pause()',
            description: 'Pause the current animation (alias for animation_stop)'
          },
          {
            name: 'animation_resume(speed)',
            description: 'Resume animation with specified speed'
          },
          {
            name: 'animation_end()',
            description: 'Check if animation has reached the last frame'
          }
        ]
      },
      {
        category: 'Collision Mask Properties',
        items: [
          {
            name: 'mask_sprite',
            description: 'Sprite used for collision detection (None = uses sprite_index)'
          },
          {
            name: 'mask_left, mask_right',
            description: 'Horizontal collision mask offsets relative to mask sprite center'
          },
          {
            name: 'mask_top, mask_bottom',
            description: 'Vertical collision mask offsets relative to mask sprite center'
          }
        ]
      },
      {
        category: 'Collision Mask Methods',
        items: [
          {
            name: 'set_mask_sprite(mask_sprite_name)',
            description: 'Set the sprite used for collision detection (None for default)'
          }
        ]
      },
      {
        category: 'State Properties',
        items: [
          {
            name: 'depth',
            description: 'Render depth (higher values drawn in front)'
          },
          {
            name: 'visible',
            description: 'Whether entity is rendered (true/false)'
          },
          {
            name: 'active',
            description: 'Whether step() method is called (true/false)'
          },
          {
            name: 'id',
            description: 'Unique identifier assigned by scene'
          },
          {
            name: 'scene',
            description: 'Reference to the scene containing this entity'
          }
        ]
      }
    ],
    example: "code-snippets/classes/entity.py"
  }
];

export { classes }
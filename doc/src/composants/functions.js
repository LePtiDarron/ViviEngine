const functions = [
  // Asset Management
  {
    name: 'load_sprite',
    category: 'Asset Management',
    prototype: 'load_sprite(filepath, name=None)',
    description: 'Load a sprite from file. Auto-detects sprite sheets with "_strip{n}" naming'
  },
  {
    name: 'load_sound',
    category: 'Asset Management',
    prototype: 'load_sound(filepath, name=None)',
    description: 'Load a sound effect from file (.wav, .ogg, .mp3)'
  },
  {
    name: 'load_font',
    category: 'Asset Management',
    prototype: 'load_font(filepath, size=24, name=None)',
    description: 'Load a font from file (.ttf, .otf) with specified size'
  },
  {
    name: 'sprite_set_center',
    category: 'Asset Management',
    prototype: 'sprite_set_center(name, x, y)',
    description: 'Set sprite center point (0.0-1.0 relative coordinates)'
  },
  {
    name: 'load_assets',
    category: 'Asset Management',
    prototype: 'load_assets(assets_folder="assets")',
    description: 'Legacy function: Load all sprites, sounds, and fonts from folder (use individual load functions instead)'
  },

  // Drawing Functions
  {
    name: 'draw_clear',
    category: 'Drawing Functions',
    prototype: 'draw_clear(color)',
    description: 'Clear the screen with the specified RGB color tuple'
  },
  {
    name: 'draw_sprite',
    category: 'Drawing Functions',
    prototype: 'draw_sprite(x, y, name, image_index, xscale=1.0, yscale=1.0, angle=0.0)',
    description: 'Draw a sprite at position with transformations and specific frame'
  },
  {
    name: 'draw_text',
    category: 'Drawing Functions',
    prototype: 'draw_text(x, y, text, scale=1, font_name=None)',
    description: 'Draw text string with optional custom font'
  },
  {
    name: 'draw_rectangle',
    category: 'Drawing Functions',
    prototype: 'draw_rectangle(x, y, width, height, filled=True)',
    description: 'Draw a rectangle (filled or outline)'
  },
  {
    name: 'draw_circle',
    category: 'Drawing Functions',
    prototype: 'draw_circle(x, y, radius, filled=True)',
    description: 'Draw a circle (filled or outline)'
  },
  {
    name: 'draw_line',
    category: 'Drawing Functions',
    prototype: 'draw_line(x1, y1, x2, y2, width=1)',
    description: 'Draw a line between two points with specified width'
  },
  {
    name: 'draw_set_color',
    category: 'Drawing Functions',
    prototype: 'draw_set_color(rgb_tuple)',
    description: 'Set the current drawing color for subsequent draw operations'
  },
  {
    name: 'draw_set_alpha',
    category: 'Drawing Functions',
    prototype: 'draw_set_alpha(alpha)',
    description: 'Set drawing transparency (0.0 = invisible, 1.0 = opaque)'
  },

  // Surface Management
  {
    name: 'surface_create',
    category: 'Surface Management',
    prototype: 'surface_create(width, height)',
    description: 'Create a new surface with specified dimensions'
  },
  {
    name: 'surface_set_target',
    category: 'Surface Management',
    prototype: 'surface_set_target(surface)',
    description: 'Set the rendering target surface (None for screen)'
  },
  {
    name: 'surface_reset_target',
    category: 'Surface Management',
    prototype: 'surface_reset_target()',
    description: 'Reset rendering target back to the screen'
  },
  {
    name: 'surface_destroy',
    category: 'Surface Management',
    prototype: 'surface_destroy(surface)',
    description: 'Destroy a surface to free memory'
  },
  {
    name: 'surface_draw',
    category: 'Surface Management',
    prototype: 'surface_draw(x, y, surface, xscale=1, yscale=1)',
    description: 'Draw a surface at position with optional scaling'
  },

  // Input Handling - Keyboard
  {
    name: 'keyboard_check_pressed',
    category: 'Input Handling',
    prototype: 'keyboard_check_pressed(key)',
    description: 'Returns True if the key was just pressed this frame'
  },
  {
    name: 'keyboard_check',
    category: 'Input Handling',
    prototype: 'keyboard_check(key)',
    description: 'Returns True if the key is currently being held down'
  },
  {
    name: 'keyboard_check_released',
    category: 'Input Handling',
    prototype: 'keyboard_check_released(key)',
    description: 'Returns True if the key was just released this frame'
  },

  // Input Handling - Mouse
  {
    name: 'mouse_check_pressed',
    category: 'Input Handling',
    prototype: 'mouse_check_pressed(button)',
    description: 'Returns True if mouse button was just pressed (1=left, 2=middle, 3=right)'
  },
  {
    name: 'mouse_check',
    category: 'Input Handling',
    prototype: 'mouse_check(button)',
    description: 'Returns True if mouse button is currently held down'
  },
  {
    name: 'mouse_check_released',
    category: 'Input Handling',
    prototype: 'mouse_check_released(button)',
    description: 'Returns True if mouse button was just released this frame'
  },
  {
    name: 'mouse_get_screen_x, mouse_get_screen_y',
    category: 'Input Handling',
    prototype: 'mouse_get_screen_x(), mouse_get_screen_y()',
    description: 'Get current mouse position in window coordinates'
  },
  {
    name: 'mouse_get_x, mouse_get_y',
    category: 'Input Handling',
    prototype: 'mouse_get_x(), mouse_get_y()',
    description: 'Get current mouse position in game coordinates'
  },

  // Audio Functions
  {
    name: 'play_sound',
    category: 'Audio',
    prototype: 'play_sound(sound_name, volume=1.0)',
    description: 'Play a loaded sound effect with optional volume control (0.0 to 1.0)'
  },
  {
    name: 'stop_sound',
    category: 'Audio',
    prototype: 'stop_sound(sound_name)',
    description: 'Stop playing the specified sound'
  },

  // Math Utilities
  {
    name: 'random_range',
    category: 'Math Utilities',
    prototype: 'random_range(min_val, max_val)',
    description: 'Generate a random float between min and max (inclusive)'
  },
  {
    name: 'random_int',
    category: 'Math Utilities',
    prototype: 'random_int(min_val, max_val)',
    description: 'Generate a random integer between min and max (inclusive)'
  },
  {
    name: 'clamp',
    category: 'Math Utilities',
    prototype: 'clamp(value, min_val, max_val)',
    description: 'Constrain a value to stay within the specified range'
  },
  {
    name: 'lerp',
    category: 'Math Utilities',
    prototype: 'lerp(start, end, factor)',
    description: 'Linear interpolation between start and end by factor (0.0 to 1.0)'
  },
  {
    name: 'distance',
    category: 'Math Utilities',
    prototype: 'distance(x1, y1, x2, y2)',
    description: 'Calculate Euclidean distance between two points'
  },
  {
    name: 'point_direction',
    category: 'Math Utilities',
    prototype: 'point_direction(x1, y1, x2, y2)',
    description: 'Calculate angle in degrees from point 1 to point 2'
  },
  {
    name: 'lengthdir_x',
    category: 'Math Utilities',
    prototype: 'lengthdir_x(length, direction)',
    description: 'Calculate X component of a vector with given length and direction (degrees)'
  },
  {
    name: 'lengthdir_y',
    category: 'Math Utilities',
    prototype: 'lengthdir_y(length, direction)',
    description: 'Calculate Y component of a vector with given length and direction (degrees)'
  },
  {
    name: 'sign',
    category: 'Math Utilities',
    prototype: 'sign(x)',
    description: 'Return the sign of a number (-1, 0, or 1)'
  },

  // Camera System & Window
  {
    name: 'camera_create',
    category: 'Camera System & Window',
    prototype: 'camera_create()',
    description: 'Create a new camera and return its ID'
  },
  {
    name: 'camera_set_active',
    category: 'Camera System & Window',
    prototype: 'camera_set_active(camera_id)',
    description: 'Set the active camera for rendering'
  },
  {
    name: 'camera_set_view_pos',
    category: 'Camera System & Window',
    prototype: 'camera_set_view_pos(camera_id, x, y)',
    description: 'Set camera position in the game world'
  },
  {
    name: 'camera_set_view_size',
    category: 'Camera System & Window',
    prototype: 'camera_set_view_size(camera_id, width, height)',
    description: 'Set camera view size (what area of the world to show)'
  },
  {
    name: 'camera_set_view_port',
    category: 'Camera System & Window',
    prototype: 'camera_set_view_port(camera_id, x, y, width, height)',
    description: 'Set camera viewport position and size on screen'
  },
  {
    name: 'camera_get_view_pos',
    category: 'Camera System & Window',
    prototype: 'camera_get_view_pos(camera_id=None)',
    description: 'Get current camera position as (x, y) tuple'
  },
  {
    name: 'camera_get_view_size',
    category: 'Camera System & Window',
    prototype: 'camera_get_view_size(camera_id=None)',
    description: 'Get camera view size as (width, height) tuple'
  },
  {
    name: 'camera_get_view_port',
    category: 'Camera System & Window',
    prototype: 'camera_get_view_port(camera_id=None)',
    description: 'Get current camera viewport as (x, y, width, height) tuple'
  },
  {
    name: 'window_get_size',
    category: 'Camera System & Window',
    prototype: 'window_get_size()',
    description: 'Get current window size as (width, height) tuple'
  },
  {
    name: 'window_set_size',
    category: 'Camera System & Window',
    prototype: 'window_set_size(width, height)',
    description: 'Set window size to specified dimensions'
  },

  // Entity Management
  {
    name: 'entity_create',
    category: 'Entity Management',
    prototype: 'entity_create(x, y, entity_class)',
    description: 'Create and add a new entity instance to the current scene'
  },
  {
    name: 'entity_destroy',
    category: 'Entity Management',
    prototype: 'entity_destroy(entity)',
    description: 'Mark an entity for destruction (will be removed next frame)'
  },
  {
    name: 'entity_number',
    category: 'Entity Management',
    prototype: 'entity_number(entity_type)',
    description: 'Count the number of entities of the specified type in current scene'
  },
  {
    name: 'get_entities',
    category: 'Entity Management',
    prototype: 'get_entities(entity_type)',
    description: 'Get a list of all entities of the specified type in current scene'
  },

  // Scene Management
  {
    name: 'go_to',
    category: 'Scene Management',
    prototype: 'go_to(scene_name)',
    description: 'Switch to and initialize the specified registered scene'
  },
  {
    name: 'scene_restart',
    category: 'Scene Management',
    prototype: 'scene_restart()',
    description: 'Reinitialize the current active scene (calls cleanup then create)'
  },

  // Game Utilities
  {
    name: 'get_delta_time',
    category: 'Game Utils',
    prototype: 'get_delta_time()',
    description: 'Return the time in seconds elapsed since the last frame'
  },
  {
    name: 'game_stop',
    category: 'Game Utils',
    prototype: 'game_stop()',
    description: 'Stop the game loop and close the window'
  }
];

export { functions }
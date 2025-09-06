const functions = [
  {
    name: 'load_assets',
    category: 'Asset Management',
    prototype: 'load_assets(folder="assets")',
    description: 'Load all sprites, sounds, and fonts from folder'
  },
  {
    name: 'draw_clear',
    category: 'Drawing Functions',
    prototype: 'draw_clear(color)',
    description: 'Clear screen with RGB color'
  },
  {
    name: 'draw_sprite',
    category: 'Drawing Functions',
    prototype: 'draw_sprite(x, y, name, xscale=1, yscale=1, angle=0)',
    description: 'Draw sprite with transformations'
  },
  {
    name: 'draw_text',
    category: 'Drawing Functions',
    prototype: 'draw_text(x, y, text, scale=1, font=None)',
    description: 'Draw text string'
  },
  {
    name: 'draw_rectangle',
    category: 'Drawing Functions',
    prototype: 'draw_rectangle(x, y, width, height, filled=True)',
    description: 'Draw rectangle'
  },
  {
    name: 'draw_circle',
    category: 'Drawing Functions',
    prototype: 'draw_circle(x, y, radius, filled=True)',
    description: 'Draw circle'
  },
  {
    name: 'draw_line',
    category: 'Drawing Functions',
    prototype: 'draw_line(x1, y1, x2, y2, width=1)',
    description: 'Draw line'
  },
  {
    name: 'draw_set_color',
    category: 'Drawing Functions',
    prototype: 'draw_set_color(rgb_tuple)',
    description: 'Set drawing color'
  },
  {
    name: 'draw_set_alpha',
    category: 'Drawing Functions',
    prototype: 'draw_set_alpha(alpha)',
    description: 'Set drawing transparency (0.0-1.0)'
  },
  {
    name: 'keyboard_check_pressed',
    category: 'Input Handling',
    prototype: 'keyboard_check_pressed(key)',
    description: 'True if key was just pressed this frame'
  },
  {
    name: 'keyboard_check',
    category: 'Input Handling',
    prototype: 'keyboard_check(key)',
    description: 'True if key is currently held down'
  },
  {
    name: 'keyboard_check_released',
    category: 'Input Handling',
    prototype: 'keyboard_check_released(key)',
    description: 'True if key was just released this frame'
  },
  {
    name: 'mouse_check_pressed',
    category: 'Input Handling',
    prototype: 'mouse_check_pressed(button)',
    description: 'True if mouse button just pressed (1=left, 2=middle, 3=right)'
  },
  {
    name: 'mouse_check',
    category: 'Input Handling',
    prototype: 'mouse_check(button)',
    description: 'True if mouse button held down'
  },
  {
    name: 'mouse_check_released',
    category: 'Input Handling',
    prototype: 'mouse_check_released(button)',
    description: 'True if mouse button just released'
  },
  {
    name: 'mouse_get_x, mouse_get_y',
    category: 'Input Handling',
    prototype: 'mouse_get_x(), mouse_get_y()',
    description: 'Get current mouse position'
  },
  {
    name: 'play_sound',
    category: 'Audio',
    prototype: 'play_sound(name, volume=1.0)',
    description: 'Play sound effect with volume control'
  },
  {
    name: 'stop_sound',
    category: 'Audio',
    prototype: 'stop_sound(name)',
    description: 'Stop playing sound'
  },
  {
    name: 'random_range',
    category: 'Math Utilities',
    prototype: 'random_range(min, max)',
    description: 'Generate random float between min and max'
  },
  {
    name: 'random_int',
    category: 'Math Utilities',
    prototype: 'random_int(min, max)',
    description: 'Generate random integer between min and max (inclusive)'
  },
  {
    name: 'clamp',
    category: 'Math Utilities',
    prototype: 'clamp(value, min, max)',
    description: 'Constrain value within range'
  },
  {
    name: 'lerp',
    category: 'Math Utilities',
    prototype: 'lerp(start, end, factor)',
    description: 'Linear interpolation between two values'
  },
  {
    name: 'distance',
    category: 'Math Utilities',
    prototype: 'distance(x1, y1, x2, y2)',
    description: 'Calculate Euclidean distance between points'
  },
  {
    name: 'point_direction',
    category: 'Math Utilities',
    prototype: 'point_direction(x1, y1, x2, y2)',
    description: 'Calculate angle between points in degrees'
  },
  {
    name: 'lengthdir_x',
    category: 'Math Utilities',
    prototype: 'lengthdir_x(length, direction)',
    description: 'Get X component of vector'
  },
  {
    name: 'lengthdir_y',
    category: 'Math Utilities',
    prototype: 'lengthdir_y(length, direction)',
    description: 'Get Y component of vector'
  },
  {
    name: 'surface_create',
    category: 'Surface Management',
    prototype: 'surface_create(width, height)',
    description: 'Create new drawing surface'
  },
  {
    name: 'surface_set_target',
    category: 'Surface Management',
    prototype: 'surface_set_target(surface)',
    description: 'Set drawing target to surface'
  },
  {
    name: 'surface_reset_target',
    category: 'Surface Management',
    prototype: 'surface_reset_target()',
    description: 'Reset drawing target to screen'
  },
  {
    name: 'surface_draw',
    category: 'Surface Management',
    prototype: 'surface_draw(x, y, surface, xscale=1, yscale=1)',
    description: 'Draw surface to current target'
  },
  {
    name: 'surface_destroy',
    category: 'Surface Management',
    prototype: 'surface_destroy(surface)',
    description: 'Free surface memory'
  },
  {
    name: 'camera_create',
    category: 'Camera System & Window',
    prototype: 'camera_create()',
    description: 'Create new camera, returns camera ID'
  },
  {
    name: 'camera_set_active',
    category: 'Camera System & Window',
    prototype: 'camera_set_active(id)',
    description: 'Make camera active'
  },
  {
    name: 'camera_set_view_pos',
    category: 'Camera System & Window',
    prototype: 'camera_set_view_pos(id, x, y)',
    description: 'Set camera position in world'
  },
  {
    name: 'camera_set_view_size',
    category: 'Camera System & Window',
    prototype: 'camera_set_view_size(id, w, y)',
    description: 'Set camera size'
  },
  {
    name: 'camera_set_view_port',
    category: 'Camera System & Window',
    prototype: 'camera_set_view_port(id, x, y, width, height)',
    description: 'Set camera viewport on screen'
  },
  {
    name: 'camera_get_view_pos',
    category: 'Camera System & Window',
    prototype: 'camera_get_view_pos(id=None)',
    description: 'Get camera position'
  },
  {
    name: 'camera_get_view_port',
    category: 'Camera System & Window',
    prototype: 'camera_get_view_port(id=None)',
    description: 'Get camera port'
  },
  {
    name: 'window_get_size',
    category: 'Camera System & Window',
    prototype: 'window_get_size()',
    description: 'Get window size'
  },
  {
    name: 'window_set_size',
    category: 'Camera System & Window',
    prototype: 'window_set_size(width, height)',
    description: 'Set window size'
  },
  {
    name: 'entity_create',
    category: 'Entity Management',
    prototype: 'entity_create(x, y, entity_class)',
    description: 'Create and add entity to current scene'
  },
  {
    name: 'entity_destroy',
    category: 'Entity Management',
    prototype: 'entity_destroy(entity)',
    description: 'Mark entity for destruction'
  },
  {
    name: 'entity_number',
    category: 'Entity Management',
    prototype: 'entity_number(entity_type)',
    description: 'Counts the number of entities of a given type'
  },
  {
    name: 'get_entities',
    category: 'Entity Management',
    prototype: 'get_entities(entity_type)',
    description: 'Get the list of entities of a type'
  },
  {
    name: 'go_to',
    category: 'Scene Management',
    prototype: 'go_to(scene)',
    description: 'Initialize and activate a registered scene'
  },
  {
    name: 'scene_restart',
    category: 'Scene Management',
    prototype: 'scene_restart()',
    description: 'Reinitialize the current active scene'
  },
  {
    name: 'get_delta_time',
    category: 'Game Utils',
    prototype: 'get_delta_time()',
    description: 'Return the time in seconds since the last frame'
  },
  {
    name: 'game_stop',
    category: 'Game Utils',
    prototype: 'game_stop()',
    description: 'Stop the game then close the window'
  }
];

export { functions  }

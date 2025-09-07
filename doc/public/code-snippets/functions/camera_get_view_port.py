from ViviEngine import *

camera_id = camera_create()
camera_set_active(camera_id)
camera_set_view_size(camera_id, 800, 450)
camera_set_view_port(camera_id, 0, 0, 1920, 1080)
camera_width, camera_height = camera_get_view_size(camera_id)
camera_set_view_pos(camera_id, scene_width / 2 - camera_width / 2, scene_height / 2 - camera_height / 2)

x, y, w, h = camera_get_view_port(camera_id)
if (window_get_size() != (w, h)):
    window_set_size(w, h)
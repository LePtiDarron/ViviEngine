from ViviEngine import *

surf = surface_create(32, 32)
surface_set_target(surf)
draw_clear(RED)
surface_reset_target()
surface_draw(0, 0, surf)
surface_destroy(surf)
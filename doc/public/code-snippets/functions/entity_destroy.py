from VIviEngine import *

class MyScene(Scene):
    def step(self):
        super().step()
        r = random_range(0, 100)
        if r < 50:
            entity_create(0, 0, MyObject)
            if (entity_number(MyObject) > 10):
                print('Victory')
                game_stop()
        else:
            if (entity_number(MyObject) == 0):
                print('Defeat')
                game_stop()
            my_objects = get_entities(MyObject)
            entity_destroy(my_objects[0])
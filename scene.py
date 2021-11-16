from ray import *

RAY_COUNT = 300

class Scene:
    def __init__(self, size):
        self.objects = []
        self.size = size

    def add_object(self, scene_object):
        self.objects.append(scene_object)

    def set_object(self, index, new_object):
        self.objects[index] = new_object

    def get_objects(self):
        return self.objects

    def ray_destinations(self, starting_position):
        dots = []
        angle = 0.0
        while angle < 2 * math.pi:
            ray = Ray(self, starting_position, angle)
            ray_destination = ray.march()
            if ray_destination is not None:
                dots.append(ray_destination)
            angle += 1 / RAY_COUNT * 2 * math.pi
        return dots

    def get_size(self):
        return self.size
import math
from scene import *

RAY_THRESHOLD = 1

class Ray:
    def __init__(self, scene, position, angle):
        self.scene = scene
        self.position = position
        self.angle = angle

    def __minimum_distance(self):
        position = self.__get_position()
        scene = self.__get_scene()
        distances_to_objects = [obj.distance(position) for obj in scene.get_objects()]
        x, y = position
        distances_to_walls = [abs(x), abs(y), abs(x - 1000), abs(y - 1000)]
        return min(distances_to_objects + distances_to_walls)

    def march(self):
        scene_size = self.__get_scene().get_size()
        step_distance = self.__step()
        while step_distance > RAY_THRESHOLD:
            step_distance = self.__step()
        return self.__get_position()

    def __step(self):
        minimum_distance = self.__minimum_distance()
        x, y = self.__get_position()
        angle = self.__get_angle()
        delta_x = math.cos(angle) * minimum_distance
        delta_y = math.sin(angle) * minimum_distance
        self.__update_position((x + delta_x, y + delta_y))
        return max(abs(delta_x), abs(delta_y))

    def __get_position(self):
        return self.position

    def __get_angle(self):
        return self.angle

    def __get_scene(self):
        return self.scene

    def __update_position(self, new_position):
        self.position = new_position
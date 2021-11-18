from ray import *
import math

RAY_COUNT = 200
FOV = 90

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

    def ray_destinations(self, starting_position, is3D, direction):
        dots = []
        if not is3D:
            angle = 0.0
            while angle < 2 * math.pi:
                ray = Ray(self, starting_position, angle)
                ray_destination = ray.march()
                dots.append(ray_destination)
                angle += 1 / RAY_COUNT * 2 * math.pi
        else:
            dots = self.__projection(starting_position, direction)
        return dots

    def __projection(self, starting_position, direction):
        offset = 200
        leftangle = direction + (FOV / 360 * math.pi)
        rightangle = direction - (FOV / 360 * math.pi)
        x, y = starting_position
        dots = []
        lx = x + offset * math.cos(leftangle)
        ly = y + offset * math.sin(leftangle)
        rx = x + offset * math.cos(rightangle)
        ry = y + offset * math.sin(rightangle)
        dx, dy = (rx - lx) / (RAY_COUNT - 1), (ry - ly) / (RAY_COUNT - 1)
        cx, cy = lx, ly
        angle = leftangle
        for i in range(RAY_COUNT):
            #shoot ray
            ray = Ray(self, starting_position, angle)
            ray_destination = ray.march()
            rx, ry = ray_destination
            dots.append(max(1, math.sqrt((rx - x) ** 2 + (ry - y) ** 2)))

            #update angle
            cx += dx
            cy += dy
            angle = math.atan2(cy - y, cx - x)
        return dots

    def get_size(self):
        return self.size
import numpy
import math

class Object:
    def __init__(self, position):
        self.position = position

    def distance_to_centre(self, camera_position):
        object_position = self.get_position()
        x1, y1 = camera_position
        x2, y2 = object_position
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position

class Circle(Object):
    def __init__(self, position, radius):
        super().__init__(position)
        self.radius = radius

    def distance(self, camera_position):
        dist_to_centre = self.__distance_to_centre(camera_position)
        return dist_to_centre - self.get_radius()

    def get_radius(self):
        return self.radius

    def __distance_to_centre(self, camera_position):
        return super().distance_to_centre(camera_position)

    def get_position(self):
        return super().get_position()

class Square(Object):
    def __init__(self, position, size, corner_radius = 0, rotation = 0):
        super().__init__(position)
        self.size = size
        self.corner_radius = corner_radius
        self.rotation = rotation

    # We rotate points on the plane using trigonometry and then using the new points
    # for our distance function
    def __rotate_point(self, x, y):
        angle = numpy.arctan2(y, x)
        new_angle = angle - self.get_rotation()
        xy_dist = math.sqrt(x ** 2 + y ** 2)
        return xy_dist * math.cos(new_angle), xy_dist * math.sin(new_angle)

    def distance(self, camera_position):
        corner_radius = self.get_corner_radius()

        sx, sy = self.get_size()
        rx, ry = sx / 2 - corner_radius, sy / 2 - corner_radius

        x, y = camera_position
        bx, by = self.get_position()

        px, py = x - bx, y - by
        px, py = self.__rotate_point(px, py)

        dist = math.sqrt(max(abs(px) - rx, 0) ** 2 + max(abs(py) - ry, 0) ** 2)
        return dist - corner_radius

    def get_size(self):
        return self.size

    def get_corner_radius(self):
        return self.corner_radius

    def get_rotation(self):
        return self.rotation

    def __distance_to_centre(self, camera_position):
        return super().distance_to_centre(camera_position)

    def get_position(self):
        return super().get_position()

    def set_position(self, new_position):
        super().set_position(new_position)
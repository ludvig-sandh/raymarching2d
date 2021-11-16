import pygame
from object import *

BACKGROUND_COLOR = (30, 30, 30)
COLOR1 = (100, 100, 100)
COLOR2 = (150, 150, 150)

class Graphics:
    def __init__(self, width, height):
        self.width, self.height = width, height
        pygame.init()
        self.__create_screen()

    # Set up the drawing window
    def __create_screen(self):
        self.screen = pygame.display.set_mode([self.__get_width(), self.__get_height()])

    # Display everything on screen
    def display_scene(self, dots, objects, camera_position):
        self.__reset_screen()
        self.__draw_dots(dots)
        self.__draw_objects(objects)
        self.__draw_camera(camera_position)
        pygame.display.flip()

    # Reset screen
    def __reset_screen(self):
        # Fill the background
        self.__get_screen().fill(BACKGROUND_COLOR)

    def __draw_dots(self, dots):
        pygame.draw.polygon(self.__get_screen(), COLOR1, dots)

    def __draw_camera(self, camera_position):
        pygame.draw.circle(self.__get_screen(), (255, 255, 0), camera_position, 10)

    def __draw_objects(self, objects):
        for obj in objects:
            x, y = obj.get_position()
            x, y = int(x), int(y)
            if type(obj) == Circle:
                radius = obj.get_radius()
                pygame.draw.circle(self.__get_screen(), COLOR2, (x, y), radius)
            elif type(obj) == Square:
                w, h = obj.get_size()
                corner_radius = obj.get_corner_radius()
                sx, sy = obj.get_position()

                points = []
                for v in range(180, 90, -1):
                    radians = v / 180 * math.pi
                    points.append((-w / 2 + corner_radius * (1 + math.cos(radians)), h / 2 - corner_radius * (1 - math.sin(radians))))

                for v in range(90, 0, -1):
                    radians = v / 180 * math.pi
                    points.append((w / 2 - corner_radius * (1 - math.cos(radians)), h / 2 - corner_radius * (1 - math.sin(radians))))

                for v in range(360, 270, -1):
                    radians = v / 180 * math.pi
                    points.append((w / 2 - corner_radius * (1 - math.cos(radians)), -h / 2 + corner_radius * (1 + math.sin(radians))))

                for v in range(270, 180, -1):
                    radians = v / 180 * math.pi
                    points.append((-w / 2 + corner_radius * (1 + math.cos(radians)), -h / 2 + corner_radius * (1 + math.sin(radians))))
                
                points.append((-w / 2, h / 2 - corner_radius))

                # Rotate points if the rectangle itself has a rotation
                for i in range(len(points)):
                    x, y = points[i]

                    angle = numpy.arctan2(y, x)
                    new_angle = angle + obj.get_rotation()
                    xy_dist = math.sqrt(x ** 2 + y ** 2)
                    x, y = xy_dist * math.cos(new_angle), xy_dist * math.sin(new_angle)
                    points[i] = (x + sx, y + sy)

                pygame.draw.polygon(self.__get_screen(), COLOR2, points)
                
    def __get_width(self):
        return self.width

    def __get_height(self):
        return self.height

    def __get_screen(self):
        return self.screen
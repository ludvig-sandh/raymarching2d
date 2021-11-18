# Ludvig Sandh

from pygame.constants import KEYDOWN
from scene import *
from graphics import *
from object import *
import pygame

def add_scene_objects(scene):
    scene.add_object(Square((800, 300), (70, 140), 30, 0.3))
    scene.add_object(Square((900, 500), (200, 200), 40))
    scene.add_object(Square((300, 200), (25, 100), 15))
    scene.add_object(Circle((925, 725), 80))
    scene.add_object(Circle((800, 800), 100))
    scene.add_object(Circle((200, 300), 50))
    scene.add_object(Circle((50, 800), 100))
    scene.add_object(Square((500, 100), (100, 10), 0))
    scene.add_object(Circle((500, 350), 35))
    scene.add_object(Circle((500, 300), 20))


if __name__ == "__main__":
    scene = Scene(1000.0)

    # Add some showcase objects
    add_scene_objects(scene)
    

    graphics = Graphics(1000, 1000)
    clock = pygame.time.Clock()
    camera_position = (50.0, 50.0)
    rot = 0.0

    is3D = False
    direction = 0.0

    while True:
        # Check for user-events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is3D = not is3D
        
        direction = direction % (math.pi * 2)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            direction -= math.pi / 30
        elif keys[pygame.K_d]:
            direction += math.pi / 30
        elif keys[pygame.K_w] or keys[pygame.K_s]:
            x, y = camera_position
            dx = 10 * math.cos(direction)
            dy = 10 * math.sin(direction)

            if keys[pygame.K_w]:
                y += dy
                x += dx
            elif keys[pygame.K_s]:
                y -= dy
                x -= dx

            x = max(x, 10)
            y = max(y, 10)
            x = min(x, 990)
            y = min(y, 990)
            camera_position = x, y

        if pygame.mouse.get_pressed()[0] and not is3D:
            pos = pygame.mouse.get_pos()
            camera_position = pos

        # Animate some stuff on screen
        rot += 0.2
        radians = rot % (2 * math.pi)
        scene.set_object(2, Square((300, 200), (25, 100), 15, radians))
        scene.set_object(8, Circle((500 + 150 * math.cos(radians), 500 + 150 * math.sin(radians)), 35))
        scene.set_object(9, Circle((500 - 200 * math.cos(radians + math.pi / 1.5 + math.sqrt(rot)), 500 + 200 * math.sin(radians)), 20))
            
        # Cast rays and display scene
        clock.tick(60)
        dots = scene.ray_destinations(camera_position, is3D, direction)
        graphics.display_scene(dots, scene.get_objects(), camera_position, is3D)
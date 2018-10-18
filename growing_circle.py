import pygame
from pygame.locals import *
from pygame import Color, Rect
import sys
import math
import numpy as np


def get_screen_size():
    """return screen (width, height) tuple"""
    screen = pygame.display.get_surface()
    return screen.get_size()


class Circle():
    def __init__(self, center=None, angle=6):
        self.width = 4
        self.height = 4

        if center is None:
            self.center = np.array([400, 400])
        else:
            self.center = center

        self.angle = angle
        self.speed = np.array([1, 1])

        self.points = []
        for x in range(self.angle):
            self.points.append( center )

    def update(self):
        interval = 360/self.angle
        rad = 0
        newPoints = []
        for pt in self.points:
            #speed = np.random.randint(1, 5)
            speed = 1
            x = np.cos(math.radians(rad))
            y = np.sin(math.radians(rad))
            velocity = np.array([x, y])
            velocity *= speed
            pt = np.add(pt, velocity)
            newPoints.append(pt)
            #print("rad:{}, velocity:{}".format(rad, velocity))
            rad += interval
            
        self.points = newPoints
            
    def is_onscreen(self):
        return True

class GameMain():
    """game Main entry point. handles intialization of game and graphics."""
    done = False
    debug = False
    color_gray = Color('lightgray')
    circles = []

    def __init__(self, width=800, height=600, color_bg=None):
        """Initialize PyGame"""
        pygame.init()
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Growing circle : pygame")

        self.clock = pygame.time.Clock()
        self.limit_fps = True
        self.limit_fps_max = 60

        if color_bg is None:
            color_bg = Color(50, 50, 50)
        self.color_bg = color_bg

        self.game_init()

    def game_init(self):
        """new game/round"""
        self.cirlces = []

    def loop(self):
        """Game() main loop"""
        while not self.done:
            self.handle_events()
            self.update()
            self.draw()

            if self.limit_fps:
                self.clock.tick(self.limit_fps_max)
            else:
                self.clock.tick()

    def update(self):
        for c in self.circles:
            c.update()

            if not c.is_onscreen():
                c.rand_loc()


    def handle_events(self):
        """handle regular events. """
        events = pygame.event.get()
        # kmods = pygame.key.get_mods() # key modifiers

        for event in events:
            if event.type == pygame.QUIT:
                # Sould set to the self.done = False!!! and call sys.exit() 
                self.done = True
                sys.exit()
            elif event.type == KEYDOWN:
                if (event.key == K_ESCAPE):
                    self.done = True
                elif (event.key == K_SPACE):
                    self.game_init()
            elif event.type == MOUSEBUTTONUP and event.button == 1 :
                pos = pygame.mouse.get_pos()
                #self.circles.append( Circle(pos, 6))
                self.circles.append( Circle(pos, 8))


    def draw(self):
        """render screen"""
        # clear screen
        self.screen.fill(self.color_bg)

        # Circle: draw
        for c in self.circles:
            for pt in c.points:
                r = Rect(pt[0], pt[1], c.width, c.height)
                self.screen.fill(self.color_gray, r)

        # will call update on whole screen Or flip buffer.
        pygame.display.flip()


if __name__ == '__main__':
    g = GameMain()
    g.loop()

"""
Missions:
  - Change the circle's color when it raises.
  - Vary the speed of the growing circle.
  - Check the edge of the screen and circles disappears when it outside of the screen.
  - Add some sound effects when playes clicks the mouse.
"""
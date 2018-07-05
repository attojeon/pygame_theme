
import os
import sys
import pygame as pg

SCREEN_SIZE = (500, 500)
BACKGROUND_COLOR = (50, 50, 60)
CAPTION = "Event Handler"


class EventControl(object):
    def __init__(self):
        """
        클래스가 생성될 때 가장 먼저 실행됩니다.
        """
        pg.init()
        os.environ["SDL_VIDEO_CENTERED"] = "TRUE"
        pg.display.set_caption(CAPTION)
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60.0
        self.done = False
        self.points = []


    def event_loop(self):
        """
        
        """
        for event in pg.event.get():
            keys = pg.key.get_pressed()
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                self.done = True
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                pass
            elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
                pos = pg.mouse.get_pos()
                self.points.append(pos)
                print("Mouse Clicked:{}, {}".format(pos[0], pos[1]))
            elif event.type == pg.KEYDOWN:
                key = event.unicode 
                print('key pressed : {}'.format(key))

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.screen.fill(BACKGROUND_COLOR)
            pg.display.update()
            self.clock.tick(self.fps)


def main():
    control = EventControl()
    control.main_loop()
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()

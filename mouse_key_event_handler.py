
import os
import sys
import pygame as pg

SCREEN_SIZE = (500, 500)
BACKGROUND_COLOR = (50, 50, 60)
CAPTION = "Event Handler"


pg.init()
os.environ["SDL_VIDEO_CENTERED"] = "TRUE"
pg.display.set_caption(CAPTION)
screen = pg.display.set_mode(SCREEN_SIZE)
clock = pg.time.Clock()
fps = 60.0
done = False
points = []


def event_loop():
    global done
    
    for event in pg.event.get():
        keys = pg.key.get_pressed()
        if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
            done = True
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            pass
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            pos = pg.mouse.get_pos()
            points.append(pos)
            print("Mouse Clicked:{}, {}".format(pos[0], pos[1]))
        elif event.type == pg.KEYDOWN:
            key = event.unicode
            print('key pressed : {}'.format(key))

def main_loop():
    """The bare minimum for a functioning main loop."""
    while not done:
        event_loop()
        screen.fill(BACKGROUND_COLOR)
        pg.display.update()
        clock.tick(fps)


def main():
    main_loop()
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()

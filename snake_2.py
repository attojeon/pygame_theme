
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
matrix = []
head = [5,5]
rows = 10
cols = 10


def set_matrix(r, c):
    matrix[r, c] = 1


# working....
def move_head(r, c, direction):
    cur_r = head[0]
    cur_c = head[1]
    if direction == UP:
        pass
    elif direction == DOWN:
        pass
    elif direction == LEFT:
        pass
    elif dirction == RIGHT:
        pass
    else:
        print("move_head error")


def game_data_init():
    onerow = []
    for i in range(0, rows):
        for j in range(0, cols):
            onerow.append(0)
        matrix.append(onerow)
        onerow = []

    set_matrix(head[0], head[1])


def display_matrix():
    for r in matrix:
        print(r)



def process_key(key):
    if( key == pg.K_LEFT):
        display_matrix()
    if( key == pg.K_RIGHT) :
        display_matrix()



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
            #key = event.unicode  # 알파벳 등은 보여질 수 있으나 특수문자 키(스페이스, 엔터 등)은 볼 수 없음.
            #print('key pressed : {}'.format(key))
            process_key(event.key)
            
    
    

def main_loop():
    """The bare minimum for a functioning main loop."""
    while not done:
        event_loop()
        screen.fill(BACKGROUND_COLOR)
        pg.display.update()
        clock.tick(fps)


def main():
    game_data_init()
    main_loop()
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
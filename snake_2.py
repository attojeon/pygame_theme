##################################################
# 사용법
# - 방향키를 누르면 콘솔화면에 matrix가 업데이트 되어 보여진다.
# - 스페이스 키를 누르면 뱀의 꼬리가 하나 길어진다.
##################################################

import os
import sys
import pygame as pg
#import time

SCREEN_SIZE = (500, 500)
BACKGROUND_COLOR = (50, 50, 60)
CAPTION = "스네이크 게임 튜토리얼 레벨 2"

pg.init()
os.environ["SDL_VIDEO_CENTERED"] = "TRUE"
pg.display.set_caption(CAPTION)
screen = pg.display.set_mode(SCREEN_SIZE)
clock = pg.time.Clock()
fps = 60.0
done = False
points = []
matrix = []
snake_coor = []
rows = 12
cols = 12
dir_c, dir_r = 0, 1  #수평방향:dir_c, 수직방향:dir_r


def setDir(c,r):
    global dir_c, dir_r
    dir_c = c
    dir_r = r



def board_init():
    global matrix
    matrix = []
    onerow = []
    for i in range(0, rows):
        for j in range(0, cols):
            # wall value setting
            onerow.append(9) if  j == 0 or j == (cols-1) or i == 0 or i == (rows-1) else onerow.append(0)
        matrix.append(onerow)
        onerow = []


def game_data_init():
    board_init()
    snake_coor.append([1,1])


def display_matrix():
    for r in matrix:
        print(r)
    print()


def snake_eat_apple():
    global snake_coor
    a = snake_coor[-1][:]
    snake_coor.append(a)


'''
아래와 같이 값이 대응된다. 
r -> y
c -> x 
x,y좌표를 r,c와 매칭하여 연산해야 한다.
'''
def process_key(key):
    if( key == pg.K_LEFT):
        setDir(-1, 0)
        display_matrix()
    elif( key == pg.K_RIGHT) :
        setDir(1, 0)
        display_matrix()
    elif( key == pg.K_UP):
        setDir(0, -1)
        display_matrix()
    elif( key == pg.K_DOWN):
        setDir(0, 1)
        display_matrix()
    elif( key == pg.K_SPACE):
        snake_eat_apple()
        display_matrix()
    else:
        pass
    


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
            key = event.unicode  # 알파벳 등은 보여질 수 있으나 특수문자 키(스페이스, 엔터 등)은 볼 수 없음.
            print('key pressed : {}'.format(key))
            process_key(event.key)
            

def forward():
    r,c  = snake_coor[0]
    r += dir_r
    c += dir_c
    snake_coor.insert(0, (r,c))
    snake_coor.pop(-1)


def object_update():
    board_init()
    for rc in snake_coor:
        matrix[rc[0]][rc[1]] = 5
    
# 함수로 구현한 메인 루프
def main_loop():
    count = 0
    while not done:
        event_loop()
        if count % 60 == 0:
            forward()
            count = 0
        object_update()
        screen.fill(BACKGROUND_COLOR)
        pg.display.update()
        count += 1
        clock.tick(fps)


def main():
    game_data_init()
    main_loop()
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
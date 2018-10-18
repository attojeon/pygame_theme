import pygame as pg
from pygame.locals import *
from pygame import Color, Rect
import sys
import math
import numpy as np
import random


SCREEN_SIZE = (500, 500)
BACKGROUND_COLOR = (50, 50, 60)
CAPTION = "스네이크 게임 튜토리얼 레벨 1"

pg.init()
pg.display.set_caption(CAPTION)
screen = pg.display.set_mode(SCREEN_SIZE)
clock = pg.time.Clock()
fps = 60.0
done = False

# pygame의 지정된 색상 갯수 출력
print( len(pg.color.THECOLORS) )

# pygame의 지정된 색상을 모두 차례대로 출력하는 방법
idx = 0
for k, v in pg.color.THECOLORS.items():
    print("idx:{}, key:{}, value:{}".format(idx, k, v))
    idx += 1

# pygame의 지정된 색상 중 랜덤한 색상을 출력하는 방법
print("=======")
print( list(pg.color.THECOLORS.keys())[20] )



def init():
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
            print("Mouse Clicked:{}, {}".format(pos[0], pos[1]))
        elif event.type == pg.KEYDOWN:
            key = event.unicode  # 알파벳 등은 보여질 수 있으나 특수문자 키(스페이스, 엔터 등)은 볼 수 없음.
            print('key pressed : {}'.format(key))
    
    

def main_loop():
    # 함수로 구현한 메인 루프
    while not done:
        event_loop()
        screen.fill(BACKGROUND_COLOR)
        pg.display.update()
        clock.tick(fps)


def main():
    init()
    main_loop()
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
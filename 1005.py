##################################################
# pygame - 마우스 이벤트(MOUSEDOWN) 이해
#
# 참고 사이트 
# https://pg.org
# https://pg.org/docs/
##################################################

import pygame as pg
import sys
import time

# 초기화 작업
# 반드시 주어진 함수이름과 순서를 지켜야 함.

pg.init()
screen = pg.display.set_mode((400, 300))
pg.display.set_caption("pygame 이해하기")

x1 = 0
y1 = 0
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            x1 = pos[0]
            y1 = pos[1]

    screen.fill((0, 0, 0))

    pg.draw.rect(screen, (0, 255, 0), (x1, y1, 44, 44), 2)

    pg.display.update()
    
    time.sleep(0.1)

print('메인루프 종료')
pg.quit()

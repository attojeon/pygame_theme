##################################################
# pygame - 키보드 추가 이벤트
#
# 참고 사이트
# https://pg.org
# https://pg.org/docs/
#
# space 다운로드 사이트
# http://learnsteam.co.kr/dn/space.zip
##################################################

import pygame as pg
import sys
import time

# 초기화 작업
# 반드시 주어진 함수이름과 순서를 지켜야 함.

pg.init()
screen = pg.display.set_mode((320, 600))
pg.display.set_caption("pygame 이해하기")

ship = pg.image.load("img/spaceship.png")
pos_x = 160
pos_y = 550
SHIP_LEFT = -5
SHIP_RIGHT = 5
direction = SHIP_LEFT
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            key_event = pg.key.get_pressed()
            if key_event[pg.K_LEFT]:
                direction = SHIP_LEFT
            elif key_event[pg.K_RIGHT]:
                direction = SHIP_RIGHT

    pos_x += direction
    print(pos_x)
    screen.fill((255, 255, 255))
    screen.blit(ship, (pos_x, pos_y))
    pg.display.update()

    time.sleep(0.1)

print('메인루프 종료')
pg.quit()

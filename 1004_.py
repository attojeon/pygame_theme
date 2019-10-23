##################################################
# pygame - 이미지를 화면에 표시하기
#
# 참고 사이트 
# https://pygame.org
# https://pygame.org/docs/
##################################################

import pygame as pg
import sys
import time

# 초기화 작업
# 반드시 주어진 함수이름과 순서를 지켜야 함.
pg.init()
screen = pg.display.set_mode((400, 300))
pg.display.set_caption("pygame 이미지")

# 메모리에 이미지를 로딩합니다.
# 이 때 현재 폴더에 있는 img 폴더의 위치를 표시하기 위해 img/ 를 잊으면 안됩니다.
player = pg.image.load("img/player.png")
#player2 = pg.image.load("img/player.png").convert_alpha()

# 전역변수 세팅
pos_x = 100
pos_y = 100
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))
    # 이미지를 화면에 그립니다.
    screen.blit(player, (pos_x, pos_y))

    pg.display.update()
    
    time.sleep(0.1)

print('메인루프 종료')
pg.quit()

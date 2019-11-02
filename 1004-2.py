##################################################
# pygame - 이미지를 움직이기
#
# 참고 사이트 
# https://pygame.org
# https://pygame.org/docs/
#
# 다운로드 사이트
# http://learnsteam.co.kr/dn/animals.zip
#
# 다운로드 받은 후
#  - 자기의 소스(`.py`)가 있는 디렉토리에서 'img'를 만들고 그 폴더 안에 이미지 파일들이 있어야 합니다.
#  - mysrc.py 
#  -      + -- img(폴더)
#  -            +-- player.png 
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

    pos_x += 1
    
    time.sleep(0.1)

print('메인루프 종료')
pg.quit()

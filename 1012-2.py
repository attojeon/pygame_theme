##################################################
# pygame - 게임에서 문자 렌더링(Rendering))
#
# 참고 사이트
# https://pg.org
# https://pg.org/docs/
#
# space 다운로드 사이트
# http://learnsteam.co.kr/dn/space.zip
# http://learnsteam.co.kr/dn/gamesound.zip
##################################################
import random

import pygame as pg
import sys
import time

# 초기화 작업
# 반드시 주어진 함수이름과 순서를 지켜야 함.

WIDHT = 320
HEIGHT = 600

pg.init()
screen = pg.display.set_mode((WIDHT, HEIGHT))
pg.display.set_caption("pygame 이해하기")

# 화면에 렌더링하는 글자값을 변경하기 위해 변수를 세팅한다.
font = pg.font.SysFont("Arial", 16)
text = "Game Score:0"
text_surface = font.render(text, True, (255, 0, 0) )

running = True
loops = 0
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # 화면 전체 지우기
    screen.fill((255, 255, 255))
    screen.blit(text_surface, (100, 20))

    # 화면에 렌더링할 글자가 바뀔 때마다 렌더링을 호출해야 한다.
    text_new = "Game Score:" + str(loops)
    text_surface = font.render(text_new, True, (255, 0, 0))

    # 화면갱신
    pg.display.update()

    loops +=1
    time.sleep(0.1)

print('메인루프 종료')
pg.quit()


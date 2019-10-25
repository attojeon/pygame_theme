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

# pygame 에서 화면에 글자를 쓰는 것이 아니라 그리는 것이라 생각
# font 설정은 한 번만 해도 됨.
# font 를 렌더링해서 글자이미지의 화면영역(text_surface)를 구함.
# 화면에 렌더링할 글자, 안티알리어싱, 색상을 지정하여 fonet.render를 수행한다.
font = pg.font.SysFont("Arial", 32)
text_surface = font.render("Game Score:", True, (255, 0, 0) )

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # 화면 전체 지우기
    screen.fill((255, 255, 255))

    # 이미지 그리기와 같이 screen.blit을 진행한다.
    screen.blit(text_surface, (100, 20))

    # 화면갱신
    pg.display.update()

    time.sleep(0.1)

print('메인루프 종료')
pg.quit()

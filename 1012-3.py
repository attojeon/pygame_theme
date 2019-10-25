### 미완성 : 난이도가 너무 높은 것 같음.
##################################################
# pygame - 게임에서 문자 렌더링과 마우스이벤트 결합
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
text = "Click Me!!!"
text_surface = font.render(text, True, (255, 0, 0) )

# 게임 오브젝트를 만듬.
clicked = False
player = [ pg.Rect(10, 10, 50, 50), text_surface, False]

def draw_player():
    global text_surface
    screen.fill((255, 0, 0), player[0])
    screen.blit(text_surface, text_surface.get_rect())

def check_click(pos):
    global clicked, player
    if player[0].collidepoint(pos) == True:
        clicked = True

def move_player(delta):
    global player
    print(delta)

running = True
loops = 0
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            delta = event.pos.get_rel()
            check_click(event.pos)
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            clicked = False

    # click이 된 상태라면 player의 위치를 계산한다.
    #move_player(delta)

    # 화면 전체 지우기
    screen.fill((255, 255, 255))
    screen.blit(text_surface, (100, 20))

    draw_player()


    # 화면갱신
    pg.display.update()

    loops +=1
    time.sleep(0.1)

print('메인루프 종료')
pg.quit()

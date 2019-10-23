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

##################################################
# 문제1 : 아래의 코드를 이해하고 화면에서 캐릭터가 오른쪽으로 움직이도록 코드를 수정해 보시오.
# 문제2 : img폴더 안에는 cat.png라는 고양이 이미지가 한 개 더 있습니다. 화면에 고양이와 우산소녀가 같이 등장하게 프로그램을 수정하시오.
# 문제3 : 고양이와 우산소녀가 움직일 수 있도록 pos_x, pos_y의 변수의 값이 while 루프 안에 계산 로직을 추가해 보시오.
##################################################

import pygame as pg
import sys
import time

# 초기화 작업
# 반드시 주어진 함수이름과 순서를 지켜야 함.

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("pygame 이해하기")

ship = pg.image.load("img/spaceship.png")
pos_x = 400
pos_y = 300
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            key_event = pg.key.get_pressed()
            print(key_event)
            if key_event[pg.K_UP]:
                pos_y -= 10
            elif key_event[pg.K_DOWN]:
                pos_y += 10
            elif key_event[pg.K_LEFT]:
                pos_x -= 10
            elif key_event[pg.K_RIGHT]:
                pos_x += 10

    screen.fill((255, 255, 255))
    screen.blit(ship, (pos_x, pos_y))
    pg.display.update()
    
    time.sleep(0.1)

print('메인루프 종료')
pg.quit()

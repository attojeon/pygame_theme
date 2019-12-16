##################################################
# pygame - 삼각함수 사용하여 회전하는 시계바늘을 구현해 봄
#
# 참고 사이트 
# https://pygame.org
# https://pygame.org/docs/
##################################################

import pygame
import sys
import time
import math

# 초기화 작업
# 반드시 주어진 함수이름과 순서를 지켜야 함.

pygame.init()
width = 400
height = 400
center_w = int(width/2)
center_h = int(height/2)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("pygame 이해하기")

startx = 0
running = True
tick = 0
scale = 150.0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    x1 = center_w + scale * math.cos(math.radians(tick))
    y1 = center_h + scale * math.sin(math.radians(tick))

    screen.fill((0, 0, 0))

    print('x1:{}, y1:{}'.format(x1, y1))
    pygame.draw.line(screen, (255, 255, 0), (center_w, center_h), (x1, y1), 6)

    pygame.display.update()

    tick += 1
    time.sleep(0.05)


print('메인루프 종료')
pygame.quit()

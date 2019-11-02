##################################################
# pygame - 화면에 커지고 작아지는 사각형 그리기
#
# 참고 사이트 
# https://pygame.org
# https://pygame.org/docs/
##################################################

import pygame
import sys
import time

width = 400
height = 400

# 초기화 작업
# 반드시 주어진 함수이름과 순서를 지켜야 함.

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("pygame 이해하기")

running = True
w = int(width/2)
h = int(height/2)
dx = 5
dy = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), (0, 0, width-w, height-h))
    pygame.draw.rect(screen, (0, 255, 0), (w, 0, width-w, height-h))
    pygame.draw.rect(screen, (0, 0, 255), (0, w, width-w, height-h))
    pygame.draw.rect(screen, (255, 255, 0), (w, h, width-w, height-h))

    pygame.display.update()
    
    w +=dx
    if w > width or w < 0:
        dx = dx * (-1)
    h +=dy
    if h > height or h < 0:
        dy = dy * (-1)
    time.sleep(0.1)

print('메인루프 종료')
pygame.quit()

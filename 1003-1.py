##################################################
# pygame - 화면에 그리기
#
# 참고 사이트 
# https://pygame.org
# https://pygame.org/docs/
##################################################

import pygame
import sys
import time

# 초기화 작업
# 반드시 주어진 함수이름과 순서를 지켜야 함.

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("pygame 이해하기")

x1 = 0
y1 = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))

    pygame.draw.line(screen, (0, 0, 255), (60, 60), (120, 60), 4)
    pygame.draw.line(screen, (255, 0, 0), (10, 10), (60, 60), 10)
    pygame.draw.rect(screen, (0, 255, 0), (x1, y1, 30, 30), 2)

    pygame.display.update()
    
    x1 +=1
    y1 +=1
    time.sleep(0.1)

print('메인루프 종료')
pygame.quit()

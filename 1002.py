##################################################
# pygame - 키보드 이벤트 이해
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

# 1.pygame 라이브러리를 초기화 함. 
pygame.init()

# 2.디스플레이의 크기를 세팅하고 화면(screen)을 리턴받음. 이 때 화면에 그리기를 할 때마다 screen을 사용합니다.
#     (400, 300)과 같이 화면의 가로 크기와 세로 크기를 tuple로 전달합니다.
screen = pygame.display.set_mode((400, 300))

# 3.화면의 제목에 캡션을 달아 줍니다.
pygame.display.set_caption("pygame 이해하기")

running = True
while running:
    # 화면의 X(닫기)를 누르면 빠져나가기를 해야 함.
    # 아래의 키보드 이벤트를 체크하는 루틴이 없으면 화면의 X를 눌러도 윈도우가 반응을 하지 않음.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 위 2번에서 리턴받은 screen을 사용합니다. 
    #   screen, color, 시작좌표, 종료좌표, 굵기 
    #   참고 사이트 : pygame.org/docs
    pygame.draw.line(screen, (0, 0, 255), (0, 60), (200, 60), 4)
    pygame.draw.line(screen, (255, 0, 0), (0, 0), (200, 300), 4)

    pygame.display.update()
    
    time.sleep(0.1)

print('메인루프 종료')
pygame.quit()

##################################################
# pygame 을 이해하기 위한 가장 짧은 코드 
##################################################

import pygame
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("pygame 이해하기")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.draw.line(screen, (0, 0, 255), (60, 60), (120, 60), 4)

    pygame.display.update()

    
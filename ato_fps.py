""" fps_test1.py """
import sys
import pygame
from pygame.locals import QUIT
import timeit

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))

def main():
    """ main routine """
    sysfont = pygame.font.SysFont(None, 36)
    counter = 0
    time_ellapsed = 0
    fps = 0
    while True:
        start = timeit.default_timer()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        counter += 1
        SURFACE.fill((0, 0, 0))

        #count_image = sysfont.render("count: {}".format(counter), True, (225, 225, 225))
        count_image = sysfont.render("FPS: {}".format(fps), True, (225, 225, 225))
        SURFACE.blit(count_image, (50, 50))
        pygame.display.update()

        end = timeit.default_timer()
        time_delta = end - start
        time_ellapsed += time_delta    

        if time_ellapsed > 1.0000 :
            time_ellapsed = 0
            fps = counter
            counter = 0

if __name__ == '__main__':
    main()

import pygame
from pygameWindow import *
from settings import *
from pygame.locals import *
import sys

def Pygame():
    pygame.init()

    screen = pygame.display.set_mode((W, H))

    img = pygame.image.load('geek2.jpg').convert()
    img_rect = img.get_rect(center = (Half_W, Half_H))

    screen.blit(img, img_rect)
    pygame.display.update()

    scale = pygame.transform.scale(img, (img.get_width() // 1, img.get_height() // 1))
    rect = scale.get_rect(center = (Half_W, Half_H))

    screen.blit(scale, rect)
    pygame.display.update(rect)

    running = True
    moving = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 3:
                    moving = True
                    if rect.collidepoint(event.pos):
                        moving = True
                if event.button == 4:
                    ratio = ratio + 0.1
                    try:
                        scale = pygame.transform.scale(img, (img.get_width() // ratio, img.get_height() // ratio))
                    except:
                        ratio = 0
                
                if event.button == 5:
                    ratio = ratio - 0.1
                    try:
                        scale = pygame.transform.scale(img, (img.get_width() // ratio, img.get_height() // ratio))
                    except:
                        ratio = 0

            elif event.type == MOUSEBUTTONUP:
                moving = False

            elif event.type == MOUSEMOTION and moving:
                if rect.centerx >= W:
                    rect.centerx = W-1
                elif rect.centerx <= 0: 
                    rect.centerx = 1

                if rect.centery >= H:
                    rect.centery = H-1
                elif rect.centery <= 0:
                    rect.centery = 1

                else:
                    rect.move_ip(event.rel)

        screen.fill(BG_COLOR1)
        screen.blit(scale, rect)

        pygame.display.update()
    pygame.quit()






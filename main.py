import pygame
from settings import *
from pygame.locals import *
import sys

# Take colors input
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Construct the GUI game
pygame.init()

# Set dimensions of game GUI

screen = pygame.display.set_mode((W, H))

# Take image as input
img = pygame.image.load('geek2.jpg')
img.convert()

# Draw rectangle around the image
rect = img.get_rect()
rect.center = Half_W, Half_H

# Set running and moving values
running = True
moving = False

# Setting what happens when game
# is in running state
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        # Making the image move
        elif event.type == MOUSEBUTTONDOWN:
            moving = True
            if rect.collidepoint(event.pos):
                moving = True

        # Set moving as False if you want
        # to move the image only with the
        # mouse click
        # Set moving as True if you want
        # to move the image without the
        # mouse click
        elif event.type == MOUSEBUTTONUP:
            moving = False

        # Make your image move continuously
        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)

    # Set screen color and image on screen
    screen.fill(BLACK)
    screen.blit(img, rect)

    # Construct the border to the image
    pygame.draw.rect(screen, BLUE, rect, 2)

    # Update the GUI pygame
    pygame.display.update()

# Quit the GUI game
pygame.quit()
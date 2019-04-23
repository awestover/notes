import pygame
from pygame.locals import *

im=pygame.image.load("test.png")

screen_dims = (800,800)
screen_color = (0,10,100)

pygame.init()
window = pygame.display.set_mode(screen_dims, RESIZABLE)

running = True

def drawPt(x, y):
    window.blit(im, (x,y))

while running:
    window.fill(screen_color)
    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pos = (100,100)
    drawPt(*pos)
    pygame.display.flip()
#! /usr/bin/python
import sys, pygame, time
pygame.init()
size = width, height = 640, 480
black = 0, 0, 0

screen = pygame.display.set_mode(size)

while True:        
    screen.fill(black)
    #screen.blit(ball, ballrect)
    pygame.display.flip()

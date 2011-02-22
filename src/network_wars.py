#! /usr/bin/python
import sys, pygame
import network
import time
from math import floor
import thread

pygame.init()
size = width, height = 640, 480
black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(size)

node_img = pygame.image.load('media/images/node.png')
node_rect = node_img.get_rect()
thread.start_new_thread(network.network.input_loop,())
t = time.time()
i=0
while True:    
    if time.time() - t > 1:
        print('fps: %s'%i)
        t=time.time()
        i=0
    i += 1
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = floor(event.pos[0]/10), floor(event.pos[1]/10)
            network.network.get_info_on_node(x, y)

    for node in network.network.nodes:
        node.balance()
        screen.blit(node_img, pygame.Rect(node.x*10, node.y*10, 10, 10))
    pygame.display.flip()

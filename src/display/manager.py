import pygame
import time
import thread
from math import floor
import sys

import network
import ui

# Setup Variables
dirty_rects = []
total_frames = 0
start_time = time.time()
## Colors

# Load Settings (constants for now)
size = width, height = 640, 480

# Setup Window and Media
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Network Wars')
screen.fill((0,160,8))
pygame.display.flip()

# Imports after pygame.init()
import media.loader
import display.pipes

def calc_fps():
    '''Calculate the FPS the game is going through'''
    global start_time, total_frames
    if time.time() - start_time > 1:
        print('Avg FPS: %s' % (total_frames/(time.time() - start_time)))
        total_frames = 0
        start_time = time.time()

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ui.handle_click(event.pos[0], event.pos[1])
#            network.network.get_info_on_node(x, y)

def draw_node(node):
    '''Draw all the nodes to the screen'''
    rect = pygame.Rect(node.x*10, node.y*10, 10, 10)
    screen.blit(media.loader.node_img, rect)
    add_dirty_rect(rect)

def add_dirty_rect(rect):
    dirty_rects.append(rect)

def loop():
    '''Main game rendering loop'''
    global total_frames, dirty_rects
    total_frames += 1
    calc_fps()
    handle_events()
    network.network.balance_nodes()
    pygame.display.update(dirty_rects)
    dirty_rects = []
    pygame.time.delay(int(1000 * 1.0/40))

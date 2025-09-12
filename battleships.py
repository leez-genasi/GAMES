import copy
import time
import pygame
import random

win_x = 1080
win_y = 720

grid_no = 10
grid_size = 40 # 400 * 400

border_btw = grid_size * 2 # 80
border_side = (win_x - (grid_size * grid_no * 2) - border_btw) // 2 # 100 from each side
border_up = (win_y - (grid_size * grid_no)) // 2

# colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255, 255, 0)
pink = pygame.Color(255, 0, 255)


# board
class Tile():
    def __init__(self, x, y, width):
        self.rect = pygame.Rect(x, y, width, width)

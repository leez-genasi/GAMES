import copy
import time
import pygame
import random

win_x = 720
win_y = 480
fps = pygame.time.Clock()

grid_no = 10
grid_size = 40   # 400 * 400

border_side = (win_x-(grid_no*grid_size))//2
border_up = (win_y-(grid_no*grid_size))//2

# colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255, 255, 0)
pink = pygame.Color(255, 0, 255)

# board
'''class Tile:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
    def render(self, game_win, grid_color):
        pygame.draw.rect(game_win, grid_color, self.rect)
'''

# init
mines = [ [0] * grid_no for n in range(grid_no)]
count = copy.deepcopy(mines) # number of mines surrounding a box (min0, max8)

flag = [ [None] * grid_no for n in range(grid_no)] # flag (1), mine (-1), open (0), or unknown (None)
board = copy.deepcopy(flag)
# for i in range(grid_no): print(i, count[i]) # check array

# setting mines
'''
Mine Rules:
Maximum of 8 mines around an empty block
Won't have 9 mines in a 3*3 block
'''
lower_rand = int((grid_no**2) * 0.12)
upper_rand = int((grid_no**2) * 0.20)
mine_no = random.randrange(lower_rand, upper_rand)
# print(f"{lower_rand}, {upper_rand}, {mine_no}")

for i in range(mine_no):
    while True:
        y = random.randrange(0, grid_no)
        x = random.randrange(0, grid_no)
        if mines[y][x] != 1:
            mines[y][x] = 1
            # print(f"{x}, {y}")
            for i in range(-1, 2):
                if y+i == grid_no or y+i < 0: continue
                for j in range(-1, 2):
                    if x+j == grid_no or x+j < 0: continue
                    if j == 0 and i == 0: continue
                    count[y+i][x+j]+=1
            break

for i in range(len(mines)):
    print(mines[i])

print()

for i in range(len(count)):
    print(count[i])
pygame.init()
game_win = pygame.display.set_mode((win_x, win_y))
pygame.display.set_caption('Minesweeper')


# flag[0][0]=0


def check_adjacent(x, y):
    for row in range(-1, 2):
        if x+row < 0 or x+row > grid_no-1: continue
        for col in range(-1, 2):
            if y + col < 0 or y + col > grid_no - 1: continue
            elif row == 0 and col == 0: continue

            if flag[x+row][y+col] is None: flag[x+row][y+col] = 0 # open

def draw_grid():
    for pos_x in range(border_side, (win_x-border_side), grid_size):
        for pos_y in range(border_up, (win_y-border_up), grid_size):
            # pygame.rect(pos_x, pos_y, size_x, size_y)
            x = (pos_x-border_side)//grid_size
            y = (pos_y-border_up)//grid_size
            if flag[x][y] == 0: # open: check adj empty cells + print number
                grid_color = yellow
                board[x][y] = pygame.Rect(pos_x, pos_y, grid_size, grid_size)
                pygame.draw.rect(game_win, grid_color, board[x][y])

                no_mines = count[y][x]
                if no_mines == 0: check_adjacent(x, y)
                font = pygame.font.SysFont('Times New Roman', 20)
                surface = font.render(f"{no_mines}", True, black)
                rect = surface.get_rect()
                rect.center = board[x][y].center
                game_win.blit(surface, rect)
            else:
                if flag[x][y] == 1: grid_color = pink # flag
                elif (x+y)%2 == 0: grid_color = blue
                else: grid_color = green
                board[x][y] = pygame.Rect(pos_x, pos_y, grid_size, grid_size)
                pygame.draw.rect(game_win, grid_color, board[x][y])

run = True

def game_over():
    font = pygame.font.SysFont('Times New Roman', 50)
    surface = font.render('Kaboom!', True, black)

    bg_rect = pygame.Rect(0, 0, 500, 75)
    bg_rect.midtop = (win_x//2, win_y//3)

    text_rect = surface.get_rect()
    text_rect.center = bg_rect.center
    pygame.draw.rect(game_win, red, bg_rect)


    for i in range(len(mines)):
        for j in range(len(mines[i])):
            if mines[i][j] == 1:
                flag[i][j] == 0
    game_win.blit(surface, text_rect)

    run = False
    return run

def game_over_win():
    font = pygame.font.SysFont('Times New Roman', 50)
    surface = font.render('Win!', True, black)

    bg_rect = pygame.Rect(0, 0, 500, 75)
    bg_rect.midtop = (win_x//2, win_y//3)

    text_rect = surface.get_rect()
    text_rect.center = bg_rect.center
    pygame.draw.rect(game_win, green, bg_rect)

    game_win.blit(surface, text_rect)
    run = False
    return run


game_win.fill(black)
draw_grid()
while run:
    game_win.fill(black)
    draw_grid()

    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(0, len(board)):
                for j in range(0, len(board[i])):
                    board_rect = board[i][j]
                    if board_rect.collidepoint(mouse_pos):
                        if event.button == 1: # lclick to open
                            if mines[j][i] == 1:
                                run = game_over()
                            elif flag[i][j] is None: flag[i][j] = 0
                        if event.button == 3: # rclick to flag
                            if flag[i][j] is None:
                                flag[i][j] = 1
                            elif flag[i][j] == 1:
                                flag[i][j] = None

    flag_count = 0
    for i in range(len(flag)):
        for j in range(len(flag[i])):
            if flag[i][j] == 0: flag_count+=1

    if flag_count == (grid_no**2)-mine_no:
        print("G/W triggered")
        run = game_over_win()

    pygame.display.flip()
    fps.tick(15)

time.sleep(2)
pygame.quit()
quit()

'''
TO DO:
[0] print numbers when tile is clicked
[0] check and open adjacent empty tiles
[o] prevent editing of flag[] once opened
[o] g/o condition
[ ] g/w condition (need to refine)

[ ] animate mine exploding game over
'''
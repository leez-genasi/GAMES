'''
TO LEARN:
border of game (ie game area with a border around it)
mouse click
snake game
minesweeper
image?
mouse click on surface/rect
'''


import pygame

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)

win_x = 720
win_y = 480

sq_x, sq_y = 0, 0

game_win = pygame.display.set_mode((win_x, win_y))
pygame.init()

def draw_grid():
    # drawing grids
    grid_size = 40
    # grid_surface = pygame.Surface(grid_size, grid_size)
    for x in range(0, win_x, grid_size):
        for y in range(0, win_y, grid_size):
            # pygame.Rect(pos_x, pos_y, size_x, size_y)
            rect = pygame.Rect(x, y, grid_size, grid_size)

            # pygame.draw.rect(surface to draw on, color, rect to draw, border width)
            pygame.draw.rect(game_win, white, rect, 1)
def draw_sq():
    sq_size = 40
    rect = pygame.Rect(sq_x, sq_y, sq_size, sq_size)
    game_win.fill(black)
    draw_grid()
    pygame.draw.rect(game_win, red, rect)
    pygame.draw.rect(game_win, white, rect, 1)


game_win.fill(black)
draw_grid()
pygame.display.update()
head = [0, 240]
body = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN: # when key is pressed
            if event.key == pygame.K_ESCAPE: # when esc is pressed, quit
                pygame.quit()
                quit()
                '''
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                print("down")
                sq_y += 40
                if sq_y > win_y-40: sq_y = win_y-40
                draw_sq()
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                print("up")
                sq_y -= 40
                if sq_y < 0: sq_y = 0
                draw_sq()
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                print("left")
                sq_x -= 40
                if sq_x < 0: sq_x = 0
                draw_sq()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                print("right")
                if sq_x > win_x: sq_x = win_x
                sq_x += 40
                if sq_x > win_x-40: sq_x = win_x-40
                draw_sq()
                '''
            pygame.display.update()

    body.append(list(head))
    if len(body) > 5: body.pop()
    print(len(body))
    print(body)
    game_win.fill(black)
    draw_grid()
    for i in range(len(body)):
        pos = body[i]
        pygame.draw.rect(game_win, white,
                         pygame.Rect(pos[0], pos[1], 40, 40))
    if head[0] == 720: break

    head[0]+=40

    pygame.display.update()
    pygame.time.Clock().tick(5)
import pygame, time, random

snake_spd = 15

win_x = 720
win_y = 480

# colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# init win
pygame.init()
game_win = pygame.display.set_mode((win_x, win_y))
score = 0

# init snake
snake_pos = [100, 50] # snake_pos[x][y]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

directn = 'RIGHT'
change_to_dir = directn

fruit_pos = [random.randrange(1, win_x)//10 * 10,
             random.randrange(1, win_y)//10 * 10]
fruit_spawn = True
# scoreboard
def Score(color, font, size):
    font = pygame.font.SysFont(font, size)
    surface = font.render('Score: '+ str(score), True, color)
    rect = surface.get_rect()
    game_win.blit(surface, rect)

# game over
def GameOver():
    font = pygame.font.SysFont('Times New Roman', 50)
    surface = font.render('Final Score: '+ str(score), True, red)
    rect = surface.get_rect()
    rect.midtop = (win_x//2, win_y//4)
    game_win.blit(surface, rect)
    pygame.display.flip()

    # after time, quit
    time.sleep(2)
    pygame.quit()
    quit()

while True:
    # keyboard input
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                change_to_dir = 'DOWN'
            if event.key == pygame.K_UP:
                change_to_dir = 'UP'
            if event.key == pygame.K_LEFT:
                change_to_dir = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to_dir = 'RIGHT'
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

    # changing snake directn
    if change_to_dir == 'DOWN' and directn != 'UP':
        directn = change_to_dir
    if change_to_dir == 'LEFT' and directn != 'RIGHT':
        directn = change_to_dir
    if change_to_dir == 'UP' and directn != 'DOWN':
        directn = change_to_dir
    if change_to_dir == 'RIGHT' and directn != 'LEFT':
        directn = change_to_dir

    # moving snake head
    if directn == 'DOWN':
        snake_pos[1]+=10
    if directn == 'LEFT':
        snake_pos[0]-=10
    if directn == 'UP':
        snake_pos[1]-=10
    if directn == 'RIGHT':
        snake_pos[0]+=10

    # snake and fruit collision
    snake_body.insert(0, list(snake_pos))

    print(fruit_pos)
    if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
        score+=10
        fruit_spawn = False
    else:
        snake_body.pop(-1)

    if not fruit_spawn:
        fruit_pos = [random.randrange(1, win_x) // 10 * 10,
                     random.randrange(1, win_y) // 10 * 10]
        fruit_spawn = True
    game_win.fill(black)

    # drawing snake body
    for body in snake_body:
        pygame.draw.rect(game_win, green,
                         pygame.Rect(body[0], body[1], 10, 10))
    # drawing fruit
    pygame.draw.rect(game_win, white,
                     pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))

    # G/O cons
    if snake_pos[0] < 0 or snake_pos[0] > (win_x-10): GameOver()
    if snake_pos[1] < 0 or snake_pos[1] > (win_y-10): GameOver()
    for body in snake_body[1:]:
        if body[0] == snake_pos[0] and body[1] == snake_pos[1]: GameOver()

    # score
    Score(white, 'Times New Roman', 20)

    pygame.display.update()
    pygame.time.Clock().tick(snake_spd)
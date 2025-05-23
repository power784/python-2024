import pygame
import Objects
import Logic
import Graphics

def setup() -> None:
    pygame.init()
    pygame.display.set_caption("Манёвр")
    
def game() -> int:
    score = 0
    player_x_start_pos = 400
    player_y_start_pos = 435
    player_speed = 3
    pygame.mouse.set_visible(False)
    pl = Objects.Player(player_x_start_pos, player_y_start_pos, player_speed)
    f = True
    balls = []
    while f:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                f = False
                flag = False
        pygame.time.delay(10)
        Logic.generate_obstacles(pl, balls)
        Logic.move(balls)
        Graphics.check_user_actions(pl)
        f = Logic.check_collisions(pl, balls)
        score += 1
        Graphics.draw_game_screen(sc, pl, balls, score)
    pygame.mouse.set_visible(True)
    return score

setup()
sc = pygame.display.set_mode([1200, 900])
score = 0
flag = True
last = 0
game_starts = False
while flag:
    button = Graphics.Button(550, 420, 150, 40, [0, 0, 255])
    Graphics.draw_main_screen(sc, score, last, button)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            flag = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            game_starts = button.is_pressed()
    if game_starts:
        last = game()
        score = max(score, last)
        game_starts = False
    pygame.display.flip()
pygame.quit()

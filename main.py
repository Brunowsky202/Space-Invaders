# importing pygame
import pygame

# importing random
import random

# importing random
import math

from pygame import mixer

# initializate pygame
pygame.init()
pygame.mixer.init()

# window size
screen_width = 800
screen_height = 600

# size constant
SIZE = (screen_width, screen_height)

# icon variable
icon = pygame.image.load("Nave humana.png")
pygame.display.set_icon(icon)

# title of the window
pygame.display.set_caption("Space invaders")

# Bg imgage
background_img = pygame.image.load ("space-11099_1280.jpg")
background_img_trans = pygame.transform.scale (background_img, (800,600))
pygame.mixer.music.load("y2mate.com - Música de Super Mario Bros Castillo.wav")
pygame.mixer.music.play(-1)  

# dislay of the window

screen = pygame.display.set_mode(SIZE)

# Player function
player_img = pygame.image.load("Nave humana.png")
player_x = 370
player_y = 480
player_x_change = 0
def player(x,y):
    screen.blit(player_img, (x,y))

# Bg imgage
background_img = pygame.image.load("space-11099_1280.jpg")
background_img_trans = pygame.transform.scale(background_img, (800,600)).convert_alpha()

# dislay of the window
screen = pygame.display.set_mode (SIZE)

# enemy function
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
number_enemies = 6

for item in range(number_enemies):
    enemy_img.append(pygame.image.load("ovni.png"))
    enemy_x.append (random.randint (0,200))
    enemy_y.append (random.randint (0,200))
    enemy_x_change.append (0.3)
    enemy_y_change.append (40)

    def enemy (x,y):
        screen.blit(enemy_img[item], (x,y))

# Bullet function
bullet_img = pygame.image.load ("bala.png")
bullet_x = 0
bullet_y = 500
bullet_state = True
bullet_y_change = 10
bullet_x_change = 0

#score variable
score = 0
score_font = pygame.font.Font ("Valorax-lg25V.otf", 32)
score_font_2 = pygame.font.Font ("Valorax-lg25V.otf", 64)
text_x = 10
text_y = 10

# show text score
def show_text (x,y):
    score_text = score_font.render(f"SCORE: {score}", True, (38, 31, 111) )
    screen.blit (score_text, (x,y))


def fire (x,y):
    global bullet_state
    bullet_state = False
    screen.blit (bullet_img, (x + 16, y + 16))

# Game loop

def is_collision(b_x, b_y, e_x, e_y):
    distance = math.sqrt((e_x - b_x)**2 + (e_y - b_y)**2)
    if distance < 150:
       return True
    else:
        return False

def game_over(x,y):
    go_text = score_font_2.render (f"GAME OVER", True, (38, 31, 111))
    screen.blit(go_text,(x,y))
    go_sound = mixer.Sound ("y2mate.com - Game Over The Legend of Zelda Ocarina of Time.wav")
    go_sound.play ()
    mixer.music.set_volume(0.2)
    
running = True
while running == True:
    for event in pygame.event.get():
        # Event to close the window
        if event.type == pygame.QUIT:
            running = False
        # Player movements
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player_x_change = -0.5

            if event.key == pygame.K_d:
                player_x_change = 0.5

            if event.key == pygame.K_SPACE and bullet_state == True:
                bullet_x = player_x
                bullet_sound = mixer.Sound ("086553_bullet-hit-39853.wav")
                bullet_sound.play()
                bullet_state = False

            if event.key == pygame.K_ESCAPE:
                screen = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player_x_change = 0

            if event.key == pygame.K_d:
                player_x_change = 0

    # Background blit
    screen.blit (background_img_trans, (0,0))

    for item in range (number_enemies):
        if enemy_y[item] > 350:
            for j in range (number_enemies):
                enemy_y[j] = 2000
            game_over(190,255)

        enemy_x[item] += enemy_x_change[item]
        if enemy_x[item] <= 0:
            enemy_x_change[item] = 0.3
            enemy_y[item] += enemy_y_change[item]
        if enemy_x[item] >= 736:
            enemy_x_change[item] = -0.3
            enemy_y[item] += enemy_y_change[item]

        collision = is_collision (bullet_x, bullet_y, enemy_x[item], enemy_y[item])

        if collision:
            bullet_state = True
            bullet_y = 480
            score += 50
            enemy_x[item] = random.randint (0,200)
            enemy_y[item] = random.randint (0,200)
            collision_sound = mixer.Sound ("y2mate.com - Explosion sonido efecto.wav")
            collision_sound.play()
        
        enemy (enemy_x[item], enemy_y[item])
        show_text (text_x, text_y)

    # Bullet blit
   
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = True 

    if bullet_state == False:
        fire(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    # player movements
    player_x += player_x_change 

    if player_x >= 736:
        player_x = 736
    if player_x <= 0:
        player_x = 0
    
    # Player blit
    player(player_x,player_y)

    pygame.display.update()
pygame.quit()


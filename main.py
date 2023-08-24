# importing pygame
import pygame

# importing random
import random

# importing random
import math

# initializate pygame
pygame.init()

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
background_img = pygame.image.load("eclipse-1492818_1280.jpg")
background_img_trans = pygame.transform.scale(background_img, (800,600))
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
background_img = pygame.image.load("eclipse-1492818_1280.jpg")
background_img_trans = pygame.transform.scale(background_img, (800,600))
# dislay of the window
screen = pygame.display.set_mode (SIZE)

# enemy function
enemy_img = pygame.image.load("ovni.png")
enemy_x = random.randint (0,200)
enemy_y = random.randint (0,200)
enemy_x_change = 0.3
enemy_y_change = 40
def enemy (x,y):
    screen.blit(enemy_img, (x,y))

# Bullet function

bullet_img = pygame.image.load ("bala.png")
bullet_x = 0
bullet_y = 480
bullet_state = True
bullet_y_change = 10
bullet_x_change = 0

def fire (x,y):
    global bullet_state
    bullet_state = False
    screen.blit (bullet_img, (x + 16, y + 16))   

# Game loop

def is_collision(b_x, b_y, e_x, e_y):
    distance = math.sqrt((e_x - b_x)**2 + (e_y - b_y)**2)
    if distance < 27:
       return True
    else:
        return False


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
                bullet_state = False

            if event.key == pygame.K_ESCAPE:
                screen = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player_x_change = 0

            if event.key == pygame.K_d:
                player_x_change = 0
    
    enemy_x += enemy_x_change
    if enemy_x <= 0:
        enemy_x_change = 0.3
        enemy_y += enemy_y_change
    if enemy_x >= 736:
        enemy_x_change = -0.3
        enemy_y += enemy_y_change


    # Background blit
    screen.blit(background_img_trans, (0,0))

    # Bullet blit
    collision = is_collision (bullet_x, bullet_y, enemy_x, enemy_y)

    if collision:
        bullet_state = True
        bullet_y = 480
        enemy_x = random.randint (0,200)
        enemy_y = random.randint (0,200)

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
    enemy (enemy_x, enemy_y)

# Enemy blit

    pygame.display.flip()
pygame.quit()


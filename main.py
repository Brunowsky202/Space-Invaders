# importing pygame
import pygame

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
screen = pygame.display.set_mode(SIZE)

# enemy function
enemy_img = pygame.image.load("ovni.png")
enemy_x = 370
enemy_y = 75
enemy_x_change = 0
def enemy (x,y):
    screen.blit(enemy_img, (x,y))

# Game loop

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

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player_x_change = 0

            if event.key == pygame.K_d:
                player_x_change = 0

    # Background blit
    screen.blit(background_img_trans, (0,0))

    # player movements
    player_x += player_x_change 

    if player_x >= 736:
        player_x = 736
    if player_x <= 0:
        player_x = 0

    
    # Player blit
    player(player_x,player_y)
    enemy (enemy_x, enemy_y)


    pygame.display.flip()
pygame.quit()

import pygame
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))
#screen.fill((150,150,150))
pygame.display.set_caption('invaders Game')

# Player
playerImg = pygame.image.load('player.png')
playerX,playerY = 370, 480
playerX_change = 0

# mixer.Sound('laser.wav').play()

def player(x, y):
    screen.blit(playerImg, (x,y))

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.5
            #if event.key == pygame.K_SPACE:
                #if bullet_state is 'ready':
                #  bulletX = playerX
                #  fire_bullet(bulletX, bulletY)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    player(playerX, playerY)

    pygame.display.update()
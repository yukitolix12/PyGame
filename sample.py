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

    playerX += 1.5
    player(playerX, playerY)

    pygame.display.update()
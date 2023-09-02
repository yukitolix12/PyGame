import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
screen.fill((150,150,150))
pygame.display.set_caption('invaders Game')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
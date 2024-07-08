import pygame
from os.path import join
from random import randint

# * general setup
pygame.init()
pygame.display.set_caption('Space Shooter')

WINDOW_WIDTH = 1280 
WINDOW_HEIGHT = 720

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True

# * plain surface
# surface = pygame.Surface((100, 200))

# * importing spaceship
path = join('images', 'player.png')
player = pygame.image.load(path).convert_alpha()

# * importing star
path = join('images', 'star.png')
star = pygame.image.load(path).convert_alpha()
star_position = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

while running:
    # * event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # * draw the game 

    display_surface.fill('black')

    for i in star_position:
        display_surface.blit(star, i)

    display_surface.blit(player, (100,200))

    pygame.display.update()



pygame.quit()
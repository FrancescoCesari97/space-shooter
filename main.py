import pygame

# * general setup
pygame.init()
pygame.display.set_caption('Space Shooter')

WINDOW_WIDTH = 1280 
WINDOW_HEIGHT = 720

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True

# * surface
surface = pygame.Surface((100, 200))

while running:
    # * event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # * draw the game 

    display_surface.fill('darkgray')
    display_surface.blit(surface, (100,200))
    pygame.display.update()



pygame.quit()
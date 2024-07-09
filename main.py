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

clock = pygame.time.Clock()

# * plain surface
# surface = pygame.Surface((100, 200))

# * importing spaceship
path = join('images', 'player.png')
player = pygame.image.load(path).convert_alpha()
player_rect = player.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_direction = pygame.math.Vector2()
player_speed = 300

# * importing star
path = join('images', 'star.png')
star = pygame.image.load(path).convert_alpha()
star_position = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]


# * importing metor
path = join('images', 'meteor.png')
meteor = pygame.image.load(path).convert_alpha()
meteor_position = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]
meteor_rect = meteor.get_frect(center = (WINDOW_WIDTH / 4, WINDOW_HEIGHT / 4))

# * importing laser
path = join('images', 'laser.png')
laser = pygame.image.load(path).convert_alpha()
laser_position = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]
laser_rect = laser.get_frect(center = (WINDOW_WIDTH / 3, WINDOW_HEIGHT / 3))


while running:
    # * framerate
    dt = clock.tick() / 1000
    # print(dt)
    # * event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # * player movement
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
        #     print(1)
        # if event.type == pygame.MOUSEMOTION:
        #     player_rect.center = event.pos

    # * input 
    keys = pygame.key.get_pressed()
    player_direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
    player_direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
    player_direction = player_direction.normalize() if player_direction else player_direction #*->to make the diagolan movement the same speed
    print((player_direction * player_speed).magnitude())
    # if keys[pygame.K_d]:
    #     player_direction.x = 1
    # else:
    #     player_direction.x = 0

    player_rect.center += player_direction * player_speed * dt

    # * draw the game 
    display_surface.fill('black')

    for i in star_position:
        display_surface.blit(star, i)

    display_surface.blit(meteor, i)

    display_surface.blit(laser, laser_rect )


    # * static player movement
    # if player_rect.bottom >= WINDOW_HEIGHT:
    #     player_rect.bottom = WINDOW_HEIGHT
    #     player_direction.y = -1
    # if player_rect.top <= 0:
    #     player_rect.top = 0
    #     player_direction.y = 1
    # if player_rect.right >= WINDOW_WIDTH:
    #     player_rect.right = WINDOW_WIDTH
    #     player_direction.x = -1
    # if player_rect.left <= 0:
    #     player_rect.left = 0
    #     player_direction.x = 1
    # player_rect.center += player_direction * player_spped * dt
    display_surface.blit(player, player_rect)


    pygame.display.update()



pygame.quit()
import pygame
from os.path import join
from random import randint

from pygame.sprite import Group

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.Vector2()
        self.speed = 300

        # * cooldown shoot
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400
    
    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True

    
    def update(self, dt):
        # print('ship is being updated')
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction #*->to make the diagolan movement the same speed
        self.rect.center += self.direction * self.speed * dt
        
        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            Laser(laser, self.rect.midtop, all_sprites)
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()
        
        self.laser_timer()

class Star(pygame.sprite.Sprite):
    
     def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))


class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = pos)
    
    def update(self, dt):
        self.rect.centery -= 400 * dt


# * general setup
pygame.init()
pygame.display.set_caption('Space Shooter')

WINDOW_WIDTH = 1280 
WINDOW_HEIGHT = 720

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True

clock = pygame.time.Clock()



all_sprites = pygame.sprite.Group()
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()

for i in range(20):
    Star(all_sprites, star_surf)

player = Player(all_sprites)



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

# * meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)


while running:
    # * framerate
    dt = clock.tick() / 1000
    # print(dt)
    # * event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            print()

    # * update
    all_sprites.update(dt)

    # * draw the game 
    display_surface.fill('black')

    all_sprites.draw(display_surface)

    pygame.display.update()



pygame.quit()
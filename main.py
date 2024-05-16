import pygame
import random
from spaceship import Ship
from bullet_blue import BlueBullet
from enemyship import EnemyShip
size = (600, 680)
screen = pygame.display.set_mode(size)

pygame.init()
pygame.font.init()

enemy_x = random.randint(0,570)
hp = 100
my_font = pygame.font.SysFont('Arial', 30)
base_hp = my_font.render(str(hp), True, (250, 0, 0))

space_bg = pygame.image.load("spacebg.png")
base = pygame.image.load("base.PNG")
enemy_bullet = pygame.image.load("enemy_bullet.png")
bullet_blue = pygame.image.load("bullet_blue.PNG")
s = Ship(250, 500)
bb = BlueBullet(s.x + 48, s.y)
es = EnemyShip(enemy_x, -50)
run = True
clicked = False
b_bullet_blitted = False
bb_off_screen = False
reseted = False
es_collision_bb = False
es_collision_base = False
off_screen = False
while run:
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_d]:
        if s.x < 510:
            s.move_direction("right")
        else:
            s.x = 509
    if keys[pygame.K_a]:
        if s.x > -10:
            s.move_direction("left")
        else:
            s.x = -9
    if b_bullet_blitted == False:   #so when the bullets not blitted its with the spaceshuttle
        bb = BlueBullet(s.x + 48, s.y)
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True

    if bb.rect.colliderect(es):
        es_collision_bb = True


    if clicked == False:
        bb = BlueBullet(s.x + 48, s.y)
    screen.blit(space_bg, (0, 0))
    screen.blit(s.image, s.rect)
    if clicked == True:
        if off_screen == False or reseted == True: #if the bullet is not past the cords of screen, or looped already
            screen.blit(bb.image, bb.rect)
        b_bullet_blitted = True
        if b_bullet_blitted == True and off_screen == False or reseted == True:
            bb.move()
            screen.blit(bb.image, bb.rect)
    if bb.y < -60:
        off_screen = True
        reseted = True
        clicked = False
        bb = BlueBullet(s.x + 48, s.y)
    if es.y > 570:
        es_collision_base = True
    if es_collision_bb == False and es_collision_base == False:
        es.move()
        screen.blit(es.image, es.rect)
    if es_collision_base == True or es_collision_bb == True:
        if es_collision_base == True:
            hp = hp - 10
        if es_collision_bb == True:
            es.delta = es.delta + 1.5
        enemy_x = random.randint(0,570)
        es = EnemyShip(enemy_x, -70)
        es_collision_base = False
        es_collision_bb = False



    screen.blit(base, (-130, 600))
    my_font = pygame.font.SysFont('Arial', 30)
    base_hp = my_font.render(str(hp), True, (255, 0, 0))
    screen.blit(base_hp, (286, 625))

    pygame.display.update()


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()


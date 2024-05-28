import pygame
import random
import time
from spaceship import Ship
from bullet_blue import BlueBullet
from enemyship import EnemyShip
from start_button import Start
from boss_ship import BossShip
size = (600, 680)
screen = pygame.display.set_mode(size)

pygame.init()
pygame.font.init()


enemy_x = random.randint(0,570)
hp = 100
bs_hp = 100
my_font = pygame.font.SysFont('agencyfb', 30)
base_hp = my_font.render(str(hp), True, (250, 0, 0))

space_bg = pygame.image.load("spacebg.PNG")
base = pygame.image.load("base.png")
enemy_bullet = pygame.image.load("enemy_bullet.png")
bullet_blue = pygame.image.load("bullet_blue.PNG")
boss_incoming = pygame.image.load("bossincoming.png")

bs = BossShip(90,-400)
s = Ship(250, 500)
bb = BlueBullet(s.x + 48, s.y)
es = EnemyShip(enemy_x, -50)
start = Start(160, 400)

bs_appear_start = random.randint(1, 10)
boss_incoming_time = bs_appear_start - 2

run = True
clicked = False
b_bullet_blitted = False
bb_off_screen = False
reseted = False
es_collision_bb = False
es_collision_base = False
off_screen = False
game_start = False
game_end = False
game_already_started = False  #to fix gligthc of time restarting
print(pygame.font.get_fonts())

while run:
    keys = pygame.key.get_pressed()  # checking pressed keys
    if game_start == True and game_end == False:
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
            if game_start == True:
                clicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            if start.rect.collidepoint(event.pos):
                game_start = True
                if game_already_started == False:
                    start_time = time.time()
                game_already_started = True

    if game_start == True:
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
                hp = hp - 20
            enemy_x = random.randint(0,570)
            es = EnemyShip(enemy_x, -70)
            if es_collision_bb == True:
                es.delta = es.delta + 1.5
            es_collision_base = False
            es_collision_bb = False

        current_time = time.time()
        time_pass = current_time - start_time
        time_pass = round(time_pass, 2)
        elapsed_time = my_font.render("Time Passed: " + str(time_pass), True, (255, 0, 0))
        if time_pass > boss_incoming_time and time_pass < bs_appear_start:
            screen.blit(boss_incoming, (30, 100))

        if time_pass > bs_appear_start:
            if bs_hp > 0:
                screen.blit(bs.image, bs.rect)
                bs.move()
            if bs.rect.colliderect(bb):
                bs_hp = bs_hp - 50



        screen.blit(base, (-130, 600))
        my_font = pygame.font.SysFont('agencyfb', 30)
        base_hp = my_font.render(str(hp), True, (255, 0, 0))
        screen.blit(base_hp, (286, 625))
        screen.blit(elapsed_time, (50, 50))

        screen.blit(bs.image, bs.rect)
        print(bs_hp)

    if hp < 1:
        game_end = True

    if game_start == False and game_end == False:
        screen.blit(space_bg, (0, 0))
        screen.blit(start.image, start.rect)
    if game_end == True:
        screen.blit(space_bg, (0, 0))




    pygame.display.update()


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()


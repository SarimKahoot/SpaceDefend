import pygame
from spaceship import Ship
from bullet_blue import BlueBullet
size = (600, 680)
screen = pygame.display.set_mode(size)


space_bg = pygame.image.load("spacebg.png")
base = pygame.image.load("base.PNG")
enemy_bullet = pygame.image.load("enemy_bullet.png")
bullet_blue = pygame.image.load("bullet_blue.PNG")
s = Ship(250, 500)
bb = BlueBullet(s.x + 48, s.y)
run = True
clicked = False
b_bullet_blitted = False
off_screen = False
while run:
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_d]:
        s.move_direction("right")
    if keys[pygame.K_a]:
        s.move_direction("left")
    if b_bullet_blitted == False:
        bb = BlueBullet(s.x + 48, s.y)
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True

    screen.blit(space_bg, (0, 0))
    screen.blit(s.image, s.rect)
    if clicked == True:
        if off_screen == False:
            screen.blit(bb.image, bb.rect)
        clicked == False
        b_bullet_blitted = True
    if b_bullet_blitted == True:
        bb.move()
        screen.blit(bb.image, bb.rect)
    if bb.y < -50:
        off_screen == True
        bb = BlueBullet(s.x + 48, s.y)

    screen.blit(base, (-130, 600))
    pygame.display.update()


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()


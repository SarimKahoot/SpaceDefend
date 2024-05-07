import pygame
from spaceship import Ship

size = (600, 680)
screen = pygame.display.set_mode(size)


space_bg = pygame.image.load("spacebg.png")

s = Ship(300, 680)
run = True

while run:
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_d]:
        s.move_direction("right")
    if keys[pygame.K_a]:
        s.move_direction("left")

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.blit(space_bg, (0, 0))
    screen.blit(s.image, s.rect)
    pygame.display.update()


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()


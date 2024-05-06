import pygame


size = (600, 680)
screen = pygame.display.set_mode(size)


space_bg = pygame.image.load("spacebg.png")

run = True

while run:


    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.blit(space_bg, (0, 0))

    pygame.display.update()


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()


import pygame


class YenemyShip:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("y_enemyship.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 2.5

    def move(self):
        self.y = self.y + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
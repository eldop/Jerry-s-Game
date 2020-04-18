import pygame
from random import choice, randint

class Baloon(pygame.sprite.Sprite):
    def __init__(self, speed):
        pygame.sprite.Sprite.__init__(self)
        listimage = [pygame.image.load('balloon_blue.png'), pygame.image.load('balloon_red.png'), pygame.image.load('balloon_green.png')]
        self.image = choice(listimage)
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, 1720)
        self.rect.y = randint(980, 1280)
        self.speed = speed


    def up(self):
        self.rect.y -= self.speed

    def update(self):
        self.up()

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # a class to rep a single alien

    def __init__(self, ai_settings, screen):
        # init alien and its position
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load alien image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start alien near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store aliens exact pos
        self.x = float(self.rect.x)

    def blitme(self):
        """ draw alien at current location """
        self.screen.blit(self.image, self.rect)

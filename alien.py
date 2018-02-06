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

    def check_edges(self):
        """return true if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """move alien right"""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

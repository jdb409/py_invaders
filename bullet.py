import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    # class to manage bullets fired from ship

    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen

        # create a bullet at (0,0) then correct it
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # move bullet up screen
        # update decimal position of bullet
        self.y -= self.speed_factor
        # update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

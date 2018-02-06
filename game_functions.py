import sys
import pygame

from bullet import Bullet
from alien import Alien


def check_events(ai_settings, screen, ship, bullets):
    # """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # create new bullet and add to group
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    if (len(bullets) < ai_settings.bullets_allowed):
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, aliens, bullets):
    screen.fill(ai_settings.bg_color)

    # redraw all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw()
    pygame.display.flip()


def update_bullets(bullets):
    # update bullet positions
    bullets.update()
    # get rid of bullets that have dissapeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def create_fleet(ai_settings, screen, aliens):
    """create fleet"""
    # create alien and find number of aliens in a row
    # spacing equal to one alien width
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - (alien_width * 2)
    number_aliens_x = (available_space_x/(alien_width * 2))

    for alien_number in range(number_aliens_x):
        # create alien place it in row
        alien = Alien(ai_settings, screen)
        alien.x = alien_width+2 * alien_width*alien_number

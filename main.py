import sys
import time
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import gameevent as ge

def runGame():
    pygame.init()
    # screen = pygame.display.set_mode((1200, 800))
    # pygame.display.set_caption('Alian Invasion')
    # bgColor = (255, 255, 255)
    settings = Settings()
    screen = pygame.display.set_mode((settings.screenWidth, settings.screenHeight))
    pygame.display.set_caption(settings.title)

    ship = Ship(screen)
    # alien = Alien(settings, screen)

    aliens = Group()
    ge.createAlienGroup(settings, screen, aliens)
    bullets = Group()

    # print(ship.rect.centery)
    # print(ship.screenRect.centery)
    while True:
        ge.checkEvents(settings, screen, ship, bullets)
        ship.moveRightOrLeft()
        ge.bulletUpdate(bullets, aliens)
        ge.alienUpdate(settings, ship, aliens)
        if len(aliens) == 0:
            time.sleep(2)
            ge.createAlienGroup(settings, screen, aliens)
        # print(len(bullets))
        ge.freshScreen(settings, screen, ship, bullets, aliens)

def main():
    runGame()

if __name__ == '__main__':
    main()

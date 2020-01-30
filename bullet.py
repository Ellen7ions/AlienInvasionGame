import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, settings, screen, ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, settings.bulletWidth, settings.bulletHeight)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.color = settings.bulletColor
        self.speed = settings.bulletSpeed

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def freshBullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

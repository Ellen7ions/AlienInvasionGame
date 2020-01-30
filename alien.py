import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('src/images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self, dir):
        self.x += self.settings.alienSpeed * dir
        self.rect.x = self.x

    def checkEdge(self):
        screenRect = self.screen.get_rect()
        if self.rect.right >= screenRect.right or self.rect.left <= 0:
            return True
        else:
            return False


if __name__ == '__main__':
    pass
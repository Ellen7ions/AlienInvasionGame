import pygame
class Ship():
    def __init__(self, screen):
        # Pos screen where the ship is
        self.screen = screen
        self.image = pygame.image.load('src/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screenRect = self.screen.get_rect()

        self.rect.centerx = self.screenRect.centerx
        # self.rect.centery = self.screenRect.centery
        self.rect.bottom = self.screenRect.bottom

        self.movingRight = False
        self.movingLeft = False

    def moveRightOrLeft(self):
        if self.movingLeft == True and self.rect.left > 0:
            self.rect.centerx -= 1
        if self.movingRight == True and self.rect.right < self.screenRect.right:
            self.rect.centerx += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)

if __name__ == '__main__':
    pass

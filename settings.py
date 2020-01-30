import pygame

class Settings():
    def __init__(self):
        self.screenWidth = 900
        self.screenHeight = 650
        self.bgColor = (230, 230, 230)
        self.title = 'Alian Invasion'

        self.background = pygame.image.load('src/images/background.bmp')

        self.bulletSpeed = 1
        self.bulletWidth = 5
        self.bulletHeight = 15
        self.bulletColor = (60, 60, 60)
        self.bulletAllowed = 2

        self.alienSpeed = 0.7
        self.alienDirection = 1
        self.alienDropSpeed = 7

if __name__ == '__main__':
    pass

import sys
import pygame

from alien import Alien
from bullet import Bullet
def checkAllEdge(settings, aliens):
    for alien in aliens:
        if alien.checkEdge():
            changeDirection(settings, aliens)
            break

def changeDirection(settings, aliens):
    for alien in aliens:
        alien.rect.y += settings.alienDropSpeed
    settings.alienDirection *= -1

def alienUpdate(settings, ship, aliens):
    checkAllEdge(settings, aliens)
    aliens.update(settings.alienDirection)

    if pygame.sprite.spritecollideany(ship, aliens):
        print('Dead!')

def bulletUpdate(bullets, aliens):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

def fireBullet(settings, screen, ship, bullets):
    if len(bullets) < settings.bulletAllowed:
        newBullet = Bullet(settings, screen, ship)
        bullets.add(newBullet)

def keyDown(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.movingRight = True
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = True
    elif event.key == pygame.K_SPACE:
        fireBullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def keyUp(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.movingRight = False
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = False

# check Keyboard Events
def checkEvents(settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keyDown(event, settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            keyUp(event, ship)
def getCnt(settings, alienWidth):
    availableSpaceX = settings.screenWidth - 2 * alienWidth
    number = int(availableSpaceX / (2 * alienWidth))
    return number

def createAlienGroup(settings, screen, aliens):
    alien = Alien(settings, screen)
    alienWidth = alien.rect.width
    number = getCnt(settings, alienWidth)

    for i in range(number):
        alien = Alien(settings, screen)
        alien.x = alienWidth + 2 * alienWidth * i
        alien.rect.x = alien.x
        aliens.add(alien)

# refreshScreen
def freshScreen(settings, screen, ship, bullets, aliens):
    # Repaint Screen
    # Attation Order

    # background
    screen.blit(settings.background, screen.get_rect())
    # screen.fill(settings.bgColor)

    # bullets
    for bullet in bullets:
        bullet.freshBullet()

    # ships
    ship.blitme()

    # alien
    aliens.draw(screen)

    pygame.display.flip()

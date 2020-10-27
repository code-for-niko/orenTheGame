import pygame
import random
import math


# Iniciar o jogo
pygame.init()

# criar display
screenX = 800
screenY = 600
screen = pygame.display.set_mode((screenX, screenY))

# Background
background = pygame.image.load('background.png')

# Title / Icon
pygame.display.set_caption("O Patrao Da Zona")
icon = pygame.image.load('mafia.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('serial-killer.png')
playerX = 370
playerY = 400
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = pygame.image.load('IMG_2564.png')
enemyX = random.randint(400, 800)
enemyY = random.randint(200, 500)
enemyX_change = 0.3
enemyY_change = 0.3

# Bullet
# Ready - está pronta
# Fire - disparo

bulletImg = pygame.image.load('bullet.png')
bulletX = 370
bulletY = 400
bulletX_change = 5
bulletY_change = 1
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


bullets = []

def displayBullet():
    for bullet in bullets:
        screen.blit(bulletImg, (bullet[0], bullet[1]))
        # HORIZONTAL
        bullet[0] = bullet[0] + bulletX_change
        # VERTICAL
        bullet[1] = bullet[1]


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    bullets.append([x, y])

    """while bullet_state == 'fire':
        if bulletX >= screenX or bulletY >= screenY:
            bullet_state = 'ready'
        elif bulletX == enemyX and bulletY == enemyY:
            bullet_state = 'fire'
        else:
            pygame.draw.circle(screen, (0,0,0), (int(bulletX), int(bulletY)), 6)
            #
            bulletX = bulletX + bulletX_change
            bulletY = bulletY"""
    
        
def reloadWindow():
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    displayBullet()


#def isCollision(enemyX, enemyY, bulletX, bulletY):
    #distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    #if distance < 27:
       # return True
   # else:
      #  return False


    pygame.display.update()

# Loop
running = True
while running:

    # RGB
    screen.fill((73, 73, 73))
    # Background loop
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Movimento
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change = -1.2
            if event.key == pygame.K_DOWN:
                playerY_change = 1.2
            if event.key == pygame.K_LEFT:
                playerX_change = -1.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.2
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, playerY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    score = 0

    playerX += playerX_change
    playerY += playerY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change

    if enemyX <= 0:
        enemy_change = 0.3
        enemyX = 0
    elif enemyX >= 736:
        enemy_change = -0.3
        enemyX = 736


    #collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    #if collision:
        #bulletY = 480
        #bullet_state = "ready"
       # score += 1
        #print(score)
        #enemyX = random.randint(400, 800)
        #enemyY = random.randint(200, 500)

        # Bullet Movement
   # if bullet_state == "fire":
     #   fire_bullet(playerX, bulletX)
      #  bulletX += bulletX_change

    reloadWindow()

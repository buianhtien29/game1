import pygame
import random

pygame.init()

#Kích thước cửa sổ
WIDTH = 700
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game bắn máy bay")

#Màu sắc
WHITE = (255, 255, 255)
Red = (255, 0, 0)
Blue = (0, 0, 255)
Black = (0, 0, 0)

player = pygame.Rect(300, 800 , 50, 50)  # Máy bay của người chơi

bullets = []  # Danh sách đạn

enemies = []  # Danh sách máy bay địch

score = 0  # Điểm số
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(player.x + 18, player.y, 5, 10)
                bullets.append(bullet)

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and player.x > 0:
        player.x -= 5
    if key[pygame.K_RIGHT] and player.x < WIDTH - 40:
        player.x += 5
    
    if random.randint(1,30) == 1:
        enemy = pygame.Rect(random.randint(0, 560), 0, 40, 40)
        enemies.append(enemy)

    for bullet in bullets:
        bullet.y -= 7

    for enemy in enemies:
        enemy.y += 4

    for enemy in enemies :
        if player.colliderect(enemy):
            print("Game Over! Điểm số của bạn là:", score)
            running = False

    for enemy in enemies[:]:
        for bullet in bullets[:]:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 1
                break

    bullets = [b for b in bullets if b.y > 0]

    screen.fill(Black)
                
    pygame.draw.rect(screen, Blue, player)
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)
    for enemy in enemies:
        pygame.draw.rect(screen, Red, enemy)

    score_text = font.render(f"Điểm số: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.update()

pygame.quit()
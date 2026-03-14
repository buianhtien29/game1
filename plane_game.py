import pygame
import random

pygame.init()

#Kích thước cửa sổ
WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game bắn máy bay")

#Màu sắc
WHITE = (255, 255, 255)
Red = (255, 0, 0)
Blue = (0, 0, 255)
Black = (0, 0, 0)

player = pygame.Rect(300, 750, 50, 50)  # Máy bay của người chơi

bullets = []  # Danh sách đạn

enemies = []  # Danh sách máy bay địch

score = 0  # Điểm số
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

running = True
paused = False

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                bullet = pygame.Rect(player.x + 18, player.y, 5, 10)
                bullets.append(bullet)

            if event.key == pygame.K_p:
                paused = not paused
                print("Game Paused" if paused else "Game Resumed")

            if event.key == pygame.K_ESCAPE:
                running = False



    if not paused:

        key = pygame.key.get_pressed()
        speed = 5

        if key[pygame.K_a] :
            player.x -= speed
        if key[pygame.K_d] :
            player.x += speed
        if key[pygame.K_s] :
            player.y += speed
        if key[pygame.K_w] :
            player.y -= speed

        if player.x < 0:
            player.x = 0
        if player.x > 600 - player.width:
            player.x = 600 - player.width
        if player.y < 0:
            player.y = 0
        if player.y > 800 - player.height:
            player.y = 800 - player.height

        for enemy in enemies:
            enemy.y += 4


        for enemy in enemies :
            if player.colliderect(enemy):
                print("Game Over! Điểm số của bạn là:", score)
                running = False

        if random.randint(1,20) == 1:
            enemy = pygame.Rect(random.randint(0, 560), 0, 40, 40)
            enemies.append(enemy)

    pygame.display.update() 

    

    for bullet in bullets:
        bullet.y -= 7
   
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

    if paused:
        text = font.render("PAUSED", True, (255,0,0))
        screen.blit(text,(320,450))

    score_text = font.render(f"Điểm số: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.update()

pygame.quit()
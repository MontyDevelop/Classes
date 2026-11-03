# Importing the lib
import pygame
import random

pygame.init() # Starting the pygame

window = pygame.display.set_mode((500,400)) #Creating a screen
pygame.display.set_caption("AI Pong Game")

# To create a paddle in rectangle shape
player = pygame.Rect(480, 150,15,100)
ai_paddle = pygame.Rect(5, 150, 15, 100)
ball = pygame.Rect(250,200,25,25)


# ball location.
ball_dx = random.choice([-5,5])
ball_dy = random.choice([-5,5])


player_score = 0
ai_score = 0

font = pygame.font.SysFont("Arial", 20)

run = True
clock = pygame.time.Clock()

while run:
    clock.tick(60)
    window.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # player movement up-down
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= 5
    if keys[pygame.K_DOWN] and player.bottom < 400:
        player.y += 5

    # ai movement
    if ai_paddle.centery < ball.centery and ai_paddle.bottom < 400:
        ai_paddle.y += 5
    elif ai_paddle.centery > ball.centery and ai_paddle.top > 0:
        ai_paddle.y -= 5

    # ball movement
    ball.x += ball_dx
    ball.y += ball_dy

    # collision with top and bottom
    if ball.top <=0 or ball.bottom >= 400:
        ball_dy *= -1

    # collision with paddle
    if ball.colliderect(player) or ball.colliderect(ai_paddle):
        ball_dx *= -1

    if ball.left <=0:
        player_score += 1
        ball.center = (250,200)
        ball_dx *= -1

    if ball.right >= 500:
        ai_score += 1
        ball.center = (250,200)
        ball_dx *= -1


    pygame.draw.rect(window, "white",player) # It makes your drawing visible in screen
    pygame.draw.rect(window, "white",ai_paddle) # It makes your drawing visible in screen
    pygame.draw.ellipse(window, "red", ball)


    player_text = font.render(f"Player: {player_score}", True, "white")
    ai_text = font.render(f"AI: {ai_score}", True, "white")
    window.blit(player_text, (400, 20))
    window.blit(ai_text, (20, 20))

    pygame.display.flip()

pygame.quit()






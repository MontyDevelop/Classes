import pygame
import sys

from PIL.FontFile import WIDTH

pygame.init()


# step 1:
# Creating Screen

WIDTH, HEIGHT = 500,500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI PONG GAME")

clock = pygame.time.Clock()
paddle_width, paddle_height = 10, 100
player = pygame.Rect(0, HEIGHT//2 - 50, paddle_width, paddle_height)
ai = pygame.Rect(490, HEIGHT//2 - 50, paddle_width, paddle_height)
ball = pygame.Rect(WIDTH//2, HEIGHT//2, 15,15)

ball_speed_x = 3
ball_speed_y = 3

def player_movement(keys):
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= 7
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += 7


def ai_movement():
    if ai.centery < ball.centery:
        ai.y += 5
    if ai.centery > ball.centery:
        ai.y -= 5

def ball_move():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(player) or ball.colliderect(ai):
        ball_speed_x *= -1


def draw():
    screen.fill('black')
    pygame.draw.rect(screen, "white", player)
    pygame.draw.rect(screen, "red", ai)
    pygame.draw.ellipse(screen, "yellow", ball)
    pygame.display.flip()



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player_movement(keys)
    ball_move()
    draw()
    clock.tick(60)
pygame.quit()
sys.exit()

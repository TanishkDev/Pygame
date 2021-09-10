import pygame
import time
import sys
pygame.init()


def player1_animation():
    player_1.y += p1_speed

    if player_1.top <= 0:
        player_1.top = 0
    if player_1.bottom >= win_height:
        player_1.bottom = win_height


def player2_animation():
    player_2.y += p2_speed

    if player_2.top <= 0:
        player_2.top = 0
    if player_2.bottom >= win_height:
        player_2.bottom = win_height


def ball_animation():
    global ball_speed_x, ball_speed_y, player_1_score, player_2_score

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= win_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= win_width:
        ball_speed_x *= -1

    if ball.colliderect(player_1) or ball.colliderect(player_2):
        ball_speed_x *= -1

    if ball.left <= 0:
        player_2_score += 1
    if ball.right >= 800:
        player_1_score += 1


def over():
    time.sleep(10)
    sys.exit()


basic_font = pygame.font.SysFont("comicsansms", 20)
winner_font = pygame.font.SysFont("comicsansms", 54)


win_width = 800
win_height = 600

dark_blue = (12, 13, 31)
white = (255, 255, 255)
red = (224, 108, 108)

size_x = 10
size_y = 100

clock = pygame.time.Clock()
screen = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Pong!")


player_1 = pygame.Rect(0, win_height/2-50, size_x, size_y)
player_2 = pygame.Rect(800-10, win_height/2-50, size_x, size_y)
ball = pygame.Rect(win_width/2-12.5, win_height/2, 25, 25)

game_over = False

ball_speed_x = 7
ball_speed_y = 7
p1_speed = 0
p2_speed = 0

player_1_score = 0
player_2_score = 0

w = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                p1_speed -= 5
            if event.key == pygame.K_DOWN:
                p1_speed += 5
            if event.key == pygame.K_w:
                p2_speed -= 5
            if event.key == pygame.K_s:
                p2_speed += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                p1_speed += 5
            if event.key == pygame.K_DOWN:
                p1_speed -= 5
            if event.key == pygame.K_w:
                p2_speed += 5
            if event.key == pygame.K_s:
                p2_speed -= 5

    ball_animation()
    player1_animation()
    player2_animation()

    screen.fill(dark_blue)
    pygame.draw.rect(screen, red, player_1)
    pygame.draw.rect(screen, red, player_2)
    pygame.draw.ellipse(screen, red, ball)
    pygame.draw.aaline(screen, red, (win_width/2, 0),
                       (win_width/2, win_height))

    text_p1 = basic_font.render(
        "Player1 Score:"+str(player_1_score), True, red)
    text_p2 = basic_font.render(
        "Player2 Score :"+str(player_2_score), True, red)
    screen.blit(text_p1, (0, 0))
    screen.blit(text_p2, (400, 0))

    if player_2_score >= 5:
        text = winner_font.render("Player 2 won!",True,red)
        screen.blit(text,(350,300))

        

    elif player_1_score >= 5:
        text = winner_font.render("Player 1 won!", True, red)
        screen.blit(text, (300, 300))
       


    pygame.display.flip()
    clock.tick(60)

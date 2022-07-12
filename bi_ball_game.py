import pygame
import sys
import time

pygame.init()
screen_width = 600
screen_height = 400
speed = [1, 1]
BLACK = 0, 0, 0
sleep_time = 5e-5
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("pygame壁球")
ball = pygame.image.load("image/ball.png")
ball_rec = ball.get_rect()
fps = 300
fclock = pygame.time.Clock()




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ball_rec = ball_rec.move(speed[0], speed[1])
    if ball_rec.left < 0 or ball_rec.right > screen_width:
        speed[0] = -speed[0]
    if ball_rec.top < 0 or ball_rec.bottom > screen_height:
        speed[1] = -speed[1]

    # time.sleep(sleep_time)
    screen.fill(BLACK)
    screen.blit(ball, ball_rec)
    pygame.display.update()
    fclock.tick(fps)

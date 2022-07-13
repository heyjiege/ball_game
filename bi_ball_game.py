import pygame
import sys
import time

pygame.init()


# 加入图标
icon = pygame.image.load("image/PYG03-flower.png")
pygame.display.set_icon(icon)

size = screen_width, screen_height = 600, 400


speed = [1, 1]
BLACK = 0, 0, 0
sleep_time = 5e-5




screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
# screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
# screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)
# screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("pygame壁球")
ball = pygame.image.load("image/ball.png")
ball_rec = ball.get_rect()
fps = 300
fclock = pygame.time.Clock()
still = False  # 小球是否 禁止or 移动
bgcolor = pygame.Color("black")  # 背景颜色



def RGBChannel(x):
    """接手一个参数，并返回0-255的一个整数"""
    return 0 if x < 0 else (255 if x > 255 else int(x))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 速度控制
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1) * int(speed[0] / abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) + 1) * int(speed[0] / abs(speed[0]))
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1) * int(speed[1] / abs(speed[1]))
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) + 1) * int(speed[1] / abs(speed[1]))
            elif event.key == pygame.K_ESCAPE:
                sys.exit()

        # 添加窗口大小可调
        elif event.type == pygame.VIDEORESIZE:
            size = screen_width, screen_height = event.size[0], event.size[1]
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)

        # 添加鼠标事件
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                still = True
        elif event.type == pygame.MOUSEBUTTONUP:
            still = False
            if event.button == 1:
                # 移动到鼠标的位置
               ball_rec = ball_rec.move(event.pos[0]-ball_rec.left, event.pos[1]-ball_rec.top)
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0] == 1:
                ball_rec = ball_rec.move(event.pos[0] - ball_rec.left, event.pos[1] - ball_rec.top)

    # 窗口最小化后，停止小球的移动
    if pygame.display.get_active() and not still:
        ball_rec = ball_rec.move(speed[0], speed[1])
    if ball_rec.left < 0 or ball_rec.right > screen_width:
        speed[0] = -speed[0]
        # 球右端超出屏幕 且 球再往右移动， 准备逃离屏幕或在屏幕角落摩擦  --> 让球反向，返回屏幕中
        if screen_width < ball_rec.right < ball_rec.right + speed[0]:
            speed[0] = -speed[0]
    if ball_rec.top < 0 or ball_rec.bottom > screen_height:
        speed[1] = -speed[1]
        if ball_rec.bottom > screen_height and ball_rec.bottom + speed[1] > ball_rec.bottom:
            speed[1] = -speed[1]

    bgcolor.r = RGBChannel(ball_rec.left * 255 / screen_width)
    bgcolor.g = RGBChannel(ball_rec.top * 255 / screen_height)
    bgcolor.b = RGBChannel(min(speed[0], speed[1]) * 255 / max(speed[0], speed[1], 1))
    # time.sleep(sleep_time)

    screen.fill(bgcolor)
    screen.blit(ball, ball_rec)
    pygame.display.update()
    fclock.tick(fps)














import pygame as pg

W = 600
H = 400

BROWN = (59, 24, 11)
GRAY = (194, 194, 194)
YELLOW = (255, 247, 0)
RED = (209, 29, 29)

FPS = 60  # число кадров в секунду

pg.init()
sc = pg.display.set_mode((W, H))
pg.display.set_caption("Класс Surface")
clock = pg.time.Clock()

bg = pg.Surface((W, H))
bg.fill(BROWN)
pg.draw.rect(bg, GRAY, (0, 50, W, 100))
pg.draw.rect(bg, GRAY, (0, 250, W, 100))

ball_1 = pg.Surface((100, 100), pg.SRCALPHA)
ball_1_rect = ball_1.get_rect(topleft=(0, 50))
pg.draw.circle(ball_1, (*YELLOW, 100), (50, 50), 40)
step_1 = 5

ball_2 = pg.Surface((100, 100), pg.SRCALPHA)
ball_2_rect = ball_2.get_rect(topleft=(0, 50))
pg.draw.circle(ball_2, (*RED, 100), (50, 50), 20)
step_2 = 10

x, y = 0, 50
x1, y1 = x, y

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    if ball_1_rect.left <= W and ball_1_rect.top == 50:
        ball_1_rect.right += step_1
    elif ball_1_rect.left > W and ball_1_rect.top == 50:
        ball_1_rect.top += 200
    elif ball_1_rect.right > 0 and ball_1_rect.top == 250:
        ball_1_rect.left -= step_1
    elif ball_1_rect.left < -40 and ball_1_rect.top == 250:
        ball_1_rect.top -= 200

    if ball_2_rect.left < W and ball_2_rect.top == 50:
        ball_2_rect.right += step_2
    elif ball_2_rect.right > W + 40 and ball_2_rect.top == 50:
        ball_2_rect.top = 250
    elif ball_2_rect.right > 0 and ball_2_rect.top == 250:
        ball_2_rect.left -= step_2
    elif ball_2_rect.left < -40 and ball_2_rect.top == 250:
        ball_2_rect.top = 50

    sc.blit(bg, (0, 0))
    sc.blit(ball_1, ball_1_rect)
    sc.blit(ball_2, ball_2_rect)

    pg.display.update()
    clock.tick(FPS)

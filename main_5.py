import pygame as pg

pg.init()

W = 600
H = 400

sc = pg.display.set_mode((W, H))
pg.display.set_caption("Класс Surface")

BROWN = (59, 24, 11)
GRAY = (194, 194, 194)
YELLOW = (255, 247, 0)
RED = (209, 29, 29)

FPS = 60  # число кадров в секунду
clock = pg.time.Clock()

sc.fill(BROWN)

x, y = 0, 50
x1, y1 = x, y

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    bg = pg.Surface((W, H))
    bg.fill(BROWN)
    pg.draw.rect(bg, GRAY, (0, 50, W, 100))
    pg.draw.rect(bg, GRAY, (0, 250, W, 100))

    ball_1 = pg.Surface((100, 100), pg.SRCALPHA)
    pg.draw.circle(ball_1, (*YELLOW, 100), (50, 50), 40)
    if x < W and y == 50:
        x += 5
    elif x >= W and y == 50:
        y = 250
        x -= 5
    elif x > -80 and y == 250:
        x -= 5
    elif x <= -80 and y == 250:
        y = 50
        x += 5


    ball_2 = pg.Surface((100, 100), pg.SRCALPHA)
    pg.draw.circle(ball_2, (*RED, 100), (50, 50), 20)
    if x1 < W and y1 == 50:
        x1 += 10
    elif x1 >= W and y1 == 50:
        y1 = 250
        x1 -= 10
    elif x1 > -80 and y1 == 250:
        x1 -= 10
    elif x1 <= -80 and y1 == 250:
        y1 = 50
        x1 += 10

    sc.blit(bg, (0, 0))
    sc.blit(ball_2, (x1, y1))
    sc.blit(ball_1, (x, y))


    pg.display.update()
    clock.tick(FPS)

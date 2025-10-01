import pygame as pg

FPS = 60
WIN_WIDTH = 900
WIN_HEIGHT = 600
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
screen.fill(WHITE)
pg.display.set_caption("Игра")
clock = pg.time.Clock()

Dx = 2
r = 90
r2 = 140
x = 0
y = 0
pg.draw.ellipse(screen, GREEN, (x, y, r2, r))
pg.display.update()
flag_play = True
while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    if x <= WIN_WIDTH - r2 and y == 0:
        x += Dx

    if x == WIN_WIDTH - r2 and y <= WIN_HEIGHT - r:
        y += Dx

    if x > 0 and y == WIN_HEIGHT - r:
        x -= Dx

    if x == 0 and y > 0:
        y -= Dx

    screen.fill(WHITE)
    pg.draw.ellipse(screen, GREEN, (x, y, r2, r))

    pg.display.update()

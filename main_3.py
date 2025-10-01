import pygame as pg

FPS = 60
WIN_WIDTH = 900
WIN_HEIGHT = 600
WHITE = (255, 255, 255)
GREEN = (40, 168, 48)

pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
screen.fill(WHITE)
pg.display.set_caption("Игра")
clock = pg.time.Clock()

Dx = 2
r = 30
x = 50
y = 50
pg.draw.circle(screen, GREEN, (x, y), r)
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

    if x <= 800 and y == 50:
        x += Dx

    if x == 800 and y <= 500:
        y += Dx

    if x > 50 and y == 500:
        x -= Dx

    if x == 50 and y > 50:
        y -= Dx

    screen.fill(WHITE)
    pg.draw.circle(screen, GREEN, (x, y), r)

    pg.display.update()

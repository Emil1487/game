import pygame as pg

FPS = 60
WIN_WIDTH = 400
WIN_HEIGHT = 100
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)

pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
screen.fill(WHITE)
pg.display.set_caption("Игра")
clock = pg.time.Clock()

Dx = 2
r = 40
x = 1
y = 30
pg.draw.rect(screen, ORANGE, (x, y, r, r))
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

    if x >= WIN_WIDTH - r or x <= 0:
        Dx *= -1
        if Dx > 0:
            Dx += 2
        else:
            Dx -= 2
        # Dx *= 1.15
        x += Dx
    else:
        x += Dx

    screen.fill(WHITE)
    pg.draw.rect(screen, ORANGE, (x, y, r, r))

    pg.display.update()

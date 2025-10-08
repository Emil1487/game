import pygame as pg
import random

FPS = 60
WIDTH, HEIGHT = 600, 500
MINT = (230, 254, 212)
COLOR1 =  (255, 150, 100)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

# до начала игрового цикла отображаем объекты:
# координаты центра круга
x, y = WIDTH / 2, HEIGHT / 2  # координаты центра круга
r = 30  # радиус круга
pg.draw.circle(screen, COLOR1, (x, y), r)  # рисуем круг
pg.display.update()  # обновляем окно

flag_play = True
while flag_play:
    clock.tick(FPS)

    COLOR = [random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)]

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                COLOR1 = (random.randint(1,255), random.randint(1,255), random.randint(1,255))
    if not flag_play:
        break

    # изменение состояний объектов:
    keys = pg.key.get_pressed()
    if keys[pg. K_LEFT] and keys[pg. K_UP] and x >= r and y >= r:
        x -= 3
        y -= 3
    elif keys[pg. K_LEFT] and keys[pg. K_DOWN] and x >= r and y <= HEIGHT - r:
        x -= 3
        y += 3
    elif keys[pg. K_RIGHT] and keys[pg. K_UP] and x <= WIDTH - r and y >= r:
        x += 3
        y -= 3
    elif keys[pg. K_RIGHT] and keys[pg. K_DOWN] and x <= WIDTH - r and y <= HEIGHT - r:
        x += 3
        y += 3
    elif keys[pg.K_LEFT] and x >= r:
        x -= 3
    elif keys[pg.K_RIGHT] and x <= WIDTH - r:
        x += 3
    elif keys[pg.K_UP] and y >= r:
        y -= 3
    elif keys[pg.K_DOWN] and y <= HEIGHT - r:
        y += 3



    screen.fill(MINT)
    pg.draw.circle(screen, COLOR1, (x, y), r)  # рисуем новый, сдвинутый круг

    pg.display.update()  # обновляем окно
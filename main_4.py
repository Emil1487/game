import pygame
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
r = 30  # радиус круга
x, y = random.randint(r, WIDTH - r), random.randint(r, HEIGHT - r)  # координаты центра круга
pg.draw.circle(screen, COLOR1, (x, y), r)  # рисуем круг
pg.display.update()  # обновляем окно

flag_play = True
while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        pos = pg.mouse.get_pos()
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
        elif event.type == pg.MOUSEWHEEL:
            if event.y < 0 and ((x - pos[0]) ** 2 + (y - pos[1]) ** 2) ** 0.5 <= r and r > 10:
                r -= 10
            elif event.y > 0 and ((x - pos[0]) ** 2 + (y - pos[1]) ** 2) ** 0.5 <= r and r < 100:
                r += 10



    if not flag_play:
        break

    # изменение состояний объектов:
    pressed = pg.mouse.get_pressed()
    pos = pg.mouse.get_pos()
    lst1 = []
    lst2 = []
    if pressed[1] and ((x - pos[0]) ** 2 + (y - pos[1]) ** 2) ** 0.5 <= r:
        x, y = random.randint(r, WIDTH - r), random.randint(r, HEIGHT - r)
    elif pressed[0] and ((x - pos[0]) ** 2 + (y - pos[1]) ** 2) ** 0.5 <= r and r < 100:
        r += 10
    elif pressed[2] and ((x - pos[0]) ** 2 + (y - pos[1]) ** 2) ** 0.5 <= r and r > 10:
        r -= 10

    screen.fill(MINT)
    pg.draw.circle(screen, COLOR1, (x, y), r)  # рисуем новый, сдвинутый круг

    pg.display.update()

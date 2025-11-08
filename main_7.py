import pygame as pg
import random

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

ball_lst = []


def random():
    return random.randint(50, 250)


class Ball:
    def __init__(self, COLOR, size, speed):
        if COLOR == "random":
            self.COLOR = (random(), random(), random(), random())
        else:
            self.COLOR = COLOR
        self.surf = pg.Surface((100, 100), pg.SRCALPHA)
        self.rect = self.surf.get_rect(topleft=(0, 50))
        if size == "random":
            self.size = random.randint(10, 50)
        else:
            self.size = size
        if speed == "random":
            self.speed = random.randint(1, 40)
        else:
            self.speed = speed
        pg.draw.circle(self.surf, self.COLOR, (50, 50), self.size)

    def move(self):
        if self.rect.left <= W and self.rect.top == 50:
            self.rect.right += self.speed
        elif self.rect.left >= W and self.rect.top == 50:
            self.rect.top += 200
        elif self.rect.right >= 0 and self.rect.top == 250:
            self.rect.left -= self.speed
        elif self.rect.right <= 0 and self.rect.top == 250:
            self.rect.top -= 200

    def draw(self):
        sc.blit(self.surf, self.rectan)


ball_lst.append(Ball((209, 29, 29, 100), 20, 10))
ball_lst.append(Ball((255, 247, 0, 100), 40, 5))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                ball_lst.append(Ball("random", "random", "random"))

    sc.blit(bg, (0, 0))
    for elem in ball_lst:
        elem.move()
        elem.draw()

    pg.display.update()
    clock.tick(FPS)

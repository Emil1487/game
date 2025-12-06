import pygame as pg
import random as rn

FPS = 30
W, H = 1000, 600

pg.mixer.pre_init(44100, -16, 1, 512)
pg.init()

pg.init()
sc = pg.display.set_mode((W, H))
pg.display.set_caption("Snake")
clock = pg.time.Clock()

bg = pg.image.load("images/background.png")
bg = pg.transform.scale_by(bg, 5)


class Head:
    def __init__(self, cords=(W/2, H/2)):
        self.surf = pg.image.load('images/snake_head.png')
        self.surf = pg.transform.scale_by(self.surf, 5)
        self.cords = cords
        self.stop = False
        self.direction = "up"

    def move(self):
        if self.direction == "right":
            self.cords = self.cords = (self.cords[0] + 100, self.cords[1])
        elif self.direction == "left":
            self.cords = self.cords = (self.cords[0] - 100, self.cords[1])
        elif self.direction == "up":
            self.cords = self.cords = (self.cords[0], self.cords[1] - 100)
        elif self.direction == "down":
            self.cords = self.cords = (self.cords[0], self.cords[1] + 100)
        if self.cords[0] >= W:
            self.cords = (0, self.cords[1])
        if self.cords[0] < 0:
            self.cords = (900, self.cords[1])

    def direct(self, d):
        if d == "right" and self.direction != "left" and self.direction != d:
            if self.direction == "up":
                self.surf = pg.transform.rotate(self.surf, -90)
            else:
                self.surf = pg.transform.rotate(self.surf, 90)
            self.direction = 'right'
        elif d == "left" and self.direction != "right" and self.direction != d:
            if self.direction == "up":
                self.surf = pg.transform.rotate(self.surf, 90)
            else:
                self.surf = pg.transform.rotate(self.surf, -90)
            self.direction = "left"
        elif d == "down" and self.direction != "up" and self.direction != d:
            if self.direction == "right":
                self.surf = pg.transform.rotate(self.surf, -90)
            else:
                self.surf = pg.transform.rotate(self.surf, 90)
            self.direction = 'down'
        elif d == "up" and self.direction != "down" and self.direction != d:
            if self.direction == "right":
                self.surf = pg.transform.rotate(self.surf, 90)
            else:
                self.surf = pg.transform.rotate(self.surf, -90)
            self.direction = "up"

    def draw(self, sc):
        sc.blit(self.surf, self.cords)


class Body():
    def __init__(self, cords):
        self.cords == cords
        self.surf == pg.image.load('images/snake_body.png')
        self.surf = pg.transform.scale_by(self.surf, 5)


head = Head()

cnt = 0
cnt_move = 0
sc.blit(bg, (0, 0))
pg.display.update()
flag_play = True
while flag_play:
    clock.tick(FPS)
    cnt += 1
    cnt_move += 1

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break

    if not flag_play:
        break

    keys = pg.key.get_pressed()
    if cnt_move >= 30:
        if keys[pg.K_LEFT]:
            head.direct("left")
        elif keys[pg.K_RIGHT]:
            head.direct("right")
        elif keys[pg.K_UP]:
            head.direct("up")
        elif keys[pg.K_DOWN]:
            head.direct("down")
        cnt_move = 0

    if cnt == 30:
        head.move()
        cnt = 0

    sc.blit(bg, (0, 0))

    head.draw(sc)
    pg.display.update()

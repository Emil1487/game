import pygame as pg
import random as rn

W = 600
H = 400

BLACK = (0, 0, 0)
GRAY = (194, 194, 194)
YELLOW = (255, 247, 0)
WHITE = (255, 255, 255)
COLOR = (153, 119, 89)
RED = (255, 0, 0)
DARK_RED = (209, 0, 0)

FPS = 60

pg.init()
sc = pg.display.set_mode((W, H))
pg.display.set_caption("car")
clock = pg.time.Clock()

sc.fill(WHITE)


class Player:

    def __init__(self):
        self.size = 10
        self.speed = 5
        self.surf = pg.image.load('car.png').convert_alpha()
        self.rect = self.surf.get_rect(center=(W / 2, H / 2))
        self.mask = pg.mask.from_surface(self.surf)

    def move(self, dx=0, dy=0):
        if (self.rect.left + dx * self.speed) > 0 and (self.rect.right + dx * self.speed) < W:
            self.rect.x += dx * self.speed
        if (self.rect.top + dy * self.speed) > 0 and (self.rect.bottom + dy * self.speed) < H:
            self.rect.y += dy * self.speed

    def draw(self):
        sc.blit(self.surf, self.rect)

    def los(self):
        pass


carx = pg.sprite.Group()

class Enemy (pg.sprite.Sprite):
    def __init__(self, x, filename, group):
        pg.sprite.Sprite.__init__(self)
        self.surf = pg.image.load(filename)
        self.rect = self.surf.get_rect(center=(x, 0))
        self.speed = 10
        self.mask = pg.mask.from_surface(self.surf)
        self.add(group)

    def spawn(self):
        self.rect.center = (rn.randint(10, W - 10), 10)

    def check_down(self):
        if self.rect.top == H:
            self.spawn()

    def draw(self):
        sc.blit(self.surf, self.rect)

    def update(self):
        if self.rect.top < H:
            self.rect.top += self.speed
            self.draw()
        else:
            self.spawn()


def check_collisions(player, cars_en):
    for cars in cars_en:
        offset = (cars.rect.x - player.rect.x, cars.rect.y - player.rect.y)
        if player.mask.overlap(cars.mask, offset) is not None:
            car.los


car = Player()
enemys = [Enemy(rn.randint(10, W - 10), "car1.png", carx), Enemy(rn.randint(10, W - 10), "car2.png", carx), Enemy(rn.randint(10, W - 10), "car3.png", carx)]

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        car.move(dx=-1)
    if keys[pg.K_RIGHT]:
        car.move(dx=1)
    if keys[pg.K_UP]:
        car.move(dy=-1)
    if keys[pg.K_DOWN]:
        car.move(dy=1)

    check_collisions(car, enemys)
    sc.fill(WHITE)
    car.draw()
    carx.update()
    pg.display.update()
    clock.tick(FPS)

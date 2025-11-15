import pygame as pg
import random

W = 600
H = 400

BROWN = (59, 24, 11)
GRAY = (194, 194, 194)
YELLOW = (255, 247, 0)
WHITE = (255, 255, 255)
COLOR = (153, 119, 89)

FPS = 60

pg.init()
sc = pg.display.set_mode((W, H))
pg.display.set_caption("Surface")
clock = pg.time.Clock()

sc.fill(WHITE)

foods = []


def rand(size):
    randomize = (random.randint(size, W - size), random.randint(size, H - size))
    return randomize


class Food:
    def __init__(self, size, pos):
        self.COLOR = (153, 119, 89)
        self.size = size
        self.SN = size
        self.surf = pg.Surface((self.size * 2, self.size * 2), pg.SRCALPHA)
        self.rect = self.surf.get_rect(center=pos)
        self.surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.surf, (*COLOR, 255),
                       (self.rect.width / 2, self.rect.height / 2), self.size)
        self.mask = pg.mask.from_surface(self.surf)
        foods.append(self)

    def eated(self):
        self.rect.center = rand(self.size)
        return self.SN

    def draw(self):
        sc.blit(self.surf, self.rect)


class Player:
    Size = 10
    speed = 5

    def __init__(self):
        self.size = 10
        self.speed = 5
        self.surf = pg.Surface((self.size * 2, self.size * 2), pg.SRCALPHA)
        self.rect = self.surf.get_rect(center=(W / 2, H / 2))
        self.surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.surf, (*YELLOW, 255), (self.rect.width / 2, self.rect.height / 2), self.size)
        self.speed = Player.speed
        self.mask = pg.mask.from_surface(self.surf)

    def move(self, dx=0, dy=0):
        if (self.rect.left + dx * self.speed) > 0 and (self.rect.right + dx * self.speed) < W:
            self.rect.x += dx * self.speed
        if (self.rect.top + dy * self.speed) > 0 and (self.rect.bottom + dy * self.speed) < H:
            self.rect.y += dy * self.speed

    def grow(self, SN):
        if self.rect.top - SN // 4 < 0:
            self.rect.top += SN // 4
        if self.rect.left - SN // 4 < 0:
            self.rect.left += SN // 4
        if self.rect.bottom + SN // 4 > H:
            self.rect.bottom -= SN // 4
        if self.rect.right + SN // 4 > W:
            self.rect.right -= SN // 4
        self.size += SN // 4
        self.surf = pg.Surface((self.size * 2, self.size * 2), pg.SRCALPHA)
        self.surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.surf, (*YELLOW, 255), (self.size, self.size), self.size)
        self.mask = pg.mask.from_surface(self.surf)
        self.rect = self.surf.get_rect(center=self.rect.center)

    def draw(self):
        sc.blit(self.surf, self.rect)


def check_collisions(playerx, foods):
    for food in foods:
        offset = (food.rect.x - playerx.rect.x, food.rect.y - playerx.rect.y)
        if player.mask.overlap(food.mask, offset) is not None:
            if playerx.size <= 150:
                playerx.grow(food.eated())


foods = []
for i in range(4):
    sized = random.randint(10, 50)
    foods.append(Food(sized, rand(sized)))
player = Player()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        player.move(dx=-1)
    if keys[pg.K_RIGHT]:
        player.move(dx=1)
    if keys[pg.K_UP]:
        player.move(dy=-1)
    if keys[pg.K_DOWN]:
        player.move(dy=1)

    check_collisions(player, foods)
    sc.fill(WHITE)
    for elem in foods:
        elem.draw()
    player.draw()

    pg.display.update()
    clock.tick(FPS)

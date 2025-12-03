import pygame as pg

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
        self.pov = 90
        self.size = 10
        self.speed = 5
        self.surf = pg.image.load('images/car.png')
        self.rect = self.surf.get_rect(center=(W / 2, H / 2))

    def move(self, dx=0, dy=0, povorot=90):
        if povorot != self.pov:
            if self.pov < povorot:
                pov = self.pov
                while pov != povorot:
                    self.surf = pg.transform.rotate(self.surf, 90)
                    pov += 90
                self.pov = povorot
            elif self.pov > povorot:
                pov = self.pov
                while pov != povorot:
                    self.surf = pg.transform.rotate(self.surf, -90)
                    pov -= 90
                self.pov = povorot
        if (self.rect.left + dx * self.speed) > 0 and (self.rect.right + dx * self.speed) < W:
            self.rect.x += dx * self.speed
        if (self.rect.top + dy * self.speed) > 0 and (self.rect.bottom + dy * self.speed) < H:
            self.rect.y += dy * self.speed

    def draw(self):
        sc.blit(self.surf, self.rect)


car = Player()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        car.move(dx=-1, povorot=180)
    elif keys[pg.K_RIGHT]:
        car.move(dx=1, povorot=360)
    elif keys[pg.K_UP]:
        car.move(dy=-1, povorot=90)
    elif keys[pg.K_DOWN]:
        car.move(dy=1, povorot=270)

    sc.fill(WHITE)
    car.draw()
    pg.display.update()
    clock.tick(FPS)

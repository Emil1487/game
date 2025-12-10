import random
import pygame as pg

FPS = 30
W, H = 1000, 600

pg.mixer.pre_init(44100, -16, 1, 512)
pg.init()

sc = pg.display.set_mode((W, H))
pg.display.set_caption("Snake")
clock = pg.time.Clock()

bg = pg.image.load("images/background.png")
body = pg.sprite.Group()


def apple_rand():
    x = random.randint(1, 18) * 40
    y = random.randint(1, 23) * 40
    for elem in body_parts:
        if x == elem.cords[0] and y == elem.cords[1]:
            return apple_rand()
    for apple in apples:
        if x == apple.cords[0] and y == apple.cords[1]:
            return apple_rand()
    return x, y


class Head:
    def __init__(self, cords=(520, 200)):
        self.surf = pg.image.load('images/snake_head.png')
        self.surf = pg.transform.scale_by(self.surf, 2)
        self.cords = cords
        self.old_cords = cords
        self.stop = False
        self.direction = "right"
        self.surf = pg.transform.rotate(self.surf, -90)

    def move(self):
        self.old_cords = self.cords
        if self.direction == "right":
            self.cords = (self.cords[0] + 40, self.cords[1])
        elif self.direction == "left":
            self.cords = (self.cords[0] - 40, self.cords[1])
        elif self.direction == "up":
            self.cords = (self.cords[0], self.cords[1] - 40)
        elif self.direction == "down":
            self.cords = (self.cords[0], self.cords[1] + 40)

        if self.cords[0] >= W:
            self.cords = (0, self.cords[1])
        if self.cords[0] < 0:
            self.cords = (960, self.cords[1])
        if self.cords[1] >= H:
            self.cords = (self.cords[0], 0)
        if self.cords[1] < 0:
            self.cords = (self.cords[0], 560)

    def direct(self, d):
        if d == "right" and self.direction != "left":
            self.surf = pg.transform.rotate(pg.image.load('images/snake_head.png'), -90)
            self.surf = pg.transform.scale_by(self.surf, 2)
            self.direction = 'right'
        elif d == "left" and self.direction != "right":
            self.surf = pg.transform.rotate(pg.image.load('images/snake_head.png'), 90)
            self.surf = pg.transform.scale_by(self.surf, 2)
            self.direction = "left"
        elif d == "down" and self.direction != "up":
            self.surf = pg.transform.rotate(pg.image.load('images/snake_head.png'), 180)
            self.surf = pg.transform.scale_by(self.surf, 2)
            self.direction = 'down'
        elif d == "up" and self.direction != "down":
            self.surf = pg.image.load('images/snake_head.png')
            self.surf = pg.transform.scale_by(self.surf, 2)
            self.direction = "up"

    def draw(self, screen):
        screen.blit(self.surf, self.cords)


class Body:
    def __init__(self, cords):
        self.cords = cords
        self.surf = pg.image.load('images/snake_body.png')
        self.surf = pg.transform.scale_by(self.surf, 2)

    def move(self, new_cords):
        self.cords = new_cords

    def draw(self, screen):
        if self == body_parts[-1]:
            self.surf = pg.image.load('images/snake_end.png')
            self.surf = pg.transform.scale_by(self.surf, 2)
        elif False:
            pass
        elif self != body_parts[-1]:
            self.surf = pg.image.load('images/snake_body.png')
            self.surf = pg.transform.scale_by(self.surf, 2)
        screen.blit(self.surf, self.cords)


class Apples:
    def __init__(self):
        self.cords = apple_rand()
        self.surf = pg.image.load('images/apple.png')
        self.surf = pg.transform.scale_by(self.surf, 2)

    def draw(self, screen):
        screen.blit(self.surf, self.cords)


head = Head()
body_parts = [head, Body((480, 200))]
apples = []
for _ in range(5):
    apples.append(Apples())

cnt = 0
sc.blit(bg, (0, 0))
pg.display.update()
flag_play = True

key_pressed = ""
while flag_play:
    clock.tick(FPS)
    cnt += 1

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break

    if not flag_play:
        break

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        key_pressed = "left"
    elif keys[pg.K_RIGHT]:
        key_pressed = "right"
    elif keys[pg.K_UP]:
        key_pressed = "up"
    elif keys[pg.K_DOWN]:
        key_pressed = "down"

    if cnt >= 10:
        if key_pressed == "left":
            head.direct("left")
        elif key_pressed == "right":
            head.direct("right")
        elif key_pressed == "up":
            head.direct("up")
        elif key_pressed == "down":
            head.direct("down")
        old_positions = [elem.cords for elem in body_parts]
        head.move()
        for i in range(1, len(body_parts)):
            body_parts[i].move(old_positions[i - 1])

        cnt = 0

    for apple in apples:
        if head.cords == apple.cords:
            apple.cords = apple_rand()
            last_part = body_parts[-1]
            body_parts.append(Body(last_part.cords))

    sc.blit(bg, (0, 0))
    for elem in apples:
        elem.draw(sc)
    for elem in body_parts:
        elem.draw(sc)

    pg.display.update()

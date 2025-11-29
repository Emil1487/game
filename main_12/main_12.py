import pygame as pg
import random as rn

W = 600
H = 400

BLACK = (0, 0, 0)
GRAY = (82, 82, 82)
YELLOW = (255, 247, 0)
WHITE = (255, 255, 255)
COLOR = (153, 119, 89)
RED = (255, 0, 0)
DARK_RED = (209, 0, 0)

FPS = 60
pg.mixer.pre_init(44100, -16, 1, 512)
pg.init()

pg.mixer.music.load('sounds/bg_music.wav')
pg.mixer.music.play(-1)

car_crash = pg.mixer.Sound('sounds/car_crash.wav')

cars = pg.sprite.Group()
pg.init()
sc = pg.display.set_mode((W, H))
pg.display.set_caption("car")
clock = pg.time.Clock()

bg = pg.Surface((W, H))
bg.fill(GRAY)
pg.draw.rect(bg, WHITE, (195, 0, 10, H))
pg.draw.rect(bg, WHITE, (395, 0, 10, H))


class Player:

    def __init__(self):
        self.size = 10
        self.speed = 6
        self.surf = pg.image.load('images/car.png')
        self.rect = self.surf.get_rect(center=(W / 2, H / 2 + 50))
        self.mask = pg.mask.from_surface(self.surf)
        self.stop = False
        self.crash_played = False

    def move(self, dx=0, dy=0):
        if (self.rect.left + dx * self.speed) > 0 and (self.rect.right + dx * self.speed) < W:
            self.rect.x += dx * self.speed
        if (self.rect.top + dy * self.speed) > 0 and (self.rect.bottom + dy * self.speed) < H:
            self.rect.y += dy * self.speed

    def draw(self):
        sc.blit(self.surf, self.rect)

    def los(self):
        if not self.crash_played:
            car_crash.play()
            self.crash_played = True
        self.speed = 0
        self.stop = True

    def reset(self):
        self.speed = 6
        self.surf = pg.image.load('images/car.png')
        self.rect = self.surf.get_rect(center=(W / 2, H / 2))
        self.mask = pg.mask.from_surface(self.surf)
        self.stop = False
        self.crash_played = False


class Enemy (pg.sprite.Sprite):
    def __init__(self, x, filename, group):
        pg.sprite.Sprite.__init__(self)
        self.surf = pg.image.load(filename)
        self.rect = self.surf.get_rect(center=(x, 0))
        self.speed = rn.randint(5, 12)
        self.mask = pg.mask.from_surface(self.surf)
        self.add(group)

    def spawn(self):
        self.rect.center = (rn.randint(10, W - 10), -10)
        self.speed = rn.randint(5, 12)

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

    def stop(self):
        self.speed = 0

    def reset(self):
        self.spawn()
        self.speed = rn.randint(5, 12)


class Button:
    def __init__(self, text, text_size, text_color, button_color, button_pos):
        self.button_color = None
        self.font = pg.font.SysFont(None, text_size)
        self.text_surf = self.font.render(text, True, text_color)
        self.text_rect = self.text_surf.get_rect(center=button_pos)
        self.button_surf = pg.Surface((self.text_surf.get_width() + 50, self.text_surf.get_height() + 50))
        self.button_rect = self.button_surf.get_rect(center=button_pos)
        self.button_surf.fill(button_color)
        pg.draw.rect(self.button_surf, BLACK, (0, 0, self.button_rect.width, self.button_rect.height), 3)

    def draw(self, screen):
        if car.stop:
            screen.blit(self.button_surf, self.button_rect)
            screen.blit(self.text_surf, self.text_rect)

    def update_color(self, button_color):
        self.button_color = button_color
        self.button_surf.fill(self.button_color)
        pg.draw.rect(self.button_surf, BLACK, (0, 0, self.button_rect.width, self.button_rect.height), 3)


def check_click_on_button(button):
    if button.button_rect.collidepoint(pg.mouse.get_pos()):
        return True


def check_collisions(player, enemys):
    for enemy2 in enemys:
        offset_x = enemy2.rect.left - player.rect.left
        offset_y = enemy2.rect.top - player.rect.top
        if player.mask.overlap(enemy2.mask, (offset_x, offset_y)) is not None:
            player.los()
            for e in enemys:
                e.stop()
            break


my_button = Button("You lost, press r to reset", 32, BLACK, RED, (W // 2, H // 2))
car = Player()
enemy = [Enemy(rn.randint(10, W - 10), "images/car1.png", cars),
         Enemy(rn.randint(10, W - 10), "images/car2.png", cars),
         Enemy(rn.randint(10, W - 10), "images/car3.png", cars)]

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if check_click_on_button(my_button):
                car.reset()
                for elem in enemy:
                    elem.reset()
        elif event.type == pg.KEYDOWN and event.key == pg.K_r:
            if car.stop:
                car.reset()
                for elem in enemy:
                    elem.reset()

    check_collisions(car, enemy)

    if check_click_on_button(my_button):
        my_button.update_color(DARK_RED)
    else:
        my_button.update_color(RED)

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        car.move(dx=-1)
    if keys[pg.K_RIGHT]:
        car.move(dx=1)
    if keys[pg.K_UP]:
        car.move(dy=-1)
    if keys[pg.K_DOWN]:
        car.move(dy=1)

    check_collisions(car, enemy)
    sc.blit(bg, (0, 0))
    car.draw()
    cars.update()
    my_button.draw(sc)
    pg.display.update()
    clock.tick(FPS)

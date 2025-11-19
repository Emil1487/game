import pygame as pg
import random

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
pg.display.set_caption("Surface")
clock = pg.time.Clock()


sc.fill(WHITE)

foods = []


def rand(size):
    randomize = (random.randint(size, W - size), random.randint(size, H - size))
    return randomize


class Food:
    def __init__(self, size, pos):
        self.COLOR = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        self.size = size
        self.SN = size
        self.surf = pg.Surface((self.size * 2, self.size * 2), pg.SRCALPHA)
        self.rect = self.surf.get_rect(center=pos)
        self.surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.surf, (*self.COLOR, 255), (self.size, self.size), self.size)
        pg.draw.circle(self.surf, (*BLACK, 255),
                       (self.rect.width / 2, self.rect.height / 2), self.size, size // 5)
        self.mask = pg.mask.from_surface(self.surf)
        foods.append(self)

    def eated(self):
        self.COLOR = [random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)]
        new_size = random.randint(10, 50)
        self.size = new_size
        self.SN = new_size
        self.surf = pg.Surface((self.size * 2, self.size * 2), pg.SRCALPHA)
        self.rect = self.surf.get_rect(center=rand(self.size))
        self.surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.surf, (*self.COLOR, 255), (self.size, self.size), self.size)
        pg.draw.circle(self.surf, (*BLACK, 255),
                       (self.rect.width / 2, self.rect.height / 2), self.size, new_size // 5)
        self.mask = pg.mask.from_surface(self.surf)
        return self.SN

    def draw(self):
        sc.blit(self.surf, self.rect)


class Button:
    def __init__(self, text, text_size, text_color, button_color, button_pos):
        self.font = pg.font.SysFont(None, text_size)
        self.text_surf = self.font.render(text, True, text_color)
        self.text_rect = self.text_surf.get_rect(center=button_pos)
        self.button_surf = pg.Surface((self.text_surf.get_width() + 50, self.text_surf.get_height() + 50))
        self.button_rect = self.button_surf.get_rect(center=button_pos)
        self.button_surf.fill(button_color)
        pg.draw.rect(self.button_surf, BLACK, (0, 0, self.button_rect.width, self.button_rect.height), 3)

    def draw(self, screen):
        screen.blit(self.button_surf, self.button_rect)
        screen.blit(self.text_surf, self.text_rect)

    def update_color(self, color):
        self.button_color = color
        self.button_surf.fill(self.button_color)
        pg.draw.rect(self.button_surf, BLACK, (0, 0, self.button_rect.width, self.button_rect.height), 3)


def check_click_on_button(button):
    if button.button_rect.collidepoint(pg.mouse.get_pos()):
        return True


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
        pg.draw.circle(self.surf, (*BLACK, 255), (self.size, self.size), self.size, self.size // 7)
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
        pg.draw.circle(self.surf, (*BLACK, 255), (self.size, self.size), self.size, self.size // 7)
        self.mask = pg.mask.from_surface(self.surf)
        self.rect = self.surf.get_rect(center=self.rect.center)

    def reset(self):
        self.size = 10
        self.surf = pg.Surface((self.size * 2, self.size * 2), pg.SRCALPHA)
        self.surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.surf, (*YELLOW, 255), (self.size, self.size), self.size)
        pg.draw.circle(self.surf, (*BLACK, 255), (self.size, self.size), self.size, self.size // 7)
        self.mask = pg.mask.from_surface(self.surf)
        self.rect = self.surf.get_rect(center=(W // 2, H // 2))
        for elem in foods:
            elem.eated()

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
my_button = Button("Reset - r", 32, BLACK, RED, (W * 85 / 100, 40))

f = pg.font.Font(None, 24)
sc_text = f.render(str(player.size), True, BLACK)
pos = sc_text.get_rect(center=(W // 2, 40))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if check_click_on_button(my_button):
                player.reset()
        elif event.type == pg.KEYDOWN and event.key == pg.K_r:
            player.reset()

    if check_click_on_button(my_button):
        my_button.update_color(DARK_RED)
    else:
        my_button.update_color(RED)

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        player.move(dx=-1)
    if keys[pg.K_RIGHT]:
        player.move(dx=1)
    if keys[pg.K_UP]:
        player.move(dy=-1)
    if keys[pg.K_DOWN]:
        player.move(dy=1)

    sc_text = f.render(f"размер: {player.size}", True, BLACK)
    pos = sc_text.get_rect(center=(W // 2, 30))

    check_collisions(player, foods)
    sc.fill(WHITE)
    for elem in foods:
        elem.draw()
    player.draw()
    sc.blit(sc_text, pos)
    my_button.draw(sc)
    pg.display.update()
    clock.tick(FPS)

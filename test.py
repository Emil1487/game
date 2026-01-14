import random
import pygame as pg

FPS = 30
W, H = 1000, 800

BLACK = (0, 0, 0)
RED = (255, 0, 0)
DARK_RED = (209, 0, 0)
WHITE = (255, 255, 255)

pg.mixer.pre_init(44100, -16, 1, 512)
pg.init()

sc = pg.display.set_mode((W, H))
pg.display.set_caption("Snake")
clock = pg.time.Clock()

bg = pg.image.load("images/background.png")


def apple_rand(occupied, exclude=None):
    attempts = 0
    while attempts < 100:
        attempts += 1
        x, y = random.randint(0, 24) * 40, random.randint(0, 19) * 40
        pos = (x, y)
        if pos not in occupied and pos != exclude:
            return pos
    return -40, -40


def check_click_on_button(button):
    if button.button_rect.collidepoint(pg.mouse.get_pos()):
        return True


def direct(self, d):
    if d == "right" and self.direction != "left":
        self.surf = pg.transform.rotate(pg.image.load('images/snake_head.png'), -90)
        self.surf = pg.transform.scale_by(self.surf, 2)
        return 'right'
    elif d == "left" and self.direction != "right":
        self.surf = pg.transform.rotate(pg.image.load(self.image), 90)
        self.surf = pg.transform.scale_by(self.surf, 2)
        return "left"
    elif d == "down" and self.direction != "up":
        self.surf = pg.transform.rotate(pg.image.load(self.image), 180)
        self.surf = pg.transform.scale_by(self.surf, 2)
        return 'down'
    elif d == "up" and self.direction != "down":
        self.surf = pg.image.load(self.image)
        self.surf = pg.transform.scale_by(self.surf, 2)
        return "up"
    return self.direction


class Head:
    def __init__(self, score=0, cords=(520, 200)):
        self.image = 'images/snake_head.png'
        self.surf = pg.image.load('images/snake_head.png')
        self.surf = pg.transform.scale_by(self.surf, 2)
        self.cords = cords
        self.old_cords = cords
        self.stop = False
        self.direction = "right"
        self.surf = pg.transform.rotate(self.surf, -90)
        self.stop = 0
        self.old_dir = self.direction
        self.score = score

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

        if self.cords[0] >= W or self.cords[0] < 0 or self.cords[1] >= H or self.cords[1] < 0:
            self.los()

    def direct(self, d):
        self.direction = direct(self, d)

    def los(self):
        self.stop = 1

    def draw(self, screen):
        screen.blit(self.surf, self.cords)


class Body:
    def __init__(self, cords):
        self.image = 'images/snake_body.png'
        self.direction = ""
        self.cords = cords
        self.surf = pg.image.load('images/snake_body.png')
        self.surf = pg.transform.scale_by(self.surf, 2)
        self.direction_to = self.direction
        self.direction_curr = "right"

    def move(self, new_cords):
        self.cords = new_cords

    def direct(self, d):
        self.direction = direct(self, d)

    def find_dir(self, index):
        if self.cords[0] < body_parts[index - 1].cords[0]:
            self.surf = pg.transform.rotate(self.surf, -90)
        elif self.cords[0] > body_parts[index - 1].cords[0]:
            self.surf = pg.transform.rotate(self.surf, 90)
        elif self.cords[1] < body_parts[index - 1].cords[1]:
            self.surf = pg.transform.rotate(self.surf, 180)
        elif self.cords[1] > body_parts[index - 1].cords[1]:
            pass

    def draw(self, screen, index):
        if self == body_parts[-1]:
            self.surf = pg.image.load('images/snake_end.png')
            self.image = 'images/snake_end.png'
            self.surf = pg.transform.scale_by(self.surf, 2)
            self.find_dir(index)
            screen.blit(self.surf, self.cords)
            return
        if self != body_parts[-1]:
            self.surf = pg.image.load('images/snake_body.png')
            self.image = 'images/snake_body.png'
            self.surf = pg.transform.scale_by(self.surf, 2)
            self.find_dir(index)

        if (body_parts[index - 1].cords[0] != body_parts[index + 1].cords[0] and body_parts[index - 1].cords[1] !=
                body_parts[index + 1].cords[1]):
            self.surf = pg.image.load('images/snake_corner.png')
            self.image = 'images/snake_corner.png'
            self.surf = pg.transform.scale_by(self.surf, 2)

            if self.cords[0] > body_parts[index - 1].cords[0] and self.cords[1] == body_parts[index - 1].cords[1]:
                if self.cords[1] < body_parts[index + 1].cords[1]:
                    self.surf = pg.transform.rotate(self.surf, 90)
                elif self.cords[1] > body_parts[index + 1].cords[1]:
                    pass

            elif self.cords[0] < body_parts[index - 1].cords[0] and self.cords[1] == body_parts[index - 1].cords[1]:
                if self.cords[1] < body_parts[index + 1].cords[1]:
                    self.surf = pg.transform.rotate(self.surf, -180)
                elif self.cords[1] > body_parts[index + 1].cords[1]:
                    self.surf = pg.transform.rotate(self.surf, -90)

            elif self.cords[0] < body_parts[index + 1].cords[0] and self.cords[1] == body_parts[index + 1].cords[1]:
                if self.cords[1] < body_parts[index - 1].cords[1]:
                    self.surf = pg.transform.rotate(self.surf, 180)
                elif self.cords[1] > body_parts[index - 1].cords[1]:
                    self.surf = pg.transform.rotate(self.surf, -90)

            elif self.cords[0] > body_parts[index + 1].cords[0] and self.cords[1] == body_parts[index + 1].cords[1]:
                if self.cords[1] < body_parts[index - 1].cords[1]:
                    self.surf = pg.transform.rotate(self.surf, 90)
                elif self.cords[1] > body_parts[index - 1].cords[1]:
                    self.surf = pg.transform.rotate(self.surf, 0)

        screen.blit(self.surf, self.cords)


class Apples:
    def __init__(self):
        occupied = [elem.cords for elem in body_parts] + [a.cords for a in apples]
        self.cords = apple_rand(occupied)
        self.surf = pg.image.load('images/apple.png')
        self.surf = pg.transform.scale_by(self.surf, 2)

    def draw(self, screen):
        screen.blit(self.surf, self.cords)


class Text:
    def __init__(self, score, text_size, text_color, text_pos):
        self.text_color = text_color
        self.color = text_color
        self.score = score
        self.bg_surf = pg.Surface((W, H), pg.SRCALPHA)
        pg.draw.rect(self.bg_surf, (*BLACK, 128), (0, 0, W, H))
        self.font = pg.font.SysFont(None, text_size)
        self.text_surf = self.font.render(score, True, text_color)
        self.text_rect = self.text_surf.get_rect(center=text_pos)

    def draw(self, screen):
        if int(self.score) < head.score:
            self.score = head.score
        self.text_surf = self.font.render(f""""Score: {head.score} Highest score: {self.score}""", True, self.text_color)
        screen.blit(self.text_surf, self.text_rect)


class Button:
    def __init__(self, text, text_size, text_color, button_color, button_pos):
        self.bg_surf = pg.Surface((W, H), pg.SRCALPHA)
        pg.draw.rect(self.bg_surf, (*BLACK, 128), (0, 0, W, H))
        self.button_color = None
        self.font = pg.font.SysFont(None, text_size)
        self.text_surf = self.font.render(text, True, text_color)
        self.text_rect = self.text_surf.get_rect(center=button_pos)
        self.button_surf = pg.Surface((self.text_surf.get_width() + 50, self.text_surf.get_height() + 50))
        self.button_rect = self.button_surf.get_rect(center=button_pos)
        self.button_surf.fill(button_color)
        pg.draw.rect(self.button_surf, BLACK, (0, 0, self.button_rect.width, self.button_rect.height), 3)

    def draw(self, screen):
        if head.stop:
            screen.blit(self.button_surf, self.button_rect)
            screen.blit(self.text_surf, self.text_rect)

    def update_color(self, button_color):
        self.button_color = button_color
        self.button_surf.fill(self.button_color)
        pg.draw.rect(self.button_surf, BLACK, (0, 0, self.button_rect.width, self.button_rect.height), 3)


sc.blit(bg, (0, 0))
pg.display.update()
flag_play = True


def main():
    cnt = 0
    head.stop = 0
    key_pressed = ''
    while True:
        clock.tick(FPS)
        cnt += 1

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return

        if head.stop:
            los()
            return

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            key_pressed = "left"
        elif keys[pg.K_RIGHT]:
            key_pressed = "right"
        elif keys[pg.K_UP]:
            key_pressed = "up"
        elif keys[pg.K_DOWN]:
            key_pressed = "down"

        if cnt >= 6:
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
                last_part = body_parts[-1]
                body_parts.append(Body(last_part.cords))
                occupied = [elem.cords for elem in body_parts] + [a.cords for a in apples]
                apple.cords = apple_rand(occupied)
                head.score += 1

        for part in body_parts[1:]:
            if head.cords == part.cords:
                head.los()

        sc.blit(bg, (0, 0))
        for ind in range(1, len(body_parts)):
            body_parts[ind].draw(sc, ind)
        head.draw(sc)
        for elem in apples:
            elem.draw(sc)
        text_score.draw(sc)
        pg.display.update()


def los():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if check_click_on_button(my_button):
                    return text_score
            elif event.type == pg.KEYDOWN and event.key == pg.K_r:
                return text_score

        if check_click_on_button(my_button):
            my_button.update_color(DARK_RED)
        else:
            my_button.update_color(RED)

        sc.blit(bg, (0, 0))
        for ind in range(1, len(body_parts)):
            body_parts[ind].draw(sc, ind)
        head.draw(sc)
        head.draw(sc)
        for elem in apples:
            elem.draw(sc)
        sc.blit(my_button.bg_surf, (0, 0))
        my_button.draw(sc)
        text_score.draw(sc)
        pg.display.update()
        clock.tick(FPS)


score_high = 0
head = Head(score_high)
text_score = Text("0", 32, WHITE, (W / 2 - 140, 20))
while flag_play:
    if score_high < int(text_score.score):
        score_high = head.score
    head = Head(0)
    body_parts = [head, Body((480, 200)), Body((440, 200)), Body((400, 200))]
    apples = []
    text_score = Text(str(score_high), 32, WHITE, (W / 2 - 140, 20))
    for _ in range(10):
        apples.append(Apples())
    my_button = Button("You lost, press r to reset", 32, BLACK, RED, (W // 2, H // 2))
    main()

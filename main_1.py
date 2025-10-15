import pygame as pg

FPS = 60
WIDTH, HEIGHT = 1000, 600

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("House")
clock = pg.time.Clock()

white = (255, 255, 255)
blue = (0, 0, 255)
light_blue = (126, 211, 224)
green = (70, 180, 70)
brown = (139, 69, 19)
dark_brown = (69, 57, 32)
roof_color = (178, 34, 34)
yellow = (250, 255, 0)

pg.display.update()

flag_play = True
while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    screen.fill(light_blue)
    pg.draw.rect(screen, green, (0, HEIGHT - 100, WIDTH, 100))
    pg.draw.circle(screen, yellow, (WIDTH, 0), 100)
    pg.draw.rect(screen, white, (100, HEIGHT - 250, 250, 150))
    pg.draw.polygon(screen, roof_color, [[90, HEIGHT - 250], [225, HEIGHT - 350], [360, HEIGHT - 250]])
    pg.draw.rect(screen, dark_brown, (120, HEIGHT - 200, 80, 100))
    pg.draw.rect(screen, blue, (230, HEIGHT - 230, 80, 80))
    pg.draw.rect(screen, brown, (WIDTH - 350, HEIGHT - 250, 50, 150))
    pg.draw.circle(screen, green, (WIDTH - 325, HEIGHT - 250), 80)

    pg.display.update()

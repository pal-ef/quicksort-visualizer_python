# Quick Sort Algorithm Visualizer by Efraín García Palacios
import pygame as pg
import random

pg.init()

# Display
dimensions = (800, 600)
screen = pg.display.set_mode(dimensions)
icon = pg.image.load("icon.png")
pg.display.set_caption("Quick Sort Visualizer")
pg.display.set_icon(icon)

# Useful constants
midscreen = dimensions[0] // 2

font = pg.font.SysFont('mono', 20, False)

# Background Surface
background = pg.Surface(screen.get_size())
background.fill((0, 0, 0))  # Fill with white
background = background.convert()  # Optimize Alphas
layer = pg.Surface(screen.get_size())



# Blit
screen.blit(background, (0, 0))

clock = pg.time.Clock()


# Main Loop
def draw_text(text="placeholder", pos=(10, 10), color=(255, 255, 255)):
    surface = font.render(text, True, color)
    screen.blit(surface, pos)


def random_list():
    rl = []
    for number in range(52):
        rl.append(random.randint(0, 500))
    return rl


def draw_data(data_list):
    salto = -3
    for number in data_list:
        salto += 15
        pg.draw.rect(background, (255, 255, 255), [salto, 590, 12, -number])
    # Rects
    pg.draw.rect(background, (255, 255, 255), [0, 60, dimensions[0], 1])  # Separator

    # Play Button
    pg.draw.rect(background, (255, 255, 255), [dimensions[0] - 50, 15, 33, 31])
    pg.draw.polygon(background, (0, 0, 0), ((760, 20), (760, 39), (775, 30)))


def mainloop():
    looping = True
    current_time = 0
    launch_time = 0
    first = True
    while looping:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                looping = False

        current_time = pg.time.get_ticks()
        draw_text("QUICKSORT ALGORITHM VISUALIZER | EFRAÍN GARCÍA PALACIOS", (20, 20))
        pg.display.flip()
        clock.tick(60)
        if first:
            rl = random_list()
            first = False
            launch_time = pg.time.get_ticks()
        elif current_time - launch_time > 200:
            rl = random_list()
            launch_time = pg.time.get_ticks()
        draw_data(rl)
        screen.blit(background, (0, 0))
        background.fill((0, 0, 0))


    pg.quit()


if __name__ == "__main__":
    mainloop()

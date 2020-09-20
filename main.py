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

# Useful
midscreen = dimensions[0] // 2
font = pg.font.SysFont('Arial', 20, True)
clock = pg.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)

# Background Surface
background = pg.Surface(screen.get_size())
background.fill(black)  # Fill with white
background = background.convert()  # Optimize Alphas
layer = pg.Surface(screen.get_size())

# Blit
screen.blit(background, (0, 0))


# Visualizer mechanics


# Main Loop
def draw_text(text="placeholder", pos=(10, 10), color=white):
    surface = font.render(text, True, color)
    screen.blit(surface, pos)


def random_list():
    rl = []
    for number in range(52):
        rl.append(random.randint(0, 500))
    return rl


def draw_data(data_list):
    space = -3
    for number in data_list:
        space += 15
        pg.draw.rect(background, white, [space, 590, 12, -number])

    # Rectangles
    pg.draw.rect(background, white, [0, 60, dimensions[0], 1])  # Separator

    # Play Button
    pg.draw.rect(background, white, [dimensions[0] - 50, 15, 33, 31])
    pg.draw.polygon(background, black, ((760, 20), (760, 39), (775, 30)))


def check(uncheck):
    if uncheck:
        return False
    else:
        return True


def start_button():
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    if 783 > mouse[0] > 750 and 50 > mouse[1] > 15:
        pg.draw.rect(background, (200, 100, 0), [dimensions[0] - 52, 13, 37, 36])
        if click[0] == 1:
            check(True)


def mainloop():
    looping = True
    launch_time = 0
    first = True
    not_started = check(False)
    while looping:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                looping = False

        current_time = pg.time.get_ticks()

        draw_text("QUICKSORT ALGORITHM VISUALIZER", (20, 20))
        pg.display.flip()

        if first:
            rl = random_list()
            first = False
            launch_time = pg.time.get_ticks()
        elif current_time - launch_time > 200:
            if not_started:
                rl = random_list()
                launch_time = pg.time.get_ticks()
            else:
                print("HEY IM HERE")

        start_button()
        draw_data(rl)
        screen.blit(background, (0, 0))
        background.fill(black)
        clock.tick(60)
        print(not_started)

    pg.quit()


if __name__ == "__main__":
    mainloop()

import pygame

# ====== Pygame Init ======
pygame.init()
# Size of window w -> width, h -> height
w = 800
h = 600
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
# If you want to stop game, change this value to False
is_running = True
# ------ Pygame Init ------

# ====== Main Game Loop ======
while is_running:
    for event in pygame.event.get():
        # This handle exit button
        if event.type == pygame.QUIT:
            is_running = True

    # This handle key pressed (run every time in loop, not only once)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        pass

    # ====== Game Mechanic ======

    # ------ Game Mechanic ------

    # ====== Drawing ======

    # screen.fill draws background, inside are color values
    screen.fill((0, 0, 0))
    # you can also define color as variable and use anywhere
    rect_color = (255, 100, 0)

    # In pygame is draw.rect which draws on screen window object
    # and Rect which is object with parameters like position and size
    # it can be passed as argument in draw.rect but also transformed before that
    pygame.draw.rect(screen, rect_color, pygame.Rect(x, y, 60, 60))

    # ------ Drawing ------

    # "Double buffer", it needs to be here to display game
    pygame.display.flip()
    # How many FPS will have a game
    clock.tick(60)
# ------ Main Game Loop ------

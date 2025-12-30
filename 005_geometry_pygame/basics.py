import pygame
from tools import grid, line, fill_cell, point, bezier_curve

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 750
DELAY = 2

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Shapes in Pygame")
clock = pygame.time.Clock()
running = True
timer = DELAY

a = (20,120)
b = (40,120)

font = pygame.font.SysFont("Arial", 15)
text_surface = font.render("Hello World!", True, "red")
text_rect = text_surface.get_rect()
text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

t = 0
while running:
    # poll for events
    # pygame.QUIT event means the user clicked the "X" button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("silver")
    grid(screen)
    
    #line(screen, a, b, "black")
    #fill_cell(screen, 1, 6, "lightblue")
    #point(screen, (50, 20), "red")
    
    bezier_curve(screen, t)
    dt = clock.tick(60) / 1000  # Amount of seconds between each loop
    timer -= dt
    if timer <= 0:
        t += 0.1
        if t > 1:
            t = 0
        timer = DELAY
    
    # flip the display to output our work to the screen
    pygame.display.flip()    
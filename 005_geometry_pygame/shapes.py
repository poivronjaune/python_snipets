import pygame

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Shapes in Pygame")
clock = pygame.time.Clock()
running = True

dt = 0
# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked the "X" button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("silver")

    # TOP/LEFT Corner (0, 0), as we move right horizontally, X increases - as we move vertically down, Y increases

    # Draw a simple line (screen, color, (x,y), (end_x, end_y), thickness: 0=fill)
    pygame.draw.line(screen, "black", (0, 50), (800, 50), 2)
    
    # Draw a circle (screen, color, (center_x, center_y), radius, thickness)
    pygame.draw.circle(screen, "black", (100, 150), 50, 2)
    pygame.draw.circle(screen, "black", (250, 150), 50, 0)
    
    # Draw a rectangle (screen, color, (top_left_x, top_left_y, width, height), thickness)
    pygame.draw.rect(screen, "black", (350, 100, 100, 150), 2)
    pygame.draw.rect(screen, "black", (500, 100, 100, 150), 0)
    
    
    # flip the display to output our work to the screen
    pygame.display.flip()
    

import pygame

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Shapes in Pygame")
clock = pygame.time.Clock()
running = True

def draw_bezier(list, t):
    li = list[:]
    while len(li) != 1:
        for pos, x in enumerate(li):
            if x != li[-1]:
                li[pos] = (1-t) * x[0] + t * li[pos+1][0], (1-t) * x[1] + t * li[pos+1][1]

        li.pop()
    return li[0]

points = [(5, 5), (20, 60), (120, 50)]
points = [(x[0], 600-x[1]) for x in points]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("silver")

    t = 0
    while t <= 1:
        point = draw_bezier(points, t)
        screen.fill((0, 0, 0), (point, (1, 1)))
        t += 0.001
    clock.tick(20)

    # flip the display to output our work to the screen
    pygame.display.flip()
    

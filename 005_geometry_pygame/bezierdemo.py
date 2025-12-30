# https://www.pygame.org/wiki/BezierCurve

import time
import numpy as np
import pygame 
CELL_SIZE = 20

def line(screen, start, end, color):
    pygame.draw.line(screen, color, start, end, width=1)

def show_text(screen, position, text, color):
    font = pygame.font.SysFont("Arial", 15)
    text = font.render(text, True, color)
    text_rect = text.get_rect()
    text_rect.center = position
    screen.blit(text, text_rect)
    
def show_coordinates(screen, position, color):
    font = pygame.font.SysFont("Arial", 15)
    x,y = position
    x_surface = font.render(f"x: {int(x)}", True, color)
    x_rect = x_surface.get_rect()
    x_rect.center = x-10, y+15
    y_surface = font.render(f"y: {int(y)}", True, color)
    y_rect = y_surface.get_rect()
    y_rect.center = x-10, y+30
    
    screen.blit(x_surface, x_rect)
    screen.blit(y_surface, y_rect)
    
def point(screen, position, color, radius=CELL_SIZE/3):
    pygame.draw.circle(screen, color, position, radius=radius)
    show_coordinates(screen, position, color)

def grid(screen, cell_size=CELL_SIZE, grid_color="lightgray", ruler=True, ruler_color="black"):
    # Draw the grid lines
    width, height = screen.get_size()
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, grid_color, (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, grid_color, (0, y), (width, y))

    if ruler:
        for y in range(0, height, cell_size):
            line(screen, (0, y), (cell_size, y), ruler_color)  # Left border
        for x in range(0, width, cell_size):
            line(screen, (x, height), (x, height-cell_size), ruler_color)  # Top border

def fill_cell(screen, cell_x, cell_y, color, cell_size=CELL_SIZE):
    rect = pygame.Rect(cell_x * cell_size, cell_y * cell_size, cell_size, cell_size)
    pygame.draw.rect(screen, color, rect)
    
def bezier_curve(screen, t=0.2):
    p0 = (100, 500)
    p1 = (600, 200)
    p2 = (1000, 400)
    
    pa = (p0[0] + (p1[0] - p0[0]) * t, p0[1] + (p1[1] - p0[1]) * t)
    pb = (p1[0] + (p2[0] - p1[0]) * t, p1[1] + (p2[1] - p1[1]) * t)

    show_text(screen, (150, 50), f"t: {t:.2f}", "black")

    point(screen=screen, position=p0, color="black")
    point(screen=screen, position=p1, color="black")
    point(screen=screen, position=pa, color="red")
    line(screen, p0, pa, "red")

    point(screen=screen, position=p2, color="black")
    point(screen=screen, position=pb, color="red")
    line(screen, p1, pb, "red")
    
    line(screen, pa, pb, "blue")
    

    # Linear interpolation : 
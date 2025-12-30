# PYGame Gemotric Shapes  

Ref: []()

### Dependencies
```
pip install -e .
```
See pyproject.toml  

# PYGAME Concepts
Initialize pygame, then set display mode to a screen size.  Caption appears in the window header and window close can be used (called events)
- pygame.init()
- screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
- pygame.display.set_caption("Shapes in Pygame")
- clock = pygame.time.Clock()

The pygame.time.Clock is essential for creating smooth, consistent, and platform-independent gameplay. Its primary purposes are controlling the game's frame rate (FPS) and calculating the time elapsed between frames.  

## Game Loop  
To display a pygame program a game loop must be initiated and events, drawing and other actions will be performed in that loop.  
An events manager section will detect events and apply actions accordingly.  

Example QUIT  
```
while running:
    # poll for events
    # pygame.QUIT event means the user clicked the "X" button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
```  


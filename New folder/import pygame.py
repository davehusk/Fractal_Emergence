import pygame
import math

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
RING_RADIUS = 50
RING_SPEED = 2

# Set up some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create two vortex rings
ring1 = {
    'pos': (WIDTH // 2 - RING_RADIUS, HEIGHT // 2),
    'vel': (RING_SPEED, 0),
    'color': RED
}

ring2 = {
    'pos': (WIDTH // 2 + RING_RADIUS, HEIGHT // 2),
    'vel': (-RING_SPEED, 0),
    'color': BLUE
}

# Set up the clock
clock = pygame.time.Clock()

# Run the main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the positions of the vortex rings
    ring1['pos'] = (ring1['pos'][0] + ring1['vel'][0], ring1['pos'][1] + ring1['vel'][1])
    ring2['pos'] = (ring2['pos'][0] + ring2['vel'][0], ring2['pos'][1] + ring2['vel'][1])

    # Check for collision
    if math.dist(ring1['pos'], ring2['pos']) < 2 * RING_RADIUS:
        # Merge the vortex rings
        ring1['vel'] = (0, 0)
        ring2['vel'] = (0, 0)
        ring1['pos'] = (WIDTH // 2, HEIGHT // 2)
        ring2['pos'] = (WIDTH // 2, HEIGHT // 2)

    # Draw the vortex rings
    screen.fill(WHITE)
    pygame.draw.circle(screen, ring1['color'], ring1['pos'], RING_RADIUS)
    pygame.draw.circle(screen, ring2['color'], ring2['pos'], RING_RADIUS)

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
BALL_RADIUS = 10
BALL_SPEED = 5

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a ball object
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_vel = [BALL_SPEED, -BALL_SPEED]

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Bounce off walls
    if ball_pos[0] - BALL_RADIUS < 0 or ball_pos[0] + BALL_RADIUS > WIDTH:
        ball_vel[0] = -ball_vel[0]
    if ball_pos[1] - BALL_RADIUS < 0 or ball_pos[1] + BALL_RADIUS > HEIGHT:
        ball_vel[1] = -ball_vel[1]

    # Draw ball
    pygame.draw.circle(screen, (255, 0, 0), ball_pos, BALL_RADIUS)

    # Flip display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 1000
BACKGROUND_COLOR = (255, 255, 255)
BOARD_COLOR = (0, 0, 0)
GRID_SIZE = 200

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ludo Game")

# Function to draw the Ludo board
def draw_board():
    # Draw the main squares
    pygame.draw.rect(screen, (255, 0, 0), (0, 0, GRID_SIZE, GRID_SIZE))  # Red section
    pygame.draw.rect(screen, (0, 255, 0), (WIDTH - GRID_SIZE, 0, GRID_SIZE, GRID_SIZE))  # Green section
    pygame.draw.rect(screen, (0, 0, 255), (0, HEIGHT - GRID_SIZE, GRID_SIZE, GRID_SIZE))  # Blue section
    pygame.draw.rect(screen, (255, 255, 0), (WIDTH - GRID_SIZE, HEIGHT - GRID_SIZE, GRID_SIZE, GRID_SIZE))  # Yellow section

    # Draw the center area
    pygame.draw.rect(screen, (255, 255, 255), (GRID_SIZE, GRID_SIZE, WIDTH - 2 * GRID_SIZE, HEIGHT - 2 * GRID_SIZE))
    
    # Draw the paths
    pygame.draw.rect(screen, (255, 0, 0), (GRID_SIZE, HEIGHT//2 - 25, WIDTH - 2 * GRID_SIZE, 50))  # Red path
    pygame.draw.rect(screen, (0, 255, 0), (WIDTH//2 - 25, GRID_SIZE, 50, HEIGHT - 2 * GRID_SIZE))  # Green path
    pygame.draw.rect(screen, (0, 0, 255), (GRID_SIZE, HEIGHT//2 - 25, WIDTH - 2 * GRID_SIZE, 50))  # Blue path
    pygame.draw.rect(screen, (255, 255, 0), (WIDTH//2 - 25, GRID_SIZE, 50, HEIGHT - 2 * GRID_SIZE))  # Yellow path
    
    # Draw the home areas
    pygame.draw.rect(screen, (255, 0, 0), (WIDTH // 4 - 40, HEIGHT // 4 - 40, 80, 80))  # Red home
    pygame.draw.rect(screen, (0, 255, 0), (3 * WIDTH // 4 - 40, HEIGHT // 4 - 40, 80, 80))  # Green home
    pygame.draw.rect(screen, (0, 0, 255), (WIDTH // 4 - 40, 3 * HEIGHT // 4 - 40, 80, 80))  # Blue home
    pygame.draw.rect(screen, (255, 255, 0), (3 * WIDTH // 4 - 40, 3 * HEIGHT // 4 - 40, 80, 80))  # Yellow home

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)
    draw_board()
    pygame.display.flip()

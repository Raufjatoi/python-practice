import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
BACKGROUND_COLOR = (0, 0, 0)
DICE_COLOR = (255, 255, 255)
DICE_POSITION = (150, 150)
DICE_SIZE = 100
ROLLING_FRAMES = 10  # Number of frames to show while rolling

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dice Roll Animation')

# Function to draw the dice face
def draw_dice(number):
    screen.fill(BACKGROUND_COLOR)  # Fill the background
    pygame.draw.rect(screen, DICE_COLOR, (DICE_POSITION[0], DICE_POSITION[1], DICE_SIZE, DICE_SIZE), 0, 10)  # Draw the dice

    # Draw dots based on the dice number
    dot_positions = {
        1: [(DICE_POSITION[0] + DICE_SIZE // 2, DICE_POSITION[1] + DICE_SIZE // 2)],
        2: [(DICE_POSITION[0] + DICE_SIZE // 4, DICE_POSITION[1] + DICE_SIZE // 4),
            (DICE_POSITION[0] + 3 * DICE_SIZE // 4, DICE_POSITION[1] + 3 * DICE_SIZE // 4)],
        3: [(DICE_POSITION[0] + DICE_SIZE // 4, DICE_POSITION[1] + DICE_SIZE // 4),
            (DICE_POSITION[0] + DICE_SIZE // 2, DICE_POSITION[1] + DICE_SIZE // 2),
            (DICE_POSITION[0] + 3 * DICE_SIZE // 4, DICE_POSITION[1] + 3 * DICE_SIZE // 4)],
        4: [(DICE_POSITION[0] + DICE_SIZE // 4, DICE_POSITION[1] + DICE_SIZE // 4),
            (DICE_POSITION[0] + 3 * DICE_SIZE // 4, DICE_POSITION[1] + DICE_SIZE // 4),
            (DICE_POSITION[0] + DICE_SIZE // 4, DICE_POSITION[1] + 3 * DICE_SIZE // 4),
            (DICE_POSITION[0] + 3 * DICE_SIZE // 4, DICE_POSITION[1] + 3 * DICE_SIZE // 4)],
        5: [(DICE_POSITION[0] + DICE_SIZE // 4, DICE_POSITION[1] + DICE_SIZE // 4),
            (DICE_POSITION[0] + 3 * DICE_SIZE // 4, DICE_POSITION[1] + DICE_SIZE // 4),
            (DICE_POSITION[0] + DICE_SIZE // 2, DICE_POSITION[1] + DICE_SIZE // 2),
            (DICE_POSITION[0] + DICE_SIZE // 4, DICE_POSITION[1] + 3 * DICE_SIZE // 4),
            (DICE_POSITION[0] + 3 * DICE_SIZE // 4, DICE_POSITION[1] + 3 * DICE_SIZE // 4)],
        6: [(DICE_POSITION[0] + DICE_SIZE // 4, DICE_POSITION[1] + DICE_SIZE // 4),
            (DICE_POSITION[0] + 3 * DICE_SIZE // 4, DICE_POSITION[1] + DICE_SIZE // 4),
            (DICE_POSITION[0] + DICE_SIZE // 4, DICE_POSITION[1] + DICE_SIZE // 2),
            (DICE_POSITION[0] + 3 * DICE_SIZE // 4, DICE_POSITION[1] + DICE_POSITION[1] + DICE_SIZE // 2),
            (DICE_POSITION[0] + DICE_SIZE // 4, DICE_POSITION[1] + 3 * DICE_SIZE // 4),
            (DICE_POSITION[0] + 3 * DICE_SIZE // 4, DICE_POSITION[1] + 3 * DICE_SIZE // 4)],
    }

    for position in dot_positions[number]:
        pygame.draw.circle(screen, BACKGROUND_COLOR, position, 10)

def roll_dice():
    for _ in range(ROLLING_FRAMES):
        dice_number = random.randint(1, 6)  # Random dice number
        draw_dice(dice_number)
        pygame.display.flip()  # Update the display
        time.sleep(0.1)  # Delay for animation effect

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:  # Roll the dice on mouse click
            roll_dice()  # Call the rolling function

    pygame.display.flip()  # Update the display

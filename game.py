import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 300 , 300
LINE_COLOR = (255, 255, 255) # white yk RGB
BACKGROUND_COLOR = (0, 0, 0) # black same rgb thin
X_COLOR = (255, 0, 0) # red
O_COLOR = (0, 0, 255) # blue 

board = [['' for _ in range(3)] for _ in range(3)]
current_player = 'X'

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')

def draw_board():
    screen.fill(BACKGROUND_COLOR)
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, i * 100), (WIDTH, i * 100), 5)
        pygame.draw.line(screen, LINE_COLOR, (i * 100, 0), (i * 100, HEIGHT), 5)

def draw_markers():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                pygame.draw.line(screen, X_COLOR, (col * 100 + 20, row * 100 + 20), (col * 100 + 80, row * 100 + 80), 5)
                pygame.draw.line(screen, X_COLOR, (col * 100 + 20, row * 100 + 80), (col * 100 + 80, row * 100 + 20), 5)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, O_COLOR, (col * 100 + 50, row * 100 + 50), 40, 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            clicked_row = mouseY // 100
            clicked_col = mouseX // 100

            if board[clicked_row][clicked_col] == '':
                board[clicked_row][clicked_col] = current_player
                current_player = 'O' if current_player == 'X' else 'X'

    draw_board()
    draw_markers()
    pygame.display.flip()

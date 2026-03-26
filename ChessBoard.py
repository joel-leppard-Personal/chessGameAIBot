import pygame

pygame.init()
board = pygame.display.set_mode((800, 800))

squareSize = 80

for row in range(8):
    for column in range(8):
        colour = (0, 0, 0) if (row+column) % 2 else (255, 255, 255)
        pygame.draw.rect(board,colour,(column * squareSize, row * squareSize, squareSize, squareSize))

pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
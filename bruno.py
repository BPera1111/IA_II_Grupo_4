import pygame
import sys

# Inicializar pygame
pygame.init()

# Definir algunos colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Configurar el tamaño de la pantalla
ANCHO=40
COLUMNAS=8
FILAS=16
WIDTH, HEIGHT = ANCHO*COLUMNAS, ANCHO*FILAS
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tablero de Búsqueda")

# Definir el tamaño de cada celda y la matriz de ejemplo
CELL_SIZE = ANCHO
tablero = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 0, 0, 25, 26, 0],
    [0, 3, 4, 0, 0, 27, 28, 0],
    [0, 5, 6, 0, 0, 29, 30, 0],
    [0, 7, 8, 0, 0, 31, 32, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 9, 10, 0, 0, 33, 34, 0],
    [0, 11, 12, 0, 0, 35, 36, 0],
    [0, 13, 14, 0, 0, 37, 38, 0],
    [0, 15, 16, 0, 0, 39, 40, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 17, 18, 0, 0, 41, 42, 0],
    [0, 19, 20, 0, 0, 43, 44, 0],
    [0, 21, 22, 0, 0, 45, 46, 0],
    [0, 23, 24, 0, 0, 47, 48, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

# Función para dibujar el tablero
def draw_board():
    for y in range(16):
        for x in range(8):
            color = BLACK if tablero[y][x] == 0 else BLUE
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, WHITE, rect, 1)  # Esta línea dibuja un rectángulo blanco alrededor de cada celda


# Función principal
def main():
    running = True
    while running:
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Dibujar el tablero
        screen.fill(WHITE)  # Rellenar la pantalla con blanco
        draw_board()
        
        # Actualizar la pantalla
        pygame.display.flip()
    
    # Salir de pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

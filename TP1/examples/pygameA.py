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
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tablero de Búsqueda")

# Definir el tamaño de cada celda y la matriz de ejemplo
CELL_SIZE = WIDTH // 10
tablero = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Función para dibujar el tablero
def draw_board():
    for y in range(10):
        for x in range(10):
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

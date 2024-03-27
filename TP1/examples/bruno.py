import pygame
import sys


filas = 21  # Puedes cambiar este valor según tus necesidades
columnas = 19  # Puedes cambiar este valor según tus necesidades

# Inicializar una lista vacía para contener la matriz
matriz = []

# Generar la matriz con las características requeridas
for i in range(filas):
    fila = []
    for j in range(columnas):
        # Verificar si la fila o la columna son múltiplos de 4 (para filas y columnas basadas en 0)
        if i % 5 == 0 or i == 0 or j == 0 or j % 3 == 0:
            fila.append(0)
        else:
            fila.append(1)
    matriz.append(fila)

# Imprimir la matriz con formato
for fila in matriz:
    print(fila)

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
COLUMNAS=19
FILAS=16
WIDTH, HEIGHT = ANCHO*COLUMNAS, ANCHO*FILAS
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tablero de Búsqueda")

# Definir el tamaño de cada celda y la matriz de ejemplo
CELL_SIZE = ANCHO
# Función para dibujar el tablero
def draw_board():
    for y in range(FILAS):
        for x in range(COLUMNAS):
            color = BLACK if matriz[y][x] == 0 else WHITE
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

import pygame
import sys
import threading

# Inicializar pygame
pygame.init()

# Definir algunos colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CIAN = (0, 255, 255)
color_dict = {0: BLACK, "r": RED, "g": GREEN, "w": WHITE, "c": CIAN}

# Configurar el tamaño de la pantalla
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tablero de Búsqueda")

# Función para dibujar el tablero
def draw_board(tablero):
    CELL_SIZE = WIDTH // len(tablero)
    for y in range(len(tablero)):
        for x in range(len(tablero[0])):
            color = color_dict.get(tablero[y][x],BLUE)
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, WHITE, rect, 1)  # Esta línea dibuja un rectángulo blanco alrededor de cada celda


# Función principal
def muestra(tablero):
    running = True
    while running:
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Dibujar el tablero
        # screen.fill(WHITE)  # Rellenar la pantalla con blanco
        draw_board(tablero)
        
        # Actualizar la pantalla
        pygame.display.flip()
    
    # Salir de pygame
    pygame.quit()
    sys.exit()

#Crear hilo para mostrar el tablero
def mostrar_tablero(tablero):
    t = threading.Thread(target=muestra, args=(tablero,))
    t.start()

# Función para actualizar la pantalla
def actualiza_pantalla(nuevo_tablero):
    # screen.fill(WHITE)  # Rellenar la pantalla con blanco
    draw_board(nuevo_tablero)
    pygame.display.flip()
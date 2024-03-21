import pygame
import sys

# Definimos clase Estatne en donde estará el producto con su posicionamiento
class Estante:
    def __init__(self, ex, ey, producto):
        self.id = producto
        self.ex = ex
        self.ey = ey
    
    def asignarProducto(self, producto):
        self.productos = producto

# Definimos la clase estanteria que contendrá los distintos estantes con productos
class Estanteria:
    def __init__(self, id):
        self.id = id
        self.estantes = []
        
    def agregarEstante(self, estante):
        self.estantes.append(estante)
        
    def quitarEstante(self, estante):
        if estante in self.estantes:
            self.estantes

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

# N° de filas, N° de columnas y N° de estanterias
estructuraEstanteria = [4, 2, 6] 

estanterias = []
#armado de tablero
tablero = []
for y in range(1,2):
    pass

for e in range(1,estructuraEstanteria[2]):
    estanterias.append(Estanteria(id=e))
    salto = 0
    if (e%3) == 0:
        salto += 1
    


# Definir el tamaño de cada celda y la matriz de ejemplo
# CELL_SIZE = WIDTH // 10
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

CELL_SIZE = WIDTH // len(tablero)

# Función para dibujar el tablero
def draw_board():
    for y in range(len(tablero)):
        for x in range(len(tablero[0])):
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

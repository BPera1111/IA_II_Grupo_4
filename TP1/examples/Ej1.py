import pygame
import sys

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)

# Dimensiones del tablero y tamaño de cada celda
ANCHO_CELDA = 40
NUM_COLUMNAS = 7
NUM_FILAS = 16
ANCHO_TABLERO = ANCHO_CELDA * NUM_COLUMNAS
ALTO_TABLERO = ANCHO_CELDA * NUM_FILAS

bloques_azules = [(1,1),(4,1),(1,6),(4,6),(1,11),(4,11)]

def dibujar_tablero(screen):
    for fila in range(NUM_FILAS):
        for columna in range(NUM_COLUMNAS):
            pygame.draw.rect(screen, BLANCO, (columna * ANCHO_CELDA, fila * ANCHO_CELDA, ANCHO_CELDA, ANCHO_CELDA), 1)

def dibujar_bloques(screen, bloques):
    for pos in bloques:
        x, y = pos
        pygame.draw.rect(screen, AZUL, (x * ANCHO_CELDA, y * ANCHO_CELDA, ANCHO_CELDA * 2, ANCHO_CELDA * 4))

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO_TABLERO, ALTO_TABLERO))
    pygame.display.set_caption("Tablero de 7x16 con bloques azules")
    pantalla.fill(NEGRO)
    
    dibujar_tablero(pantalla)
    dibujar_bloques(pantalla, bloques_azules)

    # Dibujar un bloque azul en la posición (fila, columna)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main()

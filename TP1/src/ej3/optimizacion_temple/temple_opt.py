import pygame
import sys

filas = 11  
columnas = 7
matriz = []

# Genera la matriz 
k = 1
for i in range(filas):
    fila = []
    for j in range(columnas):
        # Verificar si la fila o la columna son múltiplos de 4 (para filas y columnas basadas en 0)
        if i % 5 == 0 or i == 0 or j == 0 or j % 3 == 0:
            fila.append(0)
        else:
            fila.append(k)
            k = k + 1

    matriz.append(fila)


def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()

#imprimir_matriz(matriz)
        

posiciones_productos = []
punto1 = []
punto2 = []

for x, i in enumerate(matriz):
    for y, j in enumerate(i):
        if j != 0:
            v = [x, y]
            posiciones_productos.append(v)
            if matriz[x][y-1] == 0:
                p1 = [x, y-1]
                punto1.append(p1)
                if matriz[x-1][y] == 0:
                    p2 = [x-1, y]
                    punto2.append(p2)
                elif matriz[x+1][y] == 0:
                    p2 = [x+1, y]
                    punto2.append(p2)
                else:
                    punto2.append(p1)

            else:
                p1 = [x, y+1]
                punto1.append(p1)
                if matriz[x-1][y] == 0:
                    p2 = [x-1, y]
                    punto2.append(p2)
                elif matriz[x+1][y] == 0:
                    p2 = [x+1, y]
                    punto2.append(p2)
                else:
                    punto2.append(p1)
            
print("Vector 1: ", punto1)
print("Vector 2: ",punto2)

#print(posiciones_productos)



import pygame
import sys

# Inicializar Pygame
pygame.init()

# Tamaño de la ventana y tamaño de cada celda
ANCHO = 800
ALTO = 600
CELDA_SIZE = 30

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

def dibujar_tablero(matriz, coordenadas1, coordenadas2, pantalla):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            color = BLANCO if matriz[fila][columna] == 0 else NEGRO
            pygame.draw.rect(pantalla, color, (columna * CELDA_SIZE, fila * CELDA_SIZE, CELDA_SIZE, CELDA_SIZE))
    
    for coordenada in coordenadas1:
        fila, columna = coordenada
        pygame.draw.rect(pantalla, VERDE, (columna * CELDA_SIZE, fila * CELDA_SIZE, CELDA_SIZE, CELDA_SIZE))

    for coordenada in coordenadas2:
        fila, columna = coordenada
        pygame.draw.rect(pantalla, AZUL, (columna * CELDA_SIZE, fila * CELDA_SIZE, CELDA_SIZE, CELDA_SIZE))

def main(matriz, coordenadas1, coordenadas2):
    # Inicializar la ventana
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Tablero")

    reloj = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pantalla.fill(BLANCO)
        dibujar_tablero(matriz, coordenadas1, coordenadas2, pantalla)
        pygame.display.flip()

        reloj.tick(60)

# Ejemplo de matriz y coordenadas


# Llamar a la función principal
main(matriz, punto1, punto2)

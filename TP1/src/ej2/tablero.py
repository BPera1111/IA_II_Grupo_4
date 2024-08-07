import draw as draw

class tablero:

    def __init__(self,filas,columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = None
        self.crear_tablero()


    def crear_tablero(self): #crea el tablero y asigna valor de estanteria
        # Inicializar una lista vacía para contener la matriz
        self.matriz = []
        x=0
        # Generar la matriz con las características requeridas
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                # Verificar si la fila o la columna son múltiplos de 4 (para filas y columnas basadas en 0)
                if i % 5 == 0 or i == 0 or j == 0 or j % 3 == 0:
                    fila.append(0)
                else:
                    x+=1
                    fila.append(x)
            self.matriz.append(fila)
        
        
        
    def actualiza_tablero(self, x, y, valor): #actualiza el tablero con función de draw.py
        self.matriz[x][y] = valor
        draw.actualiza_pantalla(self.matriz)
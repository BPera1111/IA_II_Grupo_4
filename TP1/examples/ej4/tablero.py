import random

class tablero:

    def __init__(self,filas,columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = None
        self.crear_tablero()


    def crear_tablero(self): #retorna la matriz (tablero)
        # Inicializar una lista vacía para contener la matriz
        self.matriz = []
        valores_posibles=list(range(1,193))
        # Generar la matriz con las características requeridas
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                # Verificar si la fila o la columna son múltiplos de 4 (para filas y columnas basadas en 0)
                if i % 5 == 0 or i == 0 or j == 0 or j % 3 == 0:
                    fila.append(0)
                else:
                    valor_aleatorio=random.choice(valores_posibles)
                    fila.append(valor_aleatorio)
                    valores_posibles.remove(valor_aleatorio)
            self.matriz.append(fila)
        
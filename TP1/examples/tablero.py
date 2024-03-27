
# Definir las dimensiones de la matriz
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



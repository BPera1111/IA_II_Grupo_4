import numpy as np

def trasponer_matriz(matriz):
    # Convertimos la matriz a un array de NumPy
    array_matriz = np.array(matriz)
    # Aplicamos la función de transposición de NumPy
    matriz_transpuesta = np.transpose(array_matriz)
    
    return matriz_transpuesta.tolist()  # Convertimos el array NumPy de nuevo a una lista de Python

# Ejemplo de uso:
matriz_original = [(1,1),(1,2),(2,1),(2,2),(3,1),(3,2),(4,1),(4,2),(6,1),(6,2),(7,1),(7,2),(8,1),(8,2),(9,1),(9,2),(11,1),(11,2),(12,1),(12,2),(13,1),(13,2),(14,1),(14,2),(1,4),(1,5),(2,4),(2,5),(3,4),(3,5),(4,4),(4,5),(6,4),(6,5),(7,4),(7,5),(8,4),(8,5),(9,4),(9,5),(11,4),(11,5),(12,4),(12,5),(13,4),(13,5),(14,4),(14,5)]


matriz_transpuesta = trasponer_matriz(matriz_original)
print(matriz_transpuesta)

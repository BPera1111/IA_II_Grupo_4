import random

def generar_estado_actual_aleatorio(vector1, vector2):
    # Generar una permutación aleatoria
    permutation = list(range(1, len(vector1) - 1))  # Excluir el primer y último elemento
    random.shuffle(permutation)

    # Mantener las primeras y últimas componentes intactas
    primera_componente1 = vector1[0]
    ultima_componente1 = vector1[-1]
    primera_componente2 = vector2[0]
    ultima_componente2 = vector2[-1]

    # Desordenar las componentes intermedias utilizando la misma permutación para ambos vectores
    componentes_intermedias1 = [vector1[i] for i in permutation]
    componentes_intermedias2 = [vector2[i] for i in permutation]

    # Reconstruir los vectores con las componentes desordenadas
    vector_desordenado1 = [primera_componente1] + componentes_intermedias1 + [ultima_componente1]
    vector_desordenado2 = [primera_componente2] + componentes_intermedias2 + [ultima_componente2]
    
    return vector_desordenado1, vector_desordenado2

# Ejemplo de uso:
vector1_original = [1, 2, 3, 4, 5, 6, 7, 8, 9]
vector2_original = [1, 8, 7, 6, 5, 4, 3, 2, 9]
vector_desordenado1, vector_desordenado2 = generar_estado_actual_aleatorio(vector1_original, vector2_original)

print("Vector 1 desordenado:", vector_desordenado1)
print("Vector 2 desordenado:", vector_desordenado2)


import random
import numpy as np

def updateNetwork(population, bestScore):
    # ===================== ESTA FUNCIÓN RECIBE UNA POBLACIÓN A LA QUE SE DEBEN APLICAR MECANISMOS DE SELECCIÓN, =================
    # ===================== CRUCE Y MUTACIÓN. LA ACTUALIZACIÓN DE LA POBLACIÓN SE APLICA EN LA MISMA VARIABLE ====================
    best = select_fittest(population, bestScore)

    for i in range(len(population)):
        child = evolve(best[0], best[1])
        population[i].b1 = child[0]
        population[i].b2 = child[1]
        population[i].w1 = child[2]
        population[i].w2 = child[3]




    # =============================================================================================================================

def select_fittest(population, bestScore):
    # Ordenar la población en función del atributo score de forma descendente
    sorted_population = sorted(population, key=lambda x: x.score, reverse=True)
    if sorted_population[0].score <= bestScore:
        sorted_population_0 = sorted_population
        return sorted_population_0[:2]
    # Devolver los dos primeros elementos de la población ordenada



    return sorted_population[:2]

def evolve(element1, element2):
    # ===================== FUNCIÓN DE CRUCE Y MUTACIÓN =====================
    # Realizar el cruce y mutación de los atributos de los elementos
    b1_child = crossover_and_mutation(element1.b1, element2.b1)
    b2_child = crossover_and_mutation(element1.b2, element2.b2)
    w1_child = crossover_and_mutation(element1.w1, element2.w1)
    w2_child = crossover_and_mutation(element1.w2, element2.w2)

    # Crear un nuevo objeto hijo con los atributos cruzados y mutados
    child =[b1_child, b2_child, w1_child, w2_child]

    # Devolver el objeto hijo
    return child
    pass


def crossover_and_mutation(matrix1, matrix2):
    # Obtener las dimensiones de las matrices
    rows, cols = matrix1.shape
    
    # Realizar el cruce y mutación de los elementos de las matrices
    child_matrix = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            # Realizar el cruce y mutación de cada elemento
            if random.random() < 0.5:
                child_matrix[i][j] = matrix1[i][j]
            else:
                child_matrix[i][j] = matrix2[i][j]
                
            if random.random() < 0.1:
                child_matrix[i][j] += random.uniform(-0.1, 0.1)
    
    # Devolver la matriz cruzada y mutada
    return child_matrix

# ===============================================================

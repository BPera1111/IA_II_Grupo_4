import random
import numpy as np

def updateNetwork(population, bestScore):
    # ===================== ESTA FUNCIÓN RECIBE UNA POBLACIÓN A LA QUE SE DEBEN APLICAR MECANISMOS DE SELECCIÓN, =================
    # ===================== CRUCE Y MUTACIÓN. LA ACTUALIZACIÓN DE LA POBLACIÓN SE APLICA EN LA MISMA VARIABLE ====================

    population = select_fittest(population)
    

    for i in range(0, len(population), 2):
        # ===================== APLICAR CRUCE Y MUTACIÓN =====================
        child_1, child_2 = evolve(population[0], population[1])
        # ==================================================================
        population[i] = child_1
        population[i+1] = child_2




    # =============================================================================================================================

def select_fittest(population):
    # Ordenar la población en función del atributo score de forma descendente
    sorted_population = sorted(population, key=lambda x: x.score, reverse=True)
    # Guardar el mejor individuo
    try:
        if sorted_population[0].score > best_h.score:
            best_h = sorted_population[0]

        else:
            sorted_population.append(best_h)
            sorted_population.remove(sorted_population[-1])
            
    except:
        best_h = sorted_population[0]



    return sorted_population[:2]

def evolve(element1, element2):
    # ===================== FUNCIÓN DE CRUCE Y MUTACIÓN =====================
    # Realizar el cruce y mutación de los atributos de los elementos
    cross_prob = 1
    mut_prob = 0.25

    if random.random() < cross_prob:
        b1_child_1,b1_child_2 = crossover(element1.b1, element2.b1)
        b2_child_1,b2_child_2 = crossover(element1.b2, element2.b2)
        w1_child_1,w1_child_2 = crossover(element1.w1, element2.w1)
        w2_child_1,w2_child_2 = crossover(element1.w2, element2.w2)

    elif random.random() < mut_prob:
        b1_child = mutation(b1_child)
        b2_child = mutation(b2_child)
        w1_child = mutation(w1_child)
        w2_child = mutation(w2_child)
    # Crear un nuevo objeto hijo con los atributos cruzados y mutados
    child_1 =[b1_child_1, b2_child_1, w1_child_1, w2_child_1]
    child_2 =[b1_child_2, b2_child_2, w1_child_2, w2_child_2]

    return child_1, child_2



def crossover(matrix1, matrix2):
    # Obtener las dimensiones de las matrices
    assert matrix1.shape == matrix2.shape, "Los padres deben tener la misma forma"
    # Crear un punto de cruce aleatorio
    crossover_point = np.random.randint(1, matrix1.size)
    # Aplanar las matrices para facilitar el cruce
    flat_matrix1 = matrix1.flatten()
    flat_matrix2 = matrix2.flatten()
    # Realizar el cruce
    new_flat_matrix1 = np.concatenate([flat_matrix1[:crossover_point], flat_matrix2[crossover_point:]])
    new_flat_matrix2 = np.concatenate([flat_matrix2[:crossover_point], flat_matrix1[crossover_point:]])
    # Reformar los individuos a su forma original
    new_matrix1 = new_flat_matrix1.reshape(matrix1.shape)
    new_matrix2 = new_flat_matrix2.reshape(matrix2.shape)
    # Devolver los nuevos valores de las matrices
    return new_matrix1, new_matrix2

def mutation(matrix):
    # ===================== FUNCIÓN DE MUTACIÓN =====================
    # Crear una matriz de mutación con valores aleatorios de una distribución normal
    mutation_matrix = np.random.randn(matrix.shape[0], matrix.shape[1])
    # Aplicar la mutación a la matriz original
    mutated_matrix = matrix + mutation_matrix
    # Devolver la matriz mutada
    return mutated_matrix

# ===============================================================

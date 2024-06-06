import random
import numpy as np
import pickle
import copy

best_h = []  # Variable global para almacenar el mejor individuo
best_anterior = []  # Variable global para almacenar el mejor individuo de la generación anterior

def updateNetwork(population):
    global best_h
    
    # Seleccionar los más aptos y mantener el mejor individuo
    population = select_fittest(population)
    popu_id = []
    popu_w1 = []
    try:
        for i in range(len(population)):
            popu_id.append(population[i].id)
            popu_w1.append(round(population[i].w1[0,0], 3))
    except: pass
    # Aplicar cruce y mutación
    for i in range(0, len(population)//4):
        population[i].b1 = best_h[i][0]
        population[i].b2 = best_h[i][1]
        population[i].w1 = best_h[i][2]
        population[i].w2 = best_h[i][3]


    for i in range(len(population)//4 + 1, len(population)-1, 2):
        j = random.randint(0, len(population)//4 - 1)
        x = random.randint(0, len(population)//4 - 1)
        child_1, child_2 = evolve(population[j], population[x])
        
        population[i].b1 = child_1[0]
        population[i].b2 = child_1[1]
        population[i].w1 = child_1[2]
        population[i].w2 = child_1[3]
        population[i+1].b1 = child_2[0]
        population[i+1].b2 = child_2[1]
        population[i+1].w1 = child_2[2]
        population[i+1].w2 = child_2[3]

    popu_id2 = []
    popu_w12 = []
    try:
        for i in range(len(population)):
            popu_id2.append(population[i].id)
            popu_w12.append(round(population[i].w1[0,0], 3))
    except: pass
    return population

def select_fittest(population):
    global best_h, best_anterior


    # Ordenar la población en función del atributo score de forma descendente
    popu_ordenada = sorted(population, key=lambda x: x.score, reverse=True)
    # Guardar los atributos b1, b2, w1 y w2 del cuarto superior de la población
    for i in range(0, len(popu_ordenada)//4):
        best_h.append([popu_ordenada[i].b1, popu_ordenada[i].b2, popu_ordenada[i].w1, popu_ordenada[i].w2])    
    
    try:
        # Si la mejor puntuación de la generación actual es mayor que la de la anterior generación se guarda el mejor individuo
        if popu_ordenada[0].score > best_anterior[0].score:
            best_anterior = best_h
        else:
            best_h = best_anterior
    except:
        best_anterior = best_h.copy()

    


    return popu_ordenada

def evolve(element1, element2):
    # Probabilidades de cruce y mutación
    cross_prob = 1
    mut_prob = 0.3

    if random.random() < cross_prob:
        b1_child_1, b1_child_2 = crossover(element1.b1, element2.b1)
        b2_child_1, b2_child_2 = crossover(element1.b2, element2.b2)
        w1_child_1, w1_child_2 = crossover(element1.w1, element2.w1)
        w2_child_1, w2_child_2 = crossover(element1.w2, element2.w2)
    else:
        b1_child_1, b1_child_2 = element1.b1, element2.b1
        b2_child_1, b2_child_2 = element1.b2, element2.b2
        w1_child_1, w1_child_2 = element1.w1, element2.w1
        w2_child_1, w2_child_2 = element1.w2, element2.w2

    if random.random() < mut_prob:
        b1_child_1 = mutation(b1_child_1)
        b1_child_2 = mutation(b1_child_2)
        b2_child_1 = mutation(b2_child_1)
        b2_child_2 = mutation(b2_child_2)
        w1_child_1 = mutation(w1_child_1)
        w1_child_2 = mutation(w1_child_2)
        w2_child_1 = mutation(w2_child_1)
        w2_child_2 = mutation(w2_child_2)

    child_1 = [b1_child_1, b2_child_1, w1_child_1, w2_child_1]
    child_2 = [b1_child_2, b2_child_2, w1_child_2, w2_child_2]

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
    # Crear una matriz de mutación con valores aleatorios de una distribución normal
    mutation_matrix = np.random.randn(matrix.shape[0], matrix.shape[1])
    # Aplicar la mutación a la matriz original
    mutated_matrix = matrix + mutation_matrix * 0.1  # Factor de escala ajustado
    # Devolver la matriz mutada
    return mutated_matrix

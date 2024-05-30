import random
import numpy as np
import pickle
import copy
from deap import base, creator, tools, algorithms



def updateNetwork(population,BestScore):
    new_population = Deap(population,BestScore)
    for i in range(len(population)):
        population[i].b1 = new_population[i].b1
        population[i].b2 = new_population[i].b2
        population[i].w1 = new_population[i].w1
        population[i].w2 = new_population[i].w2
    return population

def select_fittest(population):
    pass

def evolve(element1, element2):
    pass


def Deap(population,BestScore):
    # Definir el tipo de individuo y la población
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    
    # Supongamos que 'existing_population' es tu población existente
    existing_population = population

    def create_individual_from_existing(element):
        return creator.Individual([element.b1, element.b2, element.w1, element.w2, element.score])

    toolbox.register("individual_existing", create_individual_from_existing)

    toolbox.register("population_existing", tools.initRepeat, list, toolbox.individual_existing)

    # Generar una población a partir de la población existente
    new_population = toolbox.population_existing(n=len(existing_population))

    # Definir los operadores de cruce y mutación
    toolbox.register("mate", crossover)
    toolbox.register("mutate", mutation)

    # Definir la función de evaluación
    def evaluate(individual, BestScore):
        return individual.score/BestScore,

    toolbox.register("evaluate", evaluate , BestScore=BestScore)

    # Definir los operadores de selección
    toolbox.register("select", tools.selTournament, tournsize=3)

    # Evaluar la población existente
    fitnesses = list(map(toolbox.evaluate, new_population))
    for ind, fit in zip(new_population, fitnesses):
        ind.fitness.values = fit

    # Definir parámetros de la evolución
    MUTPB,ELITPB = 0.5,0.1
    # Seleccionar los mejores individuos de la población existente
    elites = tools.selBest(new_population, int(ELITPB * len(new_population)))
    # Seleccionar los individuos que se cruzarán
    offspring = toolbox.select(new_population, len(new_population))
    # Clonar los individuos seleccionados para evitar referencias
    offspring = list(map(toolbox.clone, offspring))

    # Pasar los mejores individuos a la nueva generación
    new_population = elites

    # Cruzar los individuos seleccionados de manera aleatoria hasta completar la población el cruce se debe realizar siempre y la mutación solo en algunos casos
    for i in range(1, len(offspring)*0.9, 2):
        a = random.randint(0, len(offspring)-1)
        b = random.randint(0, len(offspring)-1)
        child1, child2 = toolbox.mate(offspring[a], offspring[b])
        new_population.append(child1)
        new_population.append(child2)
        del child1.fitness.values
        del child2.fitness.values

    # Aplicar la mutación a los individuos de la población
    for mutant in new_population:
        if random.random() < MUTPB:
            toolbox.mutate(mutant)
            del mutant.fitness.values
    
    return new_population

def crossover(ind1,ind2):
    B1_a,B1_b = cruce(ind1.b1, ind2.b1)
    B2_a,B2_b = cruce(ind1.b2, ind2.b2)
    W1_a,W1_b = cruce(ind1.w1, ind2.w1)
    W2_a,W2_b = cruce(ind1.w2, ind2.w2)
    return creator.Individual([B1_a,B2_a,W1_a,W2_a,0]), creator.Individual([B1_b,B2_b,W1_b,W2_b,0])




def cruce(matrix1, matrix2):
    # Obtener las dimensiones de las matrices
    assert matrix1.shape == matrix2.shape, "Los padres deben tener la misma forma"
    # Crear un punto de cruce aleatorio
    crossover_point = np.random.randint(1, matrix1.size) # valor aleatorio entre 1 y el tamaño de la matriz con distribución uniforme
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

def mutation(ind):
    return creator.Individual([mut(ind.b1),mut(ind.b2),mut(ind.w1),mut(ind.w2),0])


def mut(matrix):
    # Crear una matriz de mutación con valores aleatorios
    mutation_matrix = np.random.rand(matrix.shape[0], matrix.shape[1])
    # Crear una matriz de mutación con valores aleatorios
    mutation_matrix = np.random.rand(matrix.shape[0], matrix.shape[1]) # Matriz de mutación con valores aleatorios entre 0 y 1 con distribución uniforme
    # Aplicar la mutación a la matriz original
    mutated_matrix = matrix + mutation_matrix * 0.1  # Factor de escala ajustado
    # Devolver la matriz mutada
    return mutated_matrix

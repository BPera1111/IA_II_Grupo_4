import random
import numpy as np
import pickle
import copy
from deap import base, creator, tools, algorithms

elites_ant = None
save = True

def updateNetwork(population,BestScore):
    global save
    
    if not save:
        new_population = Deap(population,BestScore)
        for i in range(len(population)):
            population[i].b1 = new_population[i][0]
            population[i].b2 = new_population[i][1]
            population[i].b3 = new_population[i][2]
            population[i].w1 = new_population[i][3]
            population[i].w2 = new_population[i][4]
            population[i].w3 = new_population[i][5]
        return population
    else:
        with open('goat_2040_4.pickle', 'rb') as f:
            elit = pickle.load(f)
        population[0].b1 = elit[0]
        population[0].b2 = elit[1]
        population[0].b3 = elit[2]
        population[0].w1 = elit[3]
        population[0].w2 = elit[4]
        population[0].w3 = elit[5]
        return population


def select_fittest(population):
    pass

def evolve(element1, element2):
    pass


def Deap(population,BestScore):
    global elites_ant, save
    # Definir el tipo de individuo y la población
    if "FitnessMax" not in creator.__dict__:
        creator.create("FitnessMax", base.Fitness, weights=(1.0,))

    if "Individual" not in creator.__dict__:
        creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    
    # Supongamos que 'existing_population' es tu población existente
    existing_population = population

    def create_individual_from_existing(element):
        return creator.Individual([element.b1, element.b2,element.b3, element.w1, element.w2,element.w3, element.score])

    toolbox.register("individual_existing", create_individual_from_existing)

    def create_population_existing(n, existing_population):
        return [toolbox.individual_existing(element) for element in existing_population[:n]]

    toolbox.register("population_existing", create_population_existing, existing_population=existing_population)

    # Generar una población a partir de la población existente
    new_population = toolbox.population_existing(n=len(existing_population))

    # Definir los operadores de cruce y mutación
    toolbox.register("mate", crossover)
    toolbox.register("mutate", mutation)

    # Definir la función de evaluación
    def evaluate(individual, BestScore):
        return individual[6]/BestScore,

    toolbox.register("evaluate", evaluate , BestScore=BestScore)

    # Definir los operadores de selección
    toolbox.register("select", tools.selTournament, tournsize=3)

    # Evaluar la población existente
    fitnesses = list(map(toolbox.evaluate, new_population))
    for ind, fit in zip(new_population, fitnesses):
        ind.fitness.values = fit

    if not elites_ant==None:
        fitnesses = list(map(toolbox.evaluate, elites_ant))
        for ind, fit in zip(elites_ant, fitnesses):
            ind.fitness.values = fit

    # Definir parámetros de la evolución
    MUTPB,ELITPB,SUBELITE = 0.7,0.2,0.1
    # Seleccionar los mejores individuos de la población existente
    elites = tools.selBest(new_population, int(ELITPB * len(new_population)))
    # Guardar en un .pickle el objeto elites[0]
    
    subElite = tools.selBest(new_population, int(SUBELITE * len(new_population)))
    toolbox.register("evaluate_sub", evaluate , BestScore=subElite[0][6])

    fitnesses = list(map(toolbox.evaluate_sub, subElite))
    for ind, fit in zip(subElite, fitnesses):
        ind.fitness.values = fit

    if not elites_ant==None:
        the_best = elites+elites_ant
        elites = tools.selBest(the_best, int(ELITPB * len(new_population)))
        elites_ant = elites.copy()
        if not save:
            with open('elite.pickle', 'wb') as f:
                pickle.dump(elites_ant[0], f)
    else:
        elites_ant = elites.copy()


    # Seleccionar los individuos que se cruzarán
    offspring = toolbox.select(new_population, len(new_population))
    # Clonar los individuos seleccionados para evitar referencias
    offspring = list(map(toolbox.clone, offspring))

    # Pasar los mejores individuos a la nueva generación
    new_population = elites.copy() + subElite.copy()
    # Cruzar los individuos seleccionados de manera aleatoria hasta completar la población el cruce se debe realizar siempre y la mutación solo en algunos casos
    for i in range(1, int(len(offspring)*(1-ELITPB-SUBELITE)), 2):
        e = random.randint(0, len(elites)-1)
        if random.random() < elites[e].fitness.values[0]:
            a = e
        else:
            a = random.randint(0, len(offspring)-1)
        se = random.randint(0, len(subElite)-1)
        if random.random() < subElite[se].fitness.values[0]:
            b = se
        else:
            b = random.randint(0, len(offspring)-1)
        child1, child2 = toolbox.mate(offspring[a], offspring[b])
        if random.random() < MUTPB:
            child1 = toolbox.mutate(child1)
        elif random.random() < MUTPB:
            child2 = toolbox.mutate(child2)
        new_population.append(child1)
        new_population.append(child2)
        del child1.fitness.values
        del child2.fitness.values

    # Aplicar la mutación a los individuos de la población
    # for mutant in new_population:
    #     if random.random() < MUTPB:
    #         mut = toolbox.mutate(mutant)
    #         mutant[0] = mut[0]
    #         mutant[1] = mut[1]
    #         mutant[2] = mut[2]
    #         mutant[3] = mut[3]
    #         del mutant.fitness.values
            # new_population.append(mut)

    return new_population

def crossover(ind1,ind2):
    B1_a,B1_b = cruce(ind1[0], ind2[0])
    B2_a,B2_b = cruce(ind1[1], ind2[1])
    B3_a,B3_b = cruce(ind1[2], ind2[2])
    W1_a,W1_b = cruce(ind1[3], ind2[3])
    W2_a,W2_b = cruce(ind1[4], ind2[4])
    W3_a,W3_b = cruce(ind1[5], ind2[5])
    return creator.Individual([B1_a,B2_a,B3_a,W1_a,W2_a,W3_a,0]), creator.Individual([B1_b,B2_b,B3_b,W1_b,W2_b,W3_b,0])




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
    return creator.Individual([mut(ind[0]),mut(ind[1]),mut(ind[2]),mut(ind[3]),mut(ind[4]),mut(ind[5]),0])


def mut(matrix):
    # Crear una matriz de mutación con valores aleatorios
    mutation_matrix = np.random.rand(matrix.shape[0], matrix.shape[1]) # Matriz de mutación con valores aleatorios entre 0 y 1 con distribución uniforme
    # Aplicar la mutación a la matriz original
    random_vector = np.random.rand(2)
    a = np.argmax(random_vector)
    if a == 0:
        mutated_matrix = matrix + mutation_matrix *0.1 # Factor de escala ajustado
    elif a == 1:
        mutated_matrix = matrix - mutation_matrix *0.1 # Factor de escala ajustado
    # mutated_matrix = matrix + mutation_matrix *0.1 # Factor de escala ajustado
    # # Devolver la matriz mutada
    return mutated_matrix

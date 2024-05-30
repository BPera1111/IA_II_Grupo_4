from deap import base, creator, tools
import numpy as np

# Definir el tipo de fitness y el tipo de individuo
# creator.create("FitnessMax", base.Fitness, weights=(1.0,))
# creator.create("Individual", np.ndarray, fitness=creator.FitnessMax)

# Definir la función de crossover para matrices
def matrix_crossover(ind1, ind2):
    assert ind1.shape == ind2.shape, "Los padres deben tener la misma forma"
    
    # Crear un punto de cruce aleatorio
    crossover_point = np.random.randint(1, ind1.size)
    
    # Aplanar las matrices para facilitar el cruce
    flat_ind1 = ind1.flatten()
    flat_ind2 = ind2.flatten()
    
    # Realizar el cruce
    new_flat_ind1 = np.concatenate([flat_ind1[:crossover_point], flat_ind2[crossover_point:]])
    new_flat_ind2 = np.concatenate([flat_ind2[:crossover_point], flat_ind1[crossover_point:]])
    
    # Reformar los individuos a su forma original
    new_ind1 = new_flat_ind1.reshape(ind1.shape)
    new_ind2 = new_flat_ind2.reshape(ind2.shape)
    
    # Asignar los nuevos valores a los individuos
    ind1[:] = new_ind1
    ind2[:] = new_ind2
    
    return ind1, ind2

# Crear una herramienta de base
toolbox = base.Toolbox()

# Registrar las funciones de crossover y mutación
toolbox.register("mate", matrix_crossover)

# Crear dos individuos de ejemplo
parent1 = np.array([[1, 2, 3], [4, 5, 6]])
parent2 = np.array([[7, 8, 9], [10, 11, 12]])

# Aplicar el crossover
child1, child2 = toolbox.mate(parent1, parent2)

print("Child 1:\n", child1)
print("Child 2:\n", child2)

import numpy as np
import temple
import tablero
import copy


def corregir_valores_repetidos(individuo):
    # Obtener una lista de valores únicos en el individuo
    valores_unicos = set(np.unique(individuo.matriz))
    # print(len(valores_unicos))
    # Crear un diccionario con los índices de los valores repetidos
    index_dict = {}
    for row_index, row in enumerate(individuo.matriz):
        for col_index, val in enumerate(row):
            if val != 0:
                if val in index_dict:
                    index_dict[val].append((row_index, col_index))
                else:
                    index_dict[val] = [(row_index, col_index)]
    
    duplicates = {key: val for key, val in index_dict.items() if len(val) > 1}

    indices_faltantes = [duplicates[i][j] for i in duplicates for j in range(1,len(duplicates[i]))]
    
    # Encontrar los valores faltantes para completar 192 valores
    valores_faltantes = set(range(1, 193)) - valores_unicos  
    # Aleatorizar los valores faltantes y agregarlos al individuo
    valores_faltantes = np.random.permutation(list(valores_faltantes))
    #rellenamos la matriz en los indices faltantes con los valores faltantes
    for i in range(len(indices_faltantes)):
        individuo.matriz[indices_faltantes[i][0]][indices_faltantes[i][1]] = valores_faltantes[i]

    return individuo


# Función de evaluación (Fitness)
def evaluar_almacen(productos,almacen):
    # Calcular la eficiencia del picking (por ejemplo, la suma de las distancias entre los productos)
    eficiencia = temple.templado(productos,almacen)
    return eficiencia

# Operadores genéticos
def seleccion(poblacion, fitness):
    individuos_seleccionados = []
    for i in range(len(poblacion)//2):
        individuos_seleccionados.append(poblacion[np.argmin(fitness)])
        fitness[np.argmin(fitness)] = 200000
    return individuos_seleccionados

def cruce(padre1, padre2):
    # Obtener dimensiones de los padres
    n_filas, n_columnas = padre1.filas, padre1.columnas
    
    # Elegir un punto de cruce aleatorio
    punto_cruce = np.random.randint(n_columnas-int(n_columnas*0.65), int(n_columnas*0.65))

    # Crear los descendientes
    descendiente1 = tablero.tablero(n_filas,n_columnas)
    descendiente2 = tablero.tablero(n_filas,n_columnas)

    #crear descendientes a parir de cada fila de los padres
    for i in range(n_filas):
        fila_padre1 = padre1.matriz[i]
        fila_padre2 = padre2.matriz[i]

        fila_descendiente1 = np.zeros(n_columnas)
        fila_descendiente2 = np.zeros(n_columnas)
        
        # Copiar las partes de los padres antes y después del punto de cruce
        fila_descendiente1 = np.concatenate((fila_padre1[:punto_cruce], fila_padre2[punto_cruce:])).tolist()
        fila_descendiente2 = np.concatenate((fila_padre2[:punto_cruce], fila_padre1[punto_cruce:])).tolist()

        #agrergar las filas a los descendientes
        descendiente1.matriz[i] = fila_descendiente1
        descendiente2.matriz[i] = fila_descendiente2

    

    # Copiar las partes de los padres antes y después del punto de cruce
    
    '''
    descendiente1.matriz[:][:punto_cruce] = padre1.matriz[:][:punto_cruce]
    descendiente1.matriz[:][punto_cruce:] = padre2.matriz[:][punto_cruce:]
    
    descendiente2.matriz[:][:punto_cruce] = padre2.matriz[:][:punto_cruce]
    descendiente2.matriz[:][punto_cruce:] = padre1.matriz[:][punto_cruce:]
    '''
    # Corregir los valores repetidos en los descendientes
    descendiente1 = corregir_valores_repetidos(descendiente1)
    descendiente2 = corregir_valores_repetidos(descendiente2)
    #print("alto ahí bandido")

    return descendiente1, descendiente2

def mutacion(individuo, probabilidad_mutacion):
    index_dict = {}
    for row_index, row in enumerate(individuo.matriz):
        for col_index, val in enumerate(row):
            if val != 0:
                index_dict[val] = [(row_index, col_index)]
    for i in range(individuo.filas):
        for j in range(individuo.columnas):
            if individuo.matriz[i][j] != 0 and np.random.rand() < probabilidad_mutacion:
                original=copy.copy(individuo.matriz[i][j])
                mutante = np.random.randint(1, 193)
                individuo.matriz[i][j] = mutante
                individuo.matriz[index_dict[mutante][0][0]][index_dict[mutante][0][1]] = original
    return individuo
# Parámetros del algoritmo genético
tamano_poblacion = 100
probabilidad_mutacion = 0.01
num_generaciones = 20

# Inicialización de la población
n_filas, n_columnas = 21, 19

#Creo una lista de tableros
tableros = []
for i in range(tamano_poblacion):
    tableros.append(tablero.tablero(n_filas,n_columnas))

#poblacion = [np.random.randint(0, 2, size=(n_filas, n_columnas)) for _ in range(tamano_poblacion)]

productos = [[[52], [75], [81], [100], [2]],
             [[52], [3], [4], [5], [6]], 
             [[52], [43], [44], [45], [46]]]
mejor_especimen=[]
# Evolución
for _ in range(num_generaciones):
    try:
        # Evaluación de la población
        #for todos los productos
        fitness=[]
        fitness_suma=np.zeros(len(tableros))
        for j in range(len(productos)):
            fitness=[evaluar_almacen(productos[j],individuo) for individuo in tableros]#+fitness
            fitness_suma=np.array(fitness)+fitness_suma
            
        #fitness = [evaluar_almacen(productos,individuo) for individuo in tableros]
        fitness_suma=list(fitness_suma)
        print("Fitness promedio:", np.mean(fitness_suma))
        # Selección
        seleccionados = seleccion(tableros, fitness_suma)

        # Cruce
        descendientes = seleccionados
        for i in range(0, len(seleccionados), 2):
            hijo1, hijo2 = cruce(seleccionados[i], seleccionados[i + 1])
            descendientes.extend([hijo1, hijo2])

        # Corregir los valores repetidos en los descendientes
        descendientes = [corregir_valores_repetidos(individuo) for individuo in descendientes]

        # Mutación
        tableros = [mutacion(individuo, probabilidad_mutacion) for individuo in descendientes]

        tableros = [corregir_valores_repetidos(individuo) for individuo in tableros]

        print("Generación: ", _+1)
    except Exception as e:
        print("Error en la generación", _, ":", e)
        continue
# Selección del mejor individuo
fitness_suma=np.zeros(len(tableros))
for i in range(len(productos)):
    fitness=[evaluar_almacen(productos[i],individuo) for individuo in tableros]
    fitness_suma=np.array(fitness)+fitness_suma   
print(fitness_suma)
mejor_individuo = tableros[np.argmin(fitness_suma)]
for i in range(len(productos)):
    prueba=evaluar_almacen(productos[i],mejor_individuo)
    print("Fitness del mejor individuo para el producto",i+1,":",prueba)
#mejor_individuo = tableros[np.argmax([evaluar_almacen(productos,individuo) for individuo in tableros])]
#print mejor individuo con formato
for i in range(mejor_individuo.filas):
    print(mejor_individuo.matriz[i])    
#print("Mejor individuo:", mejor_individuo.matriz)
#print("Fitness:", evaluar_almacen(productos,mejor_individuo))

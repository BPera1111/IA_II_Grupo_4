import math
import funcion_a_estrella 
from itertools import combinations
import random
import math


#Funcion para crear todas las combinaciones de los elementos
#de una lista tomados de a 2. (si los elementos de la lista
#son 20, por ejemplo, la combinatoria da 190)
def combinar_vector(vector_p):
    combinaciones = []
    for comb in combinations(vector_p, 2):
        combinaciones.append(comb)  
    return combinaciones

#Funcion para permutar aleatoriamente 2 posiciones, genera un estado vecino
def permutar_aleatoriamente(estado_actual1, estado_actual2):
    estado_copia1 = estado_actual1[:]
    estado_copia2 = estado_actual2[:]
    #La primer cordenada y las ultimas no deben entrar en la permutacion
    indices_permitidos = list(range(1, len(estado_actual1) - 1))

    # Elegir dos índices aleatorios diferentes
    indice1, indice2 = random.sample(indices_permitidos, 2)
    
    # Intercambiar los elementos en los índices elegidos
    estado_copia1[indice1], estado_copia1[indice2] = estado_copia1[indice2], estado_copia1[indice1]
    estado_copia2[indice1], estado_copia2[indice2] = estado_copia2[indice2], estado_copia2[indice1]
    
    return estado_copia1, estado_copia2


#Funcion que genera aleatoriamente el estado actual
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

#Funcion que acepta o rechaza un estado peor, segun una probabilidad
def aceptar_rechazar(probabilidad):
    numero_aleatorio = random.random()
    if numero_aleatorio < probabilidad:
        return True
    else:
        return False

##############################################################################################
###############################  Funciones Schedule  #########################################   
    
def schedule_exponencial(t, temperatura_inicial, factor_enfriamiento):
    return temperatura_inicial * (factor_enfriamiento ** t)

def schedule_lineal(t, temperatura_inicial, iteraciones):
    return temperatura_inicial * (1 - t / iteraciones)


def schedule_logaritmico(t, temperatura_inicial, factor_enfriamiento):
    return temperatura_inicial / math.log(t + 1, factor_enfriamiento)

##############################################################################################
##############################################################################################


bahia_inicio_descarga = [0, 0]
productos1 = [[1, 0], [1, 3], [1, 3], [1, 6], [2, 0], [2, 3], [2, 3], [2, 6], [3, 0], [3, 3], [3, 3], [3, 6], [4, 0], [4, 3], [4, 3], [4, 6], [6, 0], [6, 3], [6, 3], [6, 6], [7, 0], [7, 3], [7, 3], [7, 6], [8, 0], [8, 3], [8, 3], [8, 6], [9, 0], [9, 3], [9, 3], [9, 6]]
productos2 = [[0, 1], [0, 2], [0, 4], [0, 5], [2, 0], [2, 3], [2, 3], [2, 6], [3, 0], [3, 3], [3, 3], [3, 6], [5, 1], [5, 2], [5, 4], [5, 5], [5, 1], [5, 2], [5, 4], [5, 5], [7, 0], [7, 3], [7, 3], [7, 6], [8, 0], [8, 3], [8, 3], [8, 6], [10, 1], [10, 2], [10, 4], [10, 5]]


#Se crea el vector picking agregando al vector de productos la posicion
#de inicio y fin
vector_p1 = [bahia_inicio_descarga] + productos1
vector_p2 = [bahia_inicio_descarga] + productos2

#Vamos a suponer que tiene que volver al mismo punto
#de donde salio, es decir el punto de inicio es la "bahía de
#descarga", si esto no fuera así, solamente sería necesario
#agregar una posición más, la de la bahía de descarga, y no
#tener en cuenta la distancia entre el punto inicial y el final. 

resultado1 = combinar_vector(vector_p1)
resultado2 = combinar_vector(vector_p2)

#Vamos a usar una heuristica, la cual consiste en conocer previamente
#las distancias entre sí de todos los productos por los que se debe pasar.
#Se consrtuye un diccionario, cuyas claves son dos coordenadas, y cuyo
#valor es el G correspondiente al camino entre P1 y P2. 

diccionario1 = {}

for i in resultado1:
    inicio = i[0]
    fin = i[1]
    g = funcion_a_estrella.A_estrella(inicio, fin)  
    diccionario1[(tuple(inicio), tuple(fin))] = g
    diccionario1[(tuple(fin), tuple(inicio))] = g
diccionario1[(tuple([0, 0]), tuple([0, 0]))] = 0

diccionario2 = {}

for i in resultado2:
    inicio = i[0]
    fin = i[1]
    g = funcion_a_estrella.A_estrella(inicio, fin)  
    diccionario2[(tuple(inicio), tuple(fin))] = g
    diccionario2[(tuple(fin), tuple(inicio))] = g
diccionario1[(tuple([0, 0]), tuple([0, 0]))] = 0


recorrido1 = vector_p1 + [bahia_inicio_descarga]
recorrido2 = vector_p2 + [bahia_inicio_descarga]
estado_actual1, estado_actual2 = generar_estado_actual_aleatorio(recorrido1, recorrido2)

#Parametros para las funciones schedule
t = 0
T_inicial = 1000
iteraciones = 100
factor_enfriamiento = 0.4

flag = True
while flag:
    
    E = 0
    for i in range(len(estado_actual1)):
        E = diccionario1[(tuple(estado_actual1[i]), tuple(estado_actual1[(i + 1) % len(estado_actual1)]))] + E

    
        
    T = schedule_exponencial(t, T_inicial, factor_enfriamiento)
    #T = schedule_lineal(t, T_inicial, iteraciones)
    #T = schedule_logaritmico(t, T_inicial, factor_enf)


    if t > iteraciones: #Otro criterio de detencion puede ser si T == 0, depende de la funcion schedule
        flag = False
    t = t + 1

    #Se elige aleatoriamente un segundo estado.
    
    estado_vecino1, estado_vecino2 = permutar_aleatoriamente(estado_actual1, estado_actual2)


    #Se calcula el E de dicho estado. 

    E2 = 0
    for i in range(len(estado_vecino1)):
        E2 = diccionario1[(tuple(estado_vecino1[i]), tuple(estado_vecino1[(i + 1) % len(estado_vecino1)]))] + E2

    

    #Se resta con el E estado anterior. A este valor se le llama DE (delta E).
        
    DE = E - E2    
    
    #Si dicho valor es positivo, significa que el nuevo estado es mejor que el 
    #inicial, en ese caso se elige el nuevo estado sin ningun otro paso intermedio.

    if DE >= 0:
        estado_actual1 = estado_vecino1
        estado_actual2 = estado_vecino2
    else:
        #Se calcula la probabilidad
        if T > 0:
            probabilidad = math.exp(DE/(T))
        else: 
            probabilidad = 0
        
        
        if aceptar_rechazar(probabilidad):
            estado_actual1 = estado_vecino1
            estado_actual2 = estado_vecino2
            
           


#print("El recorrido optimo es: ", estado_actual1)
E = 0
for i in range(len(estado_actual1)):
    E = diccionario1[(tuple(estado_actual1[i]), tuple(estado_actual1[(i + 1) % len(estado_actual1)]))] + E

print("El recorrido tiene un E de: ", E)


###########################################################################################################

def intercambiar_puntos(estado_actual1, estado_actual2):
    estado_copia1 = estado_actual1[:]
    estado_copia2 = estado_actual2[:]
    #La primer cordenada y las ultimas no deben entrar en la permutacion
    indices = list(range(0, len(estado_actual1)))

    # Elegir dos índices aleatorios diferentes
    indice1, indice2 = random.sample(indices, 2)
    
    # Intercambiar los elementos en los índices elegidos
    estado_copia1[indice1] = estado_actual2[indice1]
    estado_copia1[indice2] = estado_actual2[indice2]
    estado_copia2[indice1] = estado_actual1[indice1]
    estado_copia2[indice2] = estado_actual1[indice2]


    return estado_copia1, estado_copia2

#Parametros para las funciones schedule
t = 0
T_inicial = 1000
iteraciones = 100
factor_enfriamiento = 0.4

flag = True
while flag:
    
    E = 0
    for i in range(len(estado_actual1)):
        if (tuple(estado_actual1[i]), tuple(estado_actual1[(i + 1) % len(estado_actual1)])) not in diccionario2:
            E = diccionario1[(tuple(estado_actual1[i]), tuple(estado_actual1[(i + 1) % len(estado_actual1)]))] + E
        else:
            E = diccionario2[(tuple(estado_actual1[i]), tuple(estado_actual1[(i + 1) % len(estado_actual1)]))] + E
    
        
    T = schedule_exponencial(t, T_inicial, factor_enfriamiento)
    #T = schedule_lineal(t, T_inicial, iteraciones)
    #T = schedule_logaritmico(t, T_inicial, factor_enf)


    if t > iteraciones: 
        flag = False
    t = t + 1

    #Se elige aleatoriamente un segundo estado.
    
    estado_vecino1, estado_vecino2 = intercambiar_puntos(estado_actual1, estado_actual2)


    #Se calcula el E de dicho estado. 

    E2 = 0
    for i in range(len(estado_actual1)):
        if (tuple(estado_actual1[i]), tuple(estado_actual1[(i + 1) % len(estado_actual1)])) not in diccionario2:
            E2 = diccionario1[(tuple(estado_actual1[i]), tuple(estado_actual1[(i + 1) % len(estado_actual1)]))] + E2
        else:
            E2 = diccionario2[(tuple(estado_actual1[i]), tuple(estado_actual1[(i + 1) % len(estado_actual1)]))] + E2

    

    #Se resta con el E estado anterior. A este valor se le llama DE (delta E).
        
    DE = E - E2    
    
    #Si dicho valor es positivo, significa que el nuevo estado es mejor que el 
    #inicial, en ese caso se elige el nuevo estado sin ningun otro paso intermedio.

    if DE >= 0:
        estado_actual1 = estado_vecino1
        estado_actual2 = estado_vecino2
    else:
        #Se calcula la probabilidad
        if T > 0:
            probabilidad = math.exp(DE/(T))
        else: 
            probabilidad = 0
        
        
        if aceptar_rechazar(probabilidad):
            estado_actual1 = estado_vecino1
            estado_actual2 = estado_vecino2
            
           


#print("El recorrido optimizado es: ", estado_actual1)
E = 0
for i in range(len(estado_actual1)):
        if (tuple(estado_actual1[i]), tuple(estado_actual1[(i + 1) % len(estado_actual1)])) not in diccionario2:
            E = diccionario1[(tuple(estado_actual1[i]), tuple(estado_actual1[(i + 1) % len(estado_actual1)]))] + E
        else:
            E = diccionario2[(tuple(estado_actual1[i]), tuple(estado_actual1[(i + 1) % len(estado_actual1)]))] + E

print("El recorrido optimizado tiene un E de:  ", E)

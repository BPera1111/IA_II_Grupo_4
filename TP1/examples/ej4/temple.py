import math
import funcion_a_estrella 
from itertools import combinations
import random
import math
import agente
import tablero
import copy

#Funcion para crear todas las combinaciones de los elementos
#de una lista tomados de a 2. (si los elementos de la lista
#son 20, por ejemplo, la combinatoria da 190)
def combinar_vector(vector_p):
    combinaciones = []
    for comb in combinations(vector_p, 2):
        combinaciones.append(comb)  
    return combinaciones

#Funcion para permutar aleatoriamente 2 posiciones, genera un estado vecino
def permutar_aleatoriamente(estado_actual):
    estado_copia = estado_actual[:]
    #La primer cordenada y las ultimas no deben entrar en la permutacion
    indices_permitidos = list(range(1, len(estado_actual) - 1))

    # Elegir dos índices aleatorios diferentes
    indice1, indice2 = random.sample(indices_permitidos, 2)
    
    # Intercambiar los elementos en los índices elegidos
    estado_copia[indice1], estado_copia[indice2] = estado_copia[indice2], estado_copia[indice1]
    
    return estado_copia


#Funcion que genera aleatoriamente el estado actual
def generar_estado_actual_aleatorio(vector):
   # Mantener la primera y última componente intactas
    primera_componente = vector[0]
    ultima_componente = vector[-1]

    # Desordenar las componentes intermedias
    componentes_intermedias = vector[1:-1]
    random.shuffle(componentes_intermedias)

    # Reconstruir el vector con las componentes desordenadas
    vector_desordenado = [primera_componente] + componentes_intermedias + [ultima_componente]
    
    return vector_desordenado

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
productos = [[52], [75], [81], [100], [2]] 

# [0, 0] ,[5, 6], [8, 3], [10, 6], [1, 3] 

#Se crea el vector picking agregando al vector de productos la posicion
#de inicio y fin
vector_p = [bahia_inicio_descarga] + productos

#Vamos a suponer que tiene que volver al mismo punto
#de donde salio, es decir el punto de inicio es la "bahía de
#descarga", si esto no fuera así, solamente sería necesario
#agregar una posición más, la de la bahía de descarga, y no
#tener en cuenta la distancia entre el punto inicial y el final. 

resultado = combinar_vector(vector_p) 

#Vamos a usar una heuristica, la cual consiste en conocer previamente
#las distancias entre sí de todos los productos por los que se debe pasar.
#Se consrtuye un diccionario, cuyas claves son dos coordenadas, y cuyo
#valor es el G correspondiente al camino entre P1 y P2. 

diccionario = {}
tab=tablero.tablero(21,19)
agentee=agente.agente(tab)

for i in resultado:
    agentee.definir_agente(i[0],i[1],tab)
    #g = funcion_a_estrella.A_estrella(inicio, fin)
    g=agentee.busqueda(tab)  
    diccionario[(tuple(agentee.posicion), tuple(agentee.objetivo))] = g
    diccionario[(tuple(agentee.objetivo), tuple(agentee.posicion))] = g
diccionario[(tuple([0, 0]), tuple([0, 0]))] = 0


recorrido = vector_p + [bahia_inicio_descarga]
estado_actual = generar_estado_actual_aleatorio(recorrido)

#Parametros para las funciones schedule
t = 0
T_inicial = 1000
iteraciones = 100
factor_enfriamiento = 0.4

flag = True
while flag:
    #Se empieza con un estado aleatorio, que tiene cierta calidad. La calidad se
    #mide con la variable E. Mientras mayor sea E, peor es la calidad del estado
    #que se esta midiendo.
    #En nuestro caso E es la cantidad de pasos total (G). 

    E = 0
    for i in range(len(estado_actual)):
        E = diccionario[(tuple(estado_actual[i]), tuple(estado_actual[(i + 1) % len(estado_actual)]))] + E

    
    #La variable T es la variable "temperatura", que va en el 
    #exponente de e. Para obtener el valor de T se
    #debe crear una funcion schedule(t) en funcion de la cantidad de
    #iteraciones. Debe pasar que a medida que aumente t, disminuya T,
    #hasta que se haga cero y se termine el ciclo. 
        
    T = schedule_exponencial(t, T_inicial, factor_enfriamiento)
    #T = schedule_lineal(t, T_inicial, iteraciones)
    #T = schedule_logaritmico(t, T_inicial, factor_enf)

    #Hay que elegir (y variar para ver resultados) si T va a tener un
    #decrecimiento lineal, o exponencial, o algun otro. 

    if t > iteraciones: #Otro criterio de detencion puede ser si T == 0, depende de la funcion schedule
        flag = False
    t = t + 1

    #Se elige aleatoriamente un segundo estado.
    
    estado_vecino = permutar_aleatoriamente(estado_actual)

    

    #Se calcula el E de dicho estado. 

    E2 = 0
    for i in range(len(estado_vecino)):
        E2 = diccionario[(tuple(estado_vecino[i]), tuple(estado_vecino[(i + 1) % len(estado_vecino)]))] + E2

    

    #Se resta con el E estado anterior. A este valor se le llama DE (delta E).
        
    DE = E - E2    
    
    #Si dicho valor es positivo, significa que el nuevo estado es mejor que el 
    #inicial, en ese caso se elige el nuevo estado sin ningun otro paso intermedio.

    if DE >= 0:
        estado_actual = estado_vecino
    else:
        #Se calcula la probabilidad
        if T > 0:
            probabilidad = math.exp(DE/(T))
        else: 
            probabilidad = 0
        
        
        if aceptar_rechazar(probabilidad):
            estado_actual = estado_vecino
            
           

    #Si el estado nuevo es peor que el inicial, el DE va a ser negativo, en ese
    #caso se usa la funcion del e para encontrar la probabilidad de elegir el estado
    #nuevo que es peor, es decir, aunque sea peor igual va a haber probabilidades de elegirlo.
    #El DE siempre va a ser negativo, porque se va a calcular solamente cuando de negativo. 


print("El recorrido optimo es: ", estado_actual)
E = 0
for i in range(len(estado_actual)):
    E = diccionario[(tuple(estado_actual[i]), tuple(estado_actual[(i + 1) % len(estado_actual)]))] + E

print("Con un E de: ", E)

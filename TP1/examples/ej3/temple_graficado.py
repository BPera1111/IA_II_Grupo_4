import pygame
import random
import sys
import math
import a_estrella_recorrido
import funcion_a_estrella 
from itertools import combinations


# Definir las dimensiones de la matriz
filas = 21  
columnas = 19  
matriz = []

# Genera la matriz 
for i in range(filas):
    fila = []
    for j in range(columnas):
        # Verificar si la fila o la columna son múltiplos de 4 (para filas y columnas basadas en 0)
        if i % 5 == 0 or i == 0 or j == 0 or j % 3 == 0:
            fila.append(0)
        else:
            fila.append(1)
    matriz.append(fila)



######################################  Grafica  ############################################################
#############################################################################################################

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)

# Configuración del tablero
ANCHO_CASILLA = 30
MARGEN = 1
FILAS = 21
COLUMNAS = 19

# Tamaño de la pantalla
ANCHO_PANTALLA = COLUMNAS * (ANCHO_CASILLA + MARGEN) + MARGEN
ALTO_PANTALLA = FILAS * (ANCHO_CASILLA + MARGEN) + MARGEN

# Crear pantalla
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Tablero con colores")


def matriz_a_colores(matriz):
    # Crear una matriz de colores inicialmente vacía
    matriz_colores = []
    
    # Recorrer la matriz de unos y ceros
    for fila in matriz:
        fila_colores = []
        for elemento in fila:
            # Convertir los unos en NEGRO y los ceros en BLANCO
            color = NEGRO if elemento == 1 else BLANCO
            fila_colores.append(color)
        matriz_colores.append(fila_colores)
    
    return matriz_colores


tablero = matriz_a_colores(matriz)

# Función para dibujar el tablero
def dibujar_tablero():
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            color = tablero[fila][columna]
            pygame.draw.rect(pantalla, color, ((MARGEN + ANCHO_CASILLA) * columna + MARGEN,
                                               (MARGEN + ANCHO_CASILLA) * fila + MARGEN,
                                               ANCHO_CASILLA, ANCHO_CASILLA))

#############################################################################################################
#############################################################################################################







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


#def schedule_logaritmico(t, temperatura_inicial, factor_enfriamiento):
#    return temperatura_inicial / math.log(t + 1, factor_enfriamiento)
def schedule_logaritmico(t, temperatura_inicial, factor_enfriamiento):
    if t == 0:
        return temperatura_inicial
    else:
        return temperatura_inicial / math.log(t + 1, factor_enfriamiento)

##############################################################################################
##############################################################################################


bahia_inicio_descarga = [0, 0]
productos = [[6, 6], [8, 3], [8, 9], [11, 6], [1, 3], [13, 6], [11, 9], [15, 2], [8, 0], [0, 11],
              [1, 6], [5, 5], [12, 12], [15, 10], [5, 8], [17, 6], [12, 3], [7, 12], [0, 5], [14, 0]] 

lugar_en_estante = [[6, 5] ,[8, 2], [8, 8], [11, 5], [1, 2], [13, 5], [11, 8], [16, 2], [8, 1], [1, 11],
                     [1, 5], [4, 5], [12, 11], [14, 10], [4, 8], [17, 5], [12, 2], [7, 11], [1, 5], [14, 1]]

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

for i in resultado:
    inicio = i[0]
    fin = i[1]
    g = funcion_a_estrella.A_estrella(inicio, fin)  
    diccionario[(tuple(inicio), tuple(fin))] = g
    diccionario[(tuple(fin), tuple(inicio))] = g
diccionario[(tuple([0, 0]), tuple([0, 0]))] = 0


recorrido = vector_p + [bahia_inicio_descarga]
estado_actual = generar_estado_actual_aleatorio(recorrido)

#Parametros para las funciones schedule
t = 0
T_inicial = 10000
iteraciones = 1000  
factor_enfriamiento = 0.1 

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
    #T = schedule_logaritmico(t, T_inicial, factor_enfriamiento)

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
    

recorrido_final_invertido = []
for i in range(len(estado_actual)):
    v = a_estrella_recorrido.A_estrella_recorrido(estado_actual[i], estado_actual[(i + 1) % len(estado_actual)])
    for j in v:
        recorrido_final_invertido.append(j)
    


for i in lugar_en_estante:
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    x = i[0]
    y = i[1]
    tablero[x][y] = ROJO
   
    pygame.time.delay(50)
    # Dibujar el tablero
    pantalla.fill(BLANCO)
    dibujar_tablero()
    pygame.display.flip()




for i in recorrido_final_invertido:
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    x = i[0]
    y = i[1]
    tablero[x][y] = AZUL
    
    pygame.time.delay(50)

    # Dibujar el tablero
    pantalla.fill(BLANCO)
    dibujar_tablero()
    pygame.display.flip()





while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
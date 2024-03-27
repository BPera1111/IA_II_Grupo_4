###################################### TP 1 ###########################################
# Ejercicio 1

#import turtle

#primero se crea una matriz que representa con ceros los caminos libres
#y con unos los espacios ocupados por las estanterías

# Definir las dimensiones de la matriz
filas = 21  # Puedes cambiar este valor según tus necesidades
columnas = 19  # Puedes cambiar este valor según tus necesidades

# Inicializar una lista vacía para contener la matriz
matriz = []

# Generar la matriz con las características requeridas
for i in range(filas):
    fila = []
    for j in range(columnas):
        # Verificar si la fila o la columna son múltiplos de 4 (para filas y columnas basadas en 0)
        if i % 5 == 0 or i == 0 or j == 0 or j % 3 == 0:
            fila.append(0)
        else:
            fila.append(1)
    matriz.append(fila)

#Se crea la clase Nodo
class Nodo:
    def __init__(self, coordenadas,g):
        self.coordenadas = coordenadas
        self.g=g

    def encuentra_vecinos(self, matriz, objetivo):
        filas = len(matriz)
        columnas = len(matriz[0])
        lista_vecinos = []

        # Verificar vecino superior
        if self.coordenadas[0] > 0 and matriz[self.coordenadas[0] - 1][self.coordenadas[1]] == 0:
            h = abs(objetivo[0] - (self.coordenadas[0] - 1)) + abs(objetivo[1] - (self.coordenadas[1]))
            f=h+self.g
            vecino1 = (self.coordenadas[0] - 1, self.coordenadas[1], h, self.g,f)
            lista_vecinos.append(vecino1)

        # Verificar vecino inferior
        if self.coordenadas[0] < filas - 1 and matriz[self.coordenadas[0] + 1][self.coordenadas[1]] == 0:
            h = abs(objetivo[0] - (self.coordenadas[0] + 1)) + abs(objetivo[1] - self.coordenadas[1])
            f=h+self.g
            vecino2 = (self.coordenadas[0] + 1, self.coordenadas[1], h, self.g,f)
            lista_vecinos.append(vecino2)

        # Verificar vecino izquierdo
        if self.coordenadas[1] > 0 and matriz[self.coordenadas[0]][self.coordenadas[1] - 1] == 0:
            h = abs(objetivo[0] - (self.coordenadas[0])) + abs(objetivo[1] - (self.coordenadas[1] - 1))
            f=h+self.g
            vecino3 = (self.coordenadas[0], self.coordenadas[1] - 1, h, self.g,f)
            lista_vecinos.append(vecino3)

        # Verificar vecino derecho
        if self.coordenadas[1] < columnas - 1 and matriz[self.coordenadas[0]][self.coordenadas[1] + 1] == 0:
            h = abs(objetivo[0] - (self.coordenadas[0])) + abs(objetivo[1] - (self.coordenadas[1] + 1))
            f=h+self.g
            vecino4 = (self.coordenadas[0], self.coordenadas[1] + 1, h, self.g,f)
            lista_vecinos.append(vecino4)

        return lista_vecinos

################################################# A estrella ##########################################
    
lista_abierta=[]
lista_cerrada=[]
camino=[]

inicio = [0, 3]
#objetivo = [6, 7]
objetivo=[0,7]

g=1
nodo_inicial=Nodo(inicio,g)
primer_nodo=(0,3,4,0,4)
lista_abierta.append(primer_nodo)
print("Lista abierta: ", lista_abierta)

while True:
    if inicio == objetivo:
        print("\nSe llego al objetivo")
        print("Lista abierta: ", lista_abierta)
        print("Lista cerrada: ",lista_abierta)
        #print("/nCamino: ",camino)
        break
    
    inicio = [primer_nodo[0], primer_nodo[1]]
    lista_cerrada.append(primer_nodo)
    if primer_nodo in lista_abierta:
        lista_abierta.remove(primer_nodo)
    print("Lista cerrada:", lista_cerrada)
    print("Lista abierta:", lista_abierta)

    # Encontrar vecinos del nodo actual
    vecinos = nodo_inicial.encuentra_vecinos(matriz, objetivo)
    print("Vecinos sin ordenar: ", vecinos)

    if vecinos:
        # Agregamos los vecinos a la lista abierta y los ordenamos
        lista_abierta += vecinos
        lista_abierta.sort(key=lambda x: x[4])
        print("Lista abierta ordenada:", lista_abierta)

        primer_nodo = lista_abierta[0]
        lista_cerrada.append(primer_nodo)
        if primer_nodo in lista_abierta:
            lista_abierta.remove(primer_nodo)
        print("Lista cerrada:", lista_cerrada)
        print("Lista abierta:", lista_abierta)

        # Actualizamos g
        vecino_g = primer_nodo[3] + 1  # El costo de movimiento es 1
        nodo_inicial = Nodo([primer_nodo[0], primer_nodo[1]], vecino_g)
        print("\nNodo actual:", primer_nodo)
    else:
        print("No hay vecinos disponibles.")
        break

# Reconstruir el camino


"""    
    inicio=[primer_nodo[0],primer_nodo[1]]
    lista_cerrada.append(primer_nodo)
    lista_abierta.remove(primer_nodo) #quitamos el nodo actual y lo pasamos a la cerrada
    print("1Lista cerrada:",lista_cerrada)
    print("1Lista abierta:",lista_abierta)

    # Encontrar vecinos del nodo actual
    vecinos = nodo_inicial.encuentra_vecinos(matriz, objetivo)
    print("Vecinos sin ordenar: ",vecinos)

    #Agregamos los vecinos a la lista abierta y los ordenamos
    #lista_abierta.extend(vecinos)
    lista_abierta += vecinos
    lista_abierta.sort(key=lambda x: x[4])
    print("Lista abierta:",lista_abierta)

    lista_cerrada.append(lista_abierta[0])
    lista_abierta.remove(lista_abierta[0])
    print("Lista cerrada:",lista_cerrada)
    print("Lista abierta:",lista_abierta)
    

    #actualizaciones
    primer_nodo=lista_cerrada[-1]

    #Actualizamos g
    vecino_g =int( nodo_inicial.g + 1)  # El costo de movimiento es 1
    nodo_inicial=Nodo([primer_nodo[0],primer_nodo[1]],vecino_g)
    print("\nNodo actual:",primer_nodo)
    """
    
##################################### Funciones para graficar  ############################################
"""
# Configuración de la pantalla
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Almacenes")
screen.setup(700,700)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color('white')
        
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color('blue')
        
        self.penup()
        self.speed(0)


def iniciar_lab(matriz):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            letra_x = matriz[fila][columna]
            screen_x = -288 + (columna * 24)
            screen_y = 288 - (fila * 24)

            if letra_x == 0:
                pen.goto(screen_x,screen_y)
                pen.stamp()


player = Player()
pen = Pen()  
iniciar_lab(matriz)
turtle.mainloop()  #Para mantener la ventana abierta
"""

#Algoritmo
"""
nodo_objetivo = [6,7]
nodo_actual = [0, 3]
nodo = Nodo(nodo_actual,0)

x = nodo.encuentra_vecinos(matriz,nodo_objetivo)

print(x)

nodo2=Nodo([1,3],10)
x2 = nodo2.encuentra_vecinos(matriz,nodo_objetivo)

print(x2)
"""

#Primero se crea una matriz que representa con ceros los caminos libres
#y con unos los espacios ocupados por las estanterías

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

#Imprimir la matriz
#for fila in matriz:
#    print(fila)
    
#########################################################################################################
                                #Grafica    
#########################################################################################################
import turtle

# Configuración de la ventana de Turtle
turtle.setup(width=800, height=600)
turtle.setworldcoordinates(0, 0, columnas, filas)
turtle.speed(1000)
turtle.hideturtle()

def dibujar_matriz(matriz, lista_cerrada, lista_abierta, recorrido_final):
    turtle.tracer(0)  # Desactivar la actualización automática del dibujo

    # Dibujar la matriz
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == 0:  # Espacio vacío (blanco)
                turtle.penup()
                turtle.goto(j, filas - i)
                turtle.pendown()
                turtle.begin_fill()
                turtle.fillcolor("white")
                for _ in range(4):
                    turtle.forward(1)
                    turtle.left(90)
                turtle.end_fill()
            else:  # Espacio ocupado (negro)
                turtle.penup()
                turtle.goto(j, filas - i)
                turtle.pendown()
                turtle.begin_fill()
                turtle.fillcolor("black")
                for _ in range(4):
                    turtle.forward(1)
                    turtle.left(90)
                turtle.end_fill()

    # Dibujar nodos de la lista cerrada (rojo)
    for nodo in lista_cerrada:
        turtle.penup()
        turtle.goto(nodo.coordenadas[1], filas - nodo.coordenadas[0])
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor("red")
        for _ in range(4):
            turtle.forward(1)
            turtle.left(90)
        turtle.end_fill()

    # Dibujar nodos de la lista abierta (verde)
    for nodo in lista_abierta:
        turtle.penup()
        turtle.goto(nodo.coordenadas[1], filas - nodo.coordenadas[0])
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor("green")
        for _ in range(4):
            turtle.forward(1)
            turtle.left(90)
        turtle.end_fill()

    # Dibujar recorrido final (azul)
    for nodo in recorrido_final:
        turtle.penup()
        turtle.goto(nodo.coordenadas[1], filas - nodo.coordenadas[0])
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor("blue")
        for _ in range(4):
            turtle.forward(1)
            turtle.left(90)
        turtle.end_fill()

    turtle.update()  # Actualizar la pantalla después de dibujar todo


#########################################################################################################
                                # Fin Grafica    
#########################################################################################################



#Se crea la clase Nodo
class Nodo:
    def __init__(self, coordenadas, padre, G, objetivo):
        self.coordenadas = coordenadas
        self.padre = padre
        self.G = G
        self.objetivo = objetivo
        self.H = abs(self.objetivo[0] - self.coordenadas[0]) + abs(self.objetivo[1] - (self.coordenadas[1]))
        self.F = self.G + self.H

    def __eq__(self, other):
        return self.coordenadas == other.coordenadas and self.objetivo == other.objetivo
    #Esta funcion se utiliza para definir la igualdad de dos objetos de la clase Nodo

    def encuentra_vecinos(self, matriz):
        filas = len(matriz)
        columnas = len(matriz[0])
        lista_vecinos = []

        # Verificar vecino superior
        if self.coordenadas[0] > 0 and matriz[self.coordenadas[0] - 1][self.coordenadas[1]] == 0:
            vecino1 = (self.coordenadas[0] - 1, self.coordenadas[1])
            lista_vecinos.append(vecino1)

        # Verificar vecino inferior
        if self.coordenadas[0] < filas - 1 and matriz[self.coordenadas[0] + 1][self.coordenadas[1]] == 0:
            vecino2 = (self.coordenadas[0] + 1, self.coordenadas[1])
            lista_vecinos.append(vecino2)

        # Verificar vecino izquierdo
        if self.coordenadas[1] > 0 and matriz[self.coordenadas[0]][self.coordenadas[1] - 1] == 0:
            vecino3 = (self.coordenadas[0], self.coordenadas[1] - 1)
            lista_vecinos.append(vecino3)

        # Verificar vecino derecho
        if self.coordenadas[1] < columnas - 1 and matriz[self.coordenadas[0]][self.coordenadas[1] + 1] == 0:
            vecino4 = (self.coordenadas[0], self.coordenadas[1] + 1)
            lista_vecinos.append(vecino4)

        return lista_vecinos

    


##### Ciclo while:
## Cada nodo por el que se pase va a tener vecinos,
## esos vecinos van a ir a una lista abierta, hasta que se decida
# cambiar el nodo actual a alguno de ellos, en cuyo caso pasará a 
# formar parte de la lista cerrada.
##############################################
coordenadas_nodo_inicial = [0, 0] #[0,18] #[11,0]#
objetivo =  [12, 6] #[5, 6] #
G = 0
coordenadas_nodo_actual = coordenadas_nodo_inicial
padre = None
lista_abierta = []
lista_cerrada = []
recorrido_final = []

flag = True
nodo_actual = Nodo(coordenadas_nodo_actual, padre, G, objetivo)
recorrido_final.append(nodo_actual)
nodo_mejor = None
j = 0
while flag:
    
    #Primero se agrega el nodo actual a la lista cerrada
    lista_cerrada.append(nodo_actual)
    if nodo_mejor:
        nodo_actual = nodo_mejor
    
    #En esta lista van los vecinos de el nodo actual, que se tienen que comparar con los de la lista abierta
    lista_abierta_aux = [] 
    vecinos = nodo_actual.encuentra_vecinos(matriz)
    #Para crear los vecinos se actualiza el paso. Todos los vecinos del nodo actual van a tener un G igual
    #al G del nodo actual más uno.
    G = nodo_actual.G + 1

    #Se crean los objetos Nodo de los vecinos del nodo actual.
    for i in vecinos:
        coordenadas_nodo = [i[0], i[1]]
        nodo = Nodo(coordenadas_nodo, nodo_actual, G, objetivo)
        lista_abierta_aux.append(nodo)
    
    
    #De la lista abierta auxiliar se eliminan los nodos en los que ya se estuvo
    #es decir, los de la lista cerrada.
    nodos_a_eliminar = []
    for objeto1 in lista_abierta_aux:
        for objeto2 in lista_cerrada:
            if objeto1.coordenadas == objeto2.coordenadas:
                nodos_a_eliminar.append(objeto1)
                break  
    # Eliminar los nodos de la lista abierta auxiliar que están en la lista cerrada
    for nodo_a_eliminar in nodos_a_eliminar:
        lista_abierta_aux.remove(nodo_a_eliminar)

   
    #Buscamos cuales son los nodos que estan en la lista uxiliar, y que
    #tambien estan en  la lista abierta, si el nodo de la lista auxiliar tiene un G menor    
    #reemplazamos es nodo en la lista abierta. Esto se explicaria mejor con un diagrama de flujo
    for objeto1 in lista_abierta.copy():
        for objeto2 in lista_abierta_aux:
            if objeto1.coordenadas == objeto2.coordenadas and objeto1.G > objeto2.G:
                lista_abierta.remove(objeto1)
                lista_abierta.append(objeto2)

    
    #Modificamos nuevamente la lista abierta, agregando los nodos de la lista auxiliar
    #que no esten en la lista abierta
    for objeto in lista_abierta_aux:  
        if objeto not in lista_abierta:
            lista_abierta.append(objeto)

    #De la lista abierta se eliminan los nodos en los que ya se estuvo
    #es decir, los de la lista cerrada.
    for objeto1 in lista_abierta.copy():
        for objeto2 in lista_cerrada:
            if objeto1.coordenadas == objeto2.coordenadas:
                lista_abierta.remove(objeto1)

    #La lista abierta ya está armada:
    #Se busca el nodo con el menor F, y ese pasa a ser el nodo
    #actual. Es decir, se decide a cual nodo se va a pasar.

    F_min = lista_abierta[0].F
    nodo_mejor = lista_abierta[0]
    for nodo in lista_abierta:
        if nodo.F < F_min:
            F_min = nodo.F
            nodo_mejor = nodo
        

    #Si el nodo actual es el nodo objetivo se detiene el bucle
    if nodo_actual.coordenadas == objetivo or j == 10000:
       flag = False
    j = j + 1
    
    
#Se obtiene el recorrido final recorriendo el padre del padre del padre... del nodo actual
while nodo_actual.padre:
    recorrido_final.append(nodo_actual)
    print(nodo_actual.coordenadas)
    nodo_actual = nodo_actual.padre
    

dibujar_matriz(matriz, lista_cerrada, lista_abierta, recorrido_final)

# Mantener la ventana abierta hasta que se cierre manualmente
turtle.done()
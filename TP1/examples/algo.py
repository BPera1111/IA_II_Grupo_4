#(1) se tiene posición inicial y posición final
#(2) se evalua si el nodo inicio es el nodo objetivo
#(3) Expandimos los nodos adyasentes almacenandolos a la pila de exploración
#(4) luego de almacenar con los nodos explorados, se usa la función de evaluación f(n) = g(n) + h(n) para hacer un ordenamiento en la pila (a la izquierda menor valor)
#(5) Se toma el primero a la izquierda y se evalua si es el objetivo,
    # si es el objetifo: fin
    # sinó es el objetivo: el nodo seleccionado pasa a ser el nodo actual y se repite desde el punto (3)



def tablero(): #retorna la matriz (tablero)
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
    return matriz

class Nodo:
    def __init__(self, x, y, h, g, f):
        self.x = x
        self.y = y
        self.g = g
        self.f = f
        self.h = h
        self.padre = None
        self.hijo = None

     
    def encuentra_vecinos(self, matriz, objetivo,actual):
        filas = len(matriz)
        columnas = len(matriz[0])
        lista_vecinos = []

        # Verificar vecino superior
        if actual.x > 0 and matriz[actual.x - 1][actual.y] == 0:
            h = abs(objetivo.x - (actual.x - 1)) + abs(objetivo.y - (actual.y))
            f=h+actual.g+1
            vecino1 = Nodo(actual.x - 1, actual.y, h, actual.g,f,)
            lista_vecinos.append(vecino1)

        # Verificar vecino inferior
        if actual.x < filas - 1 and matriz[actual.x + 1][actual.y] == 0:
            h = abs(objetivo.x - (actual.x + 1)) + abs(objetivo.y - actual.y)
            f=h+actual.g+1
            vecino2 = Nodo(actual.x + 1, actual.y, h, actual.g,f)
            lista_vecinos.append(vecino2)

        # Verificar vecino izquierdo
        if actual.y > 0 and matriz[actual.x][actual.y - 1] == 0:
            h = abs(objetivo.x - (actual.x)) + abs(objetivo.y - (actual.y - 1))
            f=h+actual.g+1
            vecino3 = Nodo(actual.x, actual.y - 1, h, actual.g,f)
            lista_vecinos.append(vecino3)

        # Verificar vecino derecho
        if actual.y < columnas - 1 and matriz[actual.x][actual.y + 1] == 0:
            h = abs(objetivo.x - (actual.x)) + abs(objetivo.y - (actual.y + 1))
            f=h+actual.g+1
            vecino4 = Nodo(actual.x, actual.y + 1, h, actual.g,f)
            lista_vecinos.append(vecino4)
        
        # lista_vecinos.sort(key=lambda x: x.f)

        return lista_vecinos
        
class ListaAbiertos:
    def __init__(self):
        self.nodos = []

    def agregar(self, nodo):
        self.nodos.append(nodo)
        self.nodos.sort(key=lambda x: x.f)

    def remover(self, nodo):
        self.nodos.remove(nodo)

    def obtener_nodo_mas_cercano(self):
        return self.nodos[0]

    def contiene(self, nodo):
        for n in self.nodos:
            if n.x == nodo.x and n.y == nodo.y: #and n.g < nodo.g:
                return True
        return False
    
class ListaCerrados:
    def __init__(self):
        self.nodos = []

    def agregar(self, nodo):
        self.nodos.append(nodo)

    def contiene(self, nodo):
        for n in self.nodos:
            if n.x == nodo.x and n.y == nodo.y: #and n.g < nodo.g:
                return True
        return False


class estrella(Nodo):

    def __init__(self, mapa, nodo_inicial, nodo_objetivo):
        self.mapa = mapa
        self.nodo_inicial = nodo_inicial
        self.nodo_objetivo = nodo_objetivo


    def busqueda_a_estrella(self, mapa, nodo_inicial, nodo_objetivo):
        lista_abiertos = ListaAbiertos()
        lista_cerrados = ListaCerrados()
        # Agrega el nodo inicial a la lista de abiertos
        lista_abiertos.agregar(nodo_inicial)

        while True:
            # Obtiene el nodo con la distancia estimada más baja
            nodo_actual = lista_abiertos.obtener_nodo_mas_cercano()
            lista_abiertos.remover(nodo_actual)
            lista_cerrados.agregar(nodo_actual)
            # Si el nodo actual es el objetivo, termina el algoritmo
            if nodo_actual.x == nodo_objetivo.x and nodo_actual.y ==nodo_objetivo.y:
                print("\n\n   anashe")
                print("\nLlegamos a: "+ str(nodo_actual.x)+","+str(nodo_actual.y))
                print("\n\nTamaño de la lista abierta: ",len(lista_abiertos.nodos))
                print("Tamaño de la lista cerrada: ",len(set(lista_cerrados.nodos)))
                print("Lista abierta:")
                for i, nodo in enumerate(lista_abiertos.nodos):
                    print(f"Posición {i+1}: X: {nodo.x}, Y: {nodo.y}, G: {nodo.g}, F: {nodo.f}, H: {nodo.h}")

                print("Lista cerrada:")
                for i, nodo in enumerate(lista_cerrados.nodos):
                    print(f"Posición {i+1}: X: {nodo.x}, Y: {nodo.y}, G: {nodo.g}, F: {nodo.f}, H: {nodo.h}")
              
                # print("Lista abierta: ",lista_abiertos.nodos)
                # print("separaion")
                # print("Lista cerrada: ",lista_cerrados.nodos)
                break
                #return nodo_actual.padre
            # Expande el nodo actual
            for nodo_vecino in self.encuentra_vecinos(mapa, nodo_objetivo, nodo_actual):
                # Calcula la distancia estimada hasta el nodo objetivo
                i=i+1
                print (i)
                costo_estimado = nodo_actual.g + 1 #nodo_vecino.g
                nodo_vecino.g = costo_estimado
                # Si el nodo vecino no está en la lista de cerrados
                print(lista_abiertos.contiene(nodo_vecino))
                if not lista_abiertos.contiene(nodo_vecino) and not lista_cerrados.contiene(nodo_vecino):
                    # Agrega el nodo vecino a la lista de abiertos
                    lista_abiertos.agregar(nodo_vecino)
                    # Actualiza la distancia estimada del nodo vecino
                    

          

# Zona de pruebas
                    
def main():
    tab = tablero()
    
    inicio =[0,0] # input("\nIngrese la posición inicial (x, y): ")
    objetivo =[5,7] # input("Ingrese la posición objetivo (x, y): ")
    # inicio = [int(coord) for coord in inicio.split(",")]
    # objetivo = [int(coord) for coord in objetivo.split(",")]
    h = abs(objetivo[0] - inicio[0]) + abs(objetivo[1] - inicio[1])
    nodo_inicial = Nodo(inicio[0], inicio[1], h, 0, h)
    nodo_objetivo = Nodo(objetivo[0], objetivo[1], h ,0, h)
    estre = estrella(tab, nodo_inicial, nodo_objetivo)
    estre.busqueda_a_estrella(tab, nodo_inicial, nodo_objetivo) 

if __name__ == "__main__":
    main()              
                    

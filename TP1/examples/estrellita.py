#(1) se tiene posición inicial y posición final
#(2) se evalua si el nodo inicio es el nodo objetivo
#(3) Expandimos los nodos adyasentes almacenandolos a la pila de exploración
#(4) luego de almacenar con los nodos explorados, se usa la función de evaluación f(n) = g(n) + h(n) para hacer un ordenamiento en la pila (a la izquierda menor valor)
#(5) Se toma el primero a la izquierda y se evalua si es el objetivo,
    # si es el objetifo: fin
    # sinó es el objetivo: el nodo seleccionado pasa a ser el nodo actual y se repite desde el punto (3)

class tablero:

    def __init__(self,filas,columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = None
        self.crear_tablero()


    def crear_tablero(self): #retorna la matriz (tablero)
        # Definir las dimensiones de la matriz
        # filas = 21  # Puedes cambiar este valor según tus necesidades
        # columnas = 19  # Puedes cambiar este valor según tus necesidades

        # Inicializar una lista vacía para contener la matriz
        self.matriz = []

        # Generar la matriz con las características requeridas
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                # Verificar si la fila o la columna son múltiplos de 4 (para filas y columnas basadas en 0)
                if i % 5 == 0 or i == 0 or j == 0 or j % 3 == 0:
                    fila.append(0)
                else:
                    fila.append(1)
            self.matriz.append(fila)
        
    def actualiza_tablero(self, x, y, valor):
        self.matriz[x][y] = valor
        draw.actualiza_pantalla(self.matriz)



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
        filas = len(matriz.matriz)
        columnas = len(matriz.matriz[0])
        lista_vecinos = [] #mostro a todas las matriz hay que ponerles el .matriz para que entren al atributo del objeto

        # Verificar vecino superior
        if actual.x > 0 and matriz.matriz[actual.x - 1][actual.y] == 0:
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
    
class ListaCerrados:
    def __init__(self):
        self.nodos = []

    def agregar(self, nodo):
        self.nodos.append(nodo)

    def contiene(self, nodo):
        return nodo in self.nodos


class estrella(Nodo):

    def __init__(self, mapa, nodo_inicial, nodo_objetivo):
        self.mapa = mapa.matriz.copy()
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
            print("\nLista abierta: ",lista_abiertos.nodos)
            print("\nLista cerrada: ",lista_cerrados.nodos)
            # Si el nodo actual es el objetivo, termina el algoritmo
            if nodo_actual.x == nodo_objetivo.x and nodo_actual.y ==nodo_objetivo.y:
                print("anashe")
                print(nodo_actual.x)
                print(nodo_actual.y)
                # print("Lista abierta: ",lista_abiertos.nodos)
                # print("separaion")
                # print("Lista cerrada: ",lista_cerrados.nodos)
                break
                #return nodo_actual.padre
            # Expande el nodo actual
            for nodo_vecino in self.encuentra_vecinos(mapa, nodo_objetivo, nodo_actual):
                # Calcula la distancia estimada hasta el nodo objetivo
                costo_estimado = nodo_actual.g + 1 #nodo_vecino.g
                # Si el nodo vecino no está en la lista de cerrados
                if not lista_cerrados.contiene(nodo_vecino):
                    # Agrega el nodo vecino a la lista de abiertos
                    lista_abiertos.agregar(nodo_vecino)
                    # Actualiza la distancia estimada del nodo vecino
                    nodo_vecino.g = costo_estimado

          

# Zona de pruebas
import draw
                    
def main():
    tab = tablero(21, 19)
    print(tab.matriz)
    draw.mostrar_tablero(tab.matriz)
    
    
    inicio = input("Ingrese la posición inicial (x, y): ")
    objetivo = input("Ingrese la posición objetivo (x, y): ")
    inicio = [int(coord) for coord in inicio.split(",")]
    objetivo = [int(coord) for coord in objetivo.split(",")]
    h = abs(objetivo[0] - inicio[0]) + abs(objetivo[1] - inicio[1])
    nodo_inicial = Nodo(inicio[0], inicio[1], h, 0, h)
    nodo_objetivo = Nodo(objetivo[0], objetivo[1], h ,0, h)
    estre = estrella(tab, nodo_inicial, nodo_objetivo)
    estre.busqueda_a_estrella(tab, nodo_inicial, nodo_objetivo) 

if __name__ == "__main__":
    main()              
                    
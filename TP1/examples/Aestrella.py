#(1) se tiene posición inicial y posición final
#(2) se evalua si el nodo inicio es el nodo objetivo
#(3) Expandimos los nodos adyasentes almacenandolos a la pila de exploración
#(4) luego de almacenar con los nodos explorados, se usa la función de evaluación f(n) = g(n) + h(n) para hacer un ordenamiento en la pila (a la izquierda menor valor)
#(5) Se toma el primero a la izquierda y se evalua si es el objetivo,
    # si es el objetifo: fin
    # sinó es el objetivo: el nodo seleccionado pasa a ser el nodo actual y se repite desde el punto (3)

import numpy as np

class Nodo:
    def __init__(self, x, y, costo, padre):
        self.x = x
        self.y = y
        self.costo = costo
        self.padre = padre
        
class ListaAbiertos:
    def __init__(self):
        self.nodos = []

    def agregar(self, nodo):
        self.nodos.append(nodo)

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
    
def busqueda_a_estrella(mapa, nodo_inicial, nodo_objetivo):
    lista_abiertos = ListaAbiertos()
    lista_cerrados = ListaCerrados()

    # Agrega el nodo inicial a la lista de abiertos

    lista_abiertos.agregar(nodo_inicial)

    while True:
        # Obtiene el nodo con la distancia estimada más baja

        nodo_actual = lista_abiertos.obtener_nodo_mas_cercano()

        # Si el nodo actual es el objetivo, termina el algoritmo

        if nodo_actual == nodo_objetivo:
            return nodo_actual.padre

        # Expande el nodo actual

        for nodo_vecino in mapa.obtener_vecinos(nodo_actual):
            # Calcula la distancia estimada hasta el nodo objetivo

            costo_estimado = nodo_actual.costo + nodo_vecino.costo

            # Si el nodo vecino no está en la lista de cerrados

            if not lista_cerrados.contiene(nodo_vecino):
                # Agrega el nodo vecino a la lista de abiertos

                lista_abiertos.agregar(nodo_vecino)

                # Actualiza la distancia estimada del nodo vecino

                nodo_vecino.costo = costo_estimado
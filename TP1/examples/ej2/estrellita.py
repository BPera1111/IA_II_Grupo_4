#(1) se tiene posición inicial y posición final
#(2) se evalua si el nodo inicio es el nodo objetivo
#(3) Expandimos los nodos adyasentes almacenandolos a la pila de exploración
#(4) luego de almacenar con los nodos explorados, se usa la función de evaluación f(n) = g(n) + h(n) para hacer un ordenamiento en la pila (a la izquierda menor valor)
#(5) Se toma el primero a la izquierda y se evalua si es el objetivo,
    # si es el objetifo: fin
    # sinó es el objetivo: el nodo seleccionado pasa a ser el nodo actual y se repite desde el punto (3)

import nodo as Nodo
import tablero as tablero
import draw as draw

class agente:
    def __init__(self,tab):
        self.posicion = None
        self.objetivo = None
        self.listacerrada=[]
        self.historia=None
        self.crear_agente(tab)
    
    def crear_agente(self,tab):
        inicio = input("Ingrese la posición inicial (x, y): ")
        objetivo = int(input("Ingrese la posición objetivo (1-192): "))
        self.posicion = [int(coord) for coord in inicio.split(",")]

        # Buscar el valor 192 en la lista tab.matriz y devolver su posición
        for i, fila in enumerate(tab.matriz):
            if objetivo in fila:
                obj = [i,fila.index(objetivo)]
#                if tab.matriz[i][fila.index(objetivo)+1]==(0 or 'g' or 'r'):
                if tab.matriz[i][fila.index(objetivo)+1] in [0,'g','r']:
                    self.objetivo = (i, fila.index(objetivo)+1)
                    print("derecha")
                else:
                    self.objetivo = (i, fila.index(objetivo)-1)
                    print("izquierda")
                tab.actualiza_tablero(obj[0],obj[1], "w")
                break
        print("Posición del valor:", self.objetivo)


    def busqueda(self, tablero):
        h = abs(self.posicion[0] - self.objetivo[0]) + abs(self.posicion[1] - self.objetivo[1])
        nodo_inicial = Nodo.Nodo(self.posicion[0], self.posicion[1], h, 0, h)
        nodo_objetivo = Nodo.Nodo(self.objetivo[0], self.objetivo[1], h, 0, h)
        #tablero.actualiza_tablero(self.objetivo[0],self.objetivo[1], "w")
        estre = Nodo.estrella(tablero, nodo_inicial, nodo_objetivo)
        lista_cerrada=estre.busqueda_a_estrella(tablero, nodo_inicial, nodo_objetivo,self.historia)
        self.listacerrada=lista_cerrada


    def ver_lista_cerrada(self,otro_agente):
        self.historia=otro_agente.listacerrada

    def armar_recorrido(self,tab):
        final=self.listacerrada[-1]
        recorrido = []
        x = True
        while x:
            if final.padre == None:x = False
            
            print("Posición: ",final.x,final.y,final.g)
            recorrido.append([final.x,final.y,final.g])
            # tab.actualiza_tablero(final.x, final.y, 5)
            final = final.padre
        #for i in reversed(recorrido):
            #tab.actualiza_tablero(i[0], i[1], "c")
        self.listacerrada=recorrido
    
    def dibujar_camino(self,tab):
        for i in self.listacerrada:
            tab.actualiza_tablero(i[0], i[1], "c")

    

# Zona de pruebas
                    
def main():
    tab = tablero.tablero(21, 19)
    draw.mostrar_tablero(tab.matriz)

    #agente1
    a1 = agente(tab)
    a1.busqueda(tab)
    a1.armar_recorrido(tab)
    #agente2
    a2 = agente(tab)
    a2.ver_lista_cerrada(a1)
    a2.busqueda(tab)
    a2.armar_recorrido(tab)

    a1.dibujar_camino(tab)
    a2.dibujar_camino(tab)
   
    

if __name__ == "__main__":
    
    main()              
                    
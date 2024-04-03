import nodo as Nodo

class agente:
    def __init__(self,tab,num_agente):
        self.posicion = None #posicion inicial
        self.objetivo = None #posicion objetivo
        self.listacerrada=[] #lista de nodos que forman el camino
        self.historia=[] #historia de los agentes anteriores
        self.num_agente=num_agente #numero de agente
        self.crear_agente(tab)
    
    def crear_agente(self,tab):
        inicio = input("Ingrese la posición inicial (x, y): ")
        objetivo = int(input("Ingrese la posición objetivo (1-192): "))
        self.posicion = [int(coord) for coord in inicio.split(",")]
        # Buscar el valor en la lista tab.matriz y devolver su posición
        for i, fila in enumerate(tab.matriz):
            if objetivo in fila:
                obj = [i,fila.index(objetivo)]
                if tab.matriz[i][fila.index(objetivo)+1] in [0,'g','r']:
                    self.objetivo = (i, fila.index(objetivo)+1)
                else:
                    self.objetivo = (i, fila.index(objetivo)-1)
                tab.actualiza_tablero(obj[0],obj[1], "w")
                break
        #print("Posición del valor:", self.objetivo)


    def busqueda(self, tablero):
        h = abs(self.posicion[0] - self.objetivo[0]) + abs(self.posicion[1] - self.objetivo[1])#calculo de la heuristica
        nodo_inicial = Nodo.Nodo(self.posicion[0], self.posicion[1], h, 0, h)#creacion del nodo inicial
        nodo_objetivo = Nodo.Nodo(self.objetivo[0], self.objetivo[1], h, 0, h)#creacion del nodo objetivo
        estre = Nodo.estrella(tablero, nodo_inicial, nodo_objetivo)#creacion del objeto estrella 
        lista_cerrada=estre.busqueda_a_estrella(tablero, nodo_inicial, nodo_objetivo,self.historia)#busqueda del camino
        self.listacerrada=lista_cerrada


    def ver_lista_cerrada(self,otro_agente):
        for i in otro_agente.listacerrada:
            self.historia.append(i)#agrega la historia de los agentes anteriores

    def armar_recorrido(self):
        final=self.listacerrada[-1]#obtiene el ultimo nodo de la lista cerrada, arrancando de atras para adelante
        recorrido = []
        x = True
        while x:
            if final.padre == None:x = False #si el nodo no tiene padre, termina
            print("Posición: ",final.x,final.y,final.g) 
            recorrido.append([final.x,final.y,final.g]) #agrega la posicion del nodo a la lista de recorrido
            final = final.padre #se mueve al nodo padre
        self.listacerrada=recorrido
    
    def dibujar_camino(self,tab):
        for i in self.listacerrada:
            tab.actualiza_tablero(i[0], i[1], self.num_agente)

                    

                    
import listas
import tablero
import copy

class Nodo:
    def __init__(self, x, y, h, g, f):
        self.x = x
        self.y = y
        self.g = g
        self.f = f
        self.h = h
        self.padre = None
        

     
    def encuentra_vecinos(self, matriz, objetivo,actual):
        filas = len(matriz.matriz)
        columnas = len(matriz.matriz[0])
        lista_vecinos = [] #mostro a todas las matriz hay que ponerles el .matriz para que entren al atributo del objeto

        # Verificar vecino superior
        if actual.x > 0 and matriz.matriz[actual.x - 1][actual.y] == 0:
            h = abs(objetivo.x - (actual.x - 1)) + abs(objetivo.y - (actual.y))
            f=h+actual.g+1
            vecino1 = Nodo(actual.x - 1, actual.y, h, actual.g,f,)
            vecino1.padre=actual
            lista_vecinos.append(vecino1)

        # Verificar vecino inferior
        if actual.x < filas - 1 and matriz.matriz[actual.x + 1][actual.y] == 0:
            h = abs(objetivo.x - (actual.x + 1)) + abs(objetivo.y - actual.y)
            f=h+actual.g+1
            vecino2 = Nodo(actual.x + 1, actual.y, h, actual.g,f)
            vecino2.padre = actual
            lista_vecinos.append(vecino2)

        # Verificar vecino izquierdo
        if actual.y > 0 and matriz.matriz[actual.x][actual.y - 1] == 0:
            h = abs(objetivo.x - (actual.x)) + abs(objetivo.y - (actual.y - 1))
            f=h+actual.g+1
            vecino3 = Nodo(actual.x, actual.y - 1, h, actual.g,f)
            vecino3.padre=actual
            lista_vecinos.append(vecino3)


        # Verificar vecino derecho
        if actual.y < columnas - 1 and matriz.matriz[actual.x][actual.y + 1] == 0:
            h = abs(objetivo.x - (actual.x)) + abs(objetivo.y - (actual.y + 1))
            f=h+actual.g+1
            vecino4 = Nodo(actual.x, actual.y + 1, h, actual.g,f)
            vecino4.padre=actual
            lista_vecinos.append(vecino4)
        
        # lista_vecinos.sort(key=lambda x: x.f)

        return lista_vecinos
        


class estrella(Nodo):

    def __init__(self, mapa, nodo_inicial, nodo_objetivo):
        self.mapa = mapa
        self.tab = tablero.tablero(21,19)
        self.nodo_inicial = nodo_inicial
        self.nodo_objetivo = nodo_objetivo


    def busqueda_a_estrella(self, mapa, nodo_inicial, nodo_objetivo,historia):
        lista_abiertos = listas.ListaAbiertos()
        lista_cerrados = listas.ListaCerrados()
        # Agrega el nodo inicial a la lista de abiertos
        lista_abiertos.agregar(nodo_inicial)
        while True:
            check=False
            if historia != None:
                i=0
                temporal=lista_abiertos.obtener_nodo_mas_cercano()
                for casilla in historia:
                    if temporal.x == casilla[0] and temporal.y == casilla[1] and temporal.g == casilla[2]:
                        lista_abiertos.remover(temporal)
                        #esto permite que se quede quieto el agente por un turno
                        temporal.g+=1
                        temporal.f+=1
                        padretemp=copy.copy(temporal.padre)
                        padretemp.g+=1
                        padretemp.f+=1
                        padretemp.padre=temporal.padre
                        temporal.padre=padretemp
                        lista_cerrados.agregar(padretemp)
                        lista_abiertos.agregar(temporal)
                        check=True
                    
                    if temporal.x == casilla[0] and temporal.y == casilla[1] and temporal.g == casilla[2]+1 and temporal.padre.x == historia[i-1][0] and temporal.padre.y == historia[i-1][1]:
                        #esto hace que si se fuesen a cruzar los agentes, el segundo se busque otro camino
                        lista_abiertos.remover(temporal)
                        check=True
                    i+=1
                #el segundo agente no puede pasar por donde termino el primero
                if temporal.x==historia[0][0] and temporal.y == historia[0][1] and temporal.g >= historia[0][2]:
                    lista_abiertos.remover(temporal)
                    check=True

            if not check:    
                nodo_actual = lista_abiertos.obtener_nodo_mas_cercano()
                lista_abiertos.remover(nodo_actual)
                lista_cerrados.agregar(nodo_actual)
                #agrego el 3 para los nodos de la lista cerrada
                mapa.actualiza_tablero(nodo_actual.x, nodo_actual.y,"g")

                # Si el nodo actual es el objetivo, termina el algoritmo
                if nodo_actual.x == nodo_objetivo.x and nodo_actual.y ==nodo_objetivo.y:
                    print("\n\n   anashe")
                    print("\nLlegamos a: "+ str(nodo_actual.x)+","+str(nodo_actual.y))
                    print("\n\nTamaño de la lista abierta: ",len(lista_abiertos.nodos))
                    print("Tamaño de la lista cerrada: ",len(set(lista_cerrados.nodos)))
                    print("Lista abierta:")
                    
                    for i, nodo in enumerate(lista_abiertos.nodos):
                        try:
                            print(f"Posición {i+1}: X: {nodo.x}, Y: {nodo.y}, G: {nodo.g}, F: {nodo.f}, H: {nodo.h}, Padre:  {nodo.padre.x},{nodo.padre.y}")
                        except Exception:
                            print(f"Posición {i+1}: X: {nodo.x}, Y: {nodo.y}, G: {nodo.g}, F: {nodo.f}, H: {nodo.h}, Padre: None")

                    print("Lista cerrada:")
                    for i, nodo in enumerate(lista_cerrados.nodos):
                        try:
                            print(f"Posición {i+1}: X: {nodo.x}, Y: {nodo.y}, G: {nodo.g}, F: {nodo.f}, H: {nodo.h}, Padre: {nodo.padre.x},{nodo.padre.y}")
                        except Exception:
                            print(f"Posición {i+1}: X: {nodo.x}, Y: {nodo.y}, G: {nodo.g}, F: {nodo.f}, H: {nodo.h}, Padre: None")
                                
                    # print("Lista abierta: ",lista_abiertos.nodos)
                    # print("separaion")
                    # print("Lista cerrada: ",lista_cerrados.nodos)
                    return lista_cerrados.nodos
                    #return nodo_actual.padre
                # Expande el nodo actual
                for nodo_vecino in self.encuentra_vecinos(self.tab, nodo_objetivo, nodo_actual):
                    # Calcula la distancia estimada hasta el nodo objetivo
                    costo_estimado = nodo_actual.g + 1 #nodo_vecino.g
                    nodo_vecino.g = costo_estimado
                    # Si el nodo vecino no está en la lista de cerrados
                    #print(lista_abiertos.contiene(nodo_vecino))
                    if not lista_abiertos.contiene(nodo_vecino) and not lista_cerrados.contiene(nodo_vecino):
                        # Agrega el nodo vecino a la lista de abiertos
                        lista_abiertos.agregar(nodo_vecino)
                        self.mapa.actualiza_tablero(nodo_vecino.x, nodo_vecino.y, "r")
                        # Actualiza la distancia estimada del nodo vecino
                    
                    
                    
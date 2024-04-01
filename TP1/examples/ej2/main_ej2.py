import tablero
import draw
import agente

def main():
    tab = tablero.tablero(21, 19)
    draw.mostrar_tablero(tab.matriz)
    cant_agentes = int(input("Ingrese la cantidad de agentes: "))
    agentes = {}
    for i in range(cant_agentes):
        agentes["a"+str(i)] = agente(tab, "a"+str(i))#crea los agentes
        if i>0:
            for j in range(i-1):
                agentes["a"+str(i)].ver_lista_cerrada(agentes["a"+str(j)])#arma la historia de los agentes anteriores para que no se crucen
        agentes["a"+str(i)].busqueda(tab)#busca el camino
        agentes["a"+str(i)].armar_recorrido(tab)#arma el recorrido
        
    for i in range(cant_agentes):
        agentes["a"+str(i)].dibujar_camino(tab)#dibuja el camino

if __name__ == "__main__":
    
    main()              
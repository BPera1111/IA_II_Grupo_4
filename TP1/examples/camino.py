import Ej1 as ej1
import draw

list_cerrada = [(0, 0, 9, 0, 9), (1, 0, 11, 1, 12), (1, 0, 11, 1, 12), (0, 1, 11, 1, 12), (0, 1, 11, 1, 12), (2, 0, 10, 2, 12), (2, 0, 10, 2, 12), (0, 2, 10, 2, 12), (0, 2, 10, 2, 12), (3, 0, 9, 3, 12), (3, 0, 9, 3, 12), (0, 3, 9, 3, 12), (0, 3, 9, 3, 12), (4, 0, 8, 4, 12), (4, 0, 8, 4, 12), (1, 3, 8, 4, 12), (1, 3, 8, 4, 12), (0, 4, 8, 4, 12), (0, 4, 8, 4, 12), (5, 0, 7, 5, 12), (5, 0, 7, 5, 12), (2, 3, 7, 5, 12), (2, 3, 7, 5, 12), (0, 5, 7, 5, 12), (0, 5, 7, 5, 12), (5, 1, 6, 6, 12), (5, 1, 6, 6, 12), (3, 3, 6, 6, 12), (3, 3, 6, 6, 12), (0, 6, 6, 6, 12), (0, 6, 6, 6, 12), (5, 2, 5, 7, 12), (5, 2, 5, 7, 12), (4, 3, 5, 7, 12), (4, 3, 5, 7, 12), (1, 6, 5, 7, 12), (1, 6, 5, 7, 12), (0, 7, 5, 7, 12), (0, 7, 5, 7, 12), (5, 3, 4, 8, 12), (5, 3, 4, 8, 12), (2, 6, 4, 8, 12), (2, 6, 4, 8, 12), (5, 4, 3, 9, 12), (5, 4, 3, 9, 12), (3, 6, 3, 9, 12), (3, 6, 3, 9, 12), (5, 5, 2, 10, 12), (5, 5, 2, 10, 12), (4, 6, 2, 10, 12), (4, 6, 2, 10, 12), (5, 6, 1, 11, 12), (5, 6, 1, 11, 12), (5, 7, 0, 12, 12), (5, 7, 0, 12, 12), (0, 0, 12, 2, 14)]
print(len(list_cerrada))
def list_camino(lista , objetivo):
    lista.pop() 
    lista_ordenada = sorted(list(set(lista)), key=lambda x: x[3])
    
    camino_minimo = []
    
     # Remove the last element from the list
    
    print("\ntest\n")

    print(lista_ordenada)
  
    print("\ntest\n")

    return camino_minimo

def tab_final():
    pass

def main():
    tablero = ej1.tablero()
    list_cerrada, objetivo = ej1.estrellita(tablero)
    camino = list_camino(list_cerrada, objetivo)

    # print("Camino: ", camino)
    # print("Lista cerrada: ", list_cerrada)

    # tablero = tab_final(camino, tablero)
    
    
    # draw.muestra(tablero)






if __name__ == "__main__":
    main()
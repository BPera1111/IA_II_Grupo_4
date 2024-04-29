class ListaAbiertos:
    def __init__(self):
        self.nodos = []

    def agregar(self, nodo):#ordenar la lista de abiertos por f que seria el costo total
        self.nodos.append(nodo)
        self.nodos.sort(key=lambda x: x.f)

    def remover(self, nodo): #remover el nodo de la lista de abiertos
        self.nodos.remove(nodo)

    def obtener_nodo_mas_cercano(self): #obtener el nodo con menor f
        return self.nodos[0]
    
    def contiene(self, nodo):#verificar si el nodo ya esta en la lista de abiertos
        for n in self.nodos:
            if n.x == nodo.x and n.y == nodo.y: 
                return True
        return False
    
class ListaCerrados:
    def __init__(self):
        self.nodos = []

    def agregar(self, nodo): #agregar el nodo a la lista de cerrados
        self.nodos.append(nodo)

    def contiene(self, nodo):#verificar si el nodo ya esta en la lista de cerrados
        for n in self.nodos:
            if n.x == nodo.x and n.y == nodo.y: 
                return True
        return False

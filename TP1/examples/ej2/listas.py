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

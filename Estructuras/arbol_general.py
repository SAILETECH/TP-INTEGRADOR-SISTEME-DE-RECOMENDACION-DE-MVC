from collections import deque

class NodoArbolGeneral:
    def __init__(self, nombre, datos=None):
        self.nombre = nombre
        self.datos = datos  
        self.hijos = []

    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)
        return nodo_hijo

class ArbolGeneral:
    def __init__(self, nombre_raiz="MvC1 Universe"):
        self.raiz = NodoArbolGeneral(nombre_raiz)

    def buscar_nodo(self, nombre):
        """Busca un nodo por su nombre usando recorrido BFS."""
        if not self.raiz:
            return None

        cola = deque([self.raiz])
        while cola:
            actual = cola.popleft()
            if actual.nombre.lower() == nombre.lower():
                return actual
            for hijo in actual.hijos:
                cola.append(hijo)
        return None

    def recorrido_profundidad(self):
        """Recorrido DFS (Depth-First Search)."""
        resultados = []
        def _dfs(nodo, nivel=0):
            if nodo:
                resultados.append((nodo.nombre, nivel, nodo.datos))
                for hijo in nodo.hijos:
                    _dfs(hijo, nivel + 1)
        _dfs(self.raiz)
        return resultados

    def recorrido_amplitud(self):
        """Recorrido BFS (Breadth-First Search)."""
        resultados = []
        if not self.raiz:
            return resultados

        cola = deque([(self.raiz, 0)])
        while cola:
            actual, nivel = cola.popleft()
            resultados.append((actual.nombre, nivel, actual.datos))
            for hijo in actual.hijos:
                cola.append((hijo, nivel + 1))

        return resultados
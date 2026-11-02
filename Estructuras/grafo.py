# estructuras/grafo.py
from collections import deque

class GrafoPersonajes:
    def __init__(self):
        # Representación: Lista de adyacencia (diccionario de conjuntos/listas)
        self.adyacencia = {}

    def agregar_vertice(self, personaje_id):
        if personaje_id not in self.adyacencia:
            self.adyacencia[personaje_id] = []

    def agregar_arista(self, id1, id2):
        """Conecta dos personajes bidireccionalmente (Grafo No Dirigido)."""
        if id1 in self.adyacencia and id2 in self.adyacencia:
            if id2 not in self.adyacencia[id1]:
                self.adyacencia[id1].append(id2)
            if id1 not in self.adyacencia[id2]:
                self.adyacencia[id2].append(id1)

    def bfs_camino_mas_corto(self, inicio, objetivo):
        """
        Busca el camino más corto en cantidad de aristas entre dos personajes.
        Ideal para responder: ¿Cuál es la ruta de relación más corta?
        """
        inicio = inicio.lower().strip()
        objetivo = objetivo.lower().strip()

        if inicio not in self.adyacencia or objetivo not in self.adyacencia:
            return None

        visitados = {inicio}
        cola = deque([[inicio]])

        while cola:
            camino = cola.popleft()
            nodo_actual = camino[-1]

            if nodo_actual == objetivo:
                return camino

            for vecino in self.adyacencia.get(nodo_actual, []):
                if vecino not in visitados:
                    visitados.add(vecino)
                    nuevo_camino = list(camino)
                    nuevo_camino.append(vecino)
                    cola.append(nuevo_camino)
        return None

    def dfs_exploracion_profunda(self, inicio):
        """
        Explora recursivamente toda la red de conexiones en profundidad.
        Ideal para descubrir el clúster completo de personajes interconectados.
        """
        inicio = inicio.lower().strip()
        if inicio not in self.adyacencia:
            return []

        visitados = set()
        resultado = []

        def _dfs(nodo):
            visitados.add(nodo)
            resultado.append(nodo)
            for vecino in self.adyacencia.get(nodo, []):
                if vecino not in visitados:
                    _dfs(vecino)

        _dfs(inicio)
        return resultado
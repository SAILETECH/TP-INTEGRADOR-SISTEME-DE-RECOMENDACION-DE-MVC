# estructuras/grafo_pesado.py
import heapq
from collections import deque

class GrafoPesado:
    def __init__(self):
        self.adyacencia = {}  # {origen: {destino: costo, ...}, ...}

    def agregar_vertice(self, vertice):
        if vertice not in self.adyacencia:
            self.adyacencia[vertice] = {}

    def agregar_arista(self, origen, destino, costo):
        """Agrega una arista dirigida con un costo positivo (ej. diferencia de estilo)."""
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        self.adyacencia[origen][destino] = costo

    def dijkstra(self, inicio, objetivo):
        """
        Calcula el camino mínimo y su costo total usando Dijkstra (Min-Heap).
        Justificación: Grafo dirigido con pesos positivos (costos de transición >= 0).
        Complejidad: O((V + E) log V).
        """
        inicio = inicio.lower().strip()
        objetivo = objetivo.lower().strip()

        if inicio not in self.adyacencia or objetivo not in self.adyacencia:
            return None, float('inf')

        # Cola de prioridad: almacena (costo_acumulado, nodo_actual, camino)
        pq = [(0, inicio, [inicio])]
        distancias = {inicio: 0}
        visitados = set()

        while pq:
            costo_actual, actual, camino = heapq.heappop(pq)

            if actual == objetivo:
                return camino, costo_actual

            if actual in visitados:
                continue
            visitados.add(actual)

            for vecino, peso in self.adyacencia.get(actual, {}).items():
                if vecino in visitados:
                    continue
                nuevo_costo = costo_actual + peso

                if nuevo_costo < distancias.get(vecino, float('inf')):
                    distancias[vecino] = nuevo_costo
                    heapq.heappush(pq, (nuevo_costo, vecino, camino + [vecino]))

        return None, float('inf')

    def ordenamiento_topologico(self):
        """
        Realiza un ordenamiento topológico (Kahn's Algorithm) para dependencias de aprendizaje.
        Útil para saber qué técnica aprender antes que otra (ej: 'Fundamentos' -> 'Combos avanzados').
        """
        in_degree = {v: 0 for v in self.adyacencia}
        for u in self.adyacencia:
            for v in self.adyacencia[u]:
                in_degree[v] += 1

        cola = deque([v for v in in_degree if in_degree[v] == 0])
        orden = []

        while cola:
            u = cola.popleft()
            orden.append(u)
            for v in self.adyacencia.get(u, {}):
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    cola.append(v)

        if len(orden) == len(self.adyacencia):
            return orden
        return ["❌ Error: El grafo contiene ciclos (dependencias circulares)."]
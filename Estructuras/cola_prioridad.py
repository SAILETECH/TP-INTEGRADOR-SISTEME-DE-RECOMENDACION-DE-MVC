# estructuras/cola_prioridad.py

class ColaPrioridadMaxHeap:
    def __init__(self):
        self.heap = []  # Lista que almacena tuplas: (prioridad, personaje)

    def _padre(self, i):
        return (i - 1) // 2

    def _hijo_izq(self, i):
        return 2 * i + 1

    def _hijo_der(self, i):
        return 2 * i + 2

    def insertar(self, prioridad, personaje):
        """Inserta un elemento manteniendo la propiedad de Max-Heap."""
        self.heap.append((prioridad, personaje))
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, i):
        """Reordena hacia arriba (flotación)."""
        while i > 0 and self.heap[self._padre(i)][0] < self.heap[i][0]:
            # Intercambiar con el padre
            self.heap[self._padre(i)], self.heap[i] = self.heap[i], self.heap[self._padre(i)]
            i = self._padre(i)

    def extraer_mayor(self):
        """Extrae el elemento con mayor prioridad (raíz)."""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return raiz

    def _sift_down(self, i):
        """Reordena hacia abajo (hundimiento)."""
        max_idx = i
        izq = self._hijo_izq(i)
        der = self._hijo_der(i)
        n = len(self.heap)

        if izq < n and self.heap[izq][0] > self.heap[max_idx][0]:
            max_idx = izq
        if der < n and self.heap[der][0] > self.heap[max_idx][0]:
            max_idx = der

        if max_idx != i:
            self.heap[i], self.heap[max_idx] = self.heap[max_idx], self.heap[i]
            self._sift_down(max_idx)

    def obtener_top_n(self, n: int):
        """Obtiene los N elementos con mayor prioridad eficientemente."""
        # Creamos una copia de la heap para no destruir la original
        heap_copia = list(self.heap)
        resultados = []
        
        # Extraer N veces (o hasta agotar)
        temp_heap = ColaPrioridadMaxHeap()
        temp_heap.heap = heap_copia
        
        for _ in range(min(n, len(temp_heap.heap))):
            prioridad, personaje = temp_heap.extraer_mayor()
            resultados.append((prioridad, personaje))
            
        return resultados
# estructuras/arbol_binario.py

class NodoArbol:
    def __init__(self, personaje):
        self.personaje = personaje
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, personaje):
        """Inserta un objeto personaje ordenado por su campo 'id'."""
        nuevo_nodo = NodoArbol(personaje)
        if self.raiz is None:
            self.raiz = nuevo_nodo
            return

        actual = self.raiz
        clave_nueva = personaje.id.lower().strip()

        while True:
            clave_actual = actual.personaje.id.lower().strip()
            if clave_nueva < clave_actual:
                if actual.izquierdo is None:
                    actual.izquierdo = nuevo_nodo
                    break
                actual = actual.izquierdo
            elif clave_nueva > clave_actual:
                if actual.derecho is None:
                    actual.derecho = nuevo_nodo
                    break
                actual = actual.derecho
            else:
                actual.personaje = personaje
                break

    def buscar(self, char_id: str):
        """Busca un personaje por ID en O(log n) promedio."""
        clave_buscada = char_id.lower().strip()
        actual = self.raiz

        while actual is not None:
            clave_actual = actual.personaje.id.lower().strip()
            if clave_buscada == clave_actual:
                return actual.personaje
            elif clave_buscada < clave_actual:
                actual = actual.izquierdo
            else:
                actual = actual.derecho

        return None

    def inorder(self):
        """Recorrido In-Order: Izquierda -> Raíz -> Derecha."""
        resultados = []
        def _inorder(nodo):
            if nodo:
                _inorder(nodo.izquierdo)
                resultados.append(nodo.personaje)
                _inorder(nodo.derecho)
        _inorder(self.raiz)
        return resultados

    def preorder(self):
        """Recorrido Pre-Order: Raíz -> Izquierda -> Derecha."""
        resultados = []
        def _preorder(nodo):
            if nodo:
                resultados.append(nodo.personaje)
                _preorder(nodo.izquierdo)
                _preorder(nodo.derecho)
        _preorder(self.raiz)
        return resultados

    def postorder(self):
        """Recorrido Post-Order: Izquierda -> Derecha -> Raíz."""
        resultados = []
        def _postorder(nodo):
            if nodo:
                _postorder(nodo.izquierdo)
                _postorder(nodo.derecho)
                resultados.append(nodo.personaje)
        _postorder(self.raiz)
        return resultados
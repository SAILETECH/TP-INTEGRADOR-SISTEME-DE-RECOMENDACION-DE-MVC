# estructuras/avl.py

class NodoAVL:
    def __init__(self, personaje):
        self.personaje = personaje
        self.izquierdo = None
        self.derecho = None
        self.altura = 1

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def _obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def _obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self._obtener_altura(nodo.izquierdo) - self._obtener_altura(nodo.derecho)


    def _rotacion_derecha(self, y):
        """Rotación Simple Derecha (LL Case)."""
        x = y.izquierdo
        T2 = x.derecho

        # Realizar rotación
        x.derecho = y
        y.izquierdo = T2

        # Actualizar alturas
        y.altura = 1 + max(self._obtener_altura(y.izquierdo), self._obtener_altura(y.derecho))
        x.altura = 1 + max(self._obtener_altura(x.izquierdo), self._obtener_altura(x.derecho))

        return x

    def _rotacion_izquierda(self, x):
        """Rotación Simple Izquierda (RR Case)."""
        y = x.derecho
        T2 = y.izquierdo

        y.izquierdo = x
        x.derecho = T2

        # Actualizar alturas
        x.altura = 1 + max(self._obtener_altura(x.izquierdo), self._obtener_altura(x.derecho))
        y.altura = 1 + max(self._obtener_altura(y.izquierdo), self._obtener_altura(y.derecho))

        return y


    def insertar(self, personaje):
        self.raiz = self._insertar_recursivo(self.raiz, personaje)

    def _insertar_recursivo(self, nodo, personaje):
        if not nodo:
            return NodoAVL(personaje)

        clave_nueva = personaje.id.lower().strip()
        clave_actual = nodo.personaje.id.lower().strip()

        if clave_nueva < clave_actual:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, personaje)
        elif clave_nueva > clave_actual:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, personaje)
        else:
            nodo.personaje = personaje
            return nodo

        nodo.altura = 1 + max(self._obtener_altura(nodo.izquierdo), self._obtener_altura(nodo.derecho))

        balance = self._obtener_balance(nodo)


        if balance > 1 and personaje.id.lower().strip() < nodo.izquierdo.personaje.id.lower().strip():
            return self._rotacion_derecha(nodo)

        
        if balance < -1 and personaje.id.lower().strip() > nodo.derecho.personaje.id.lower().strip():
            return self._rotacion_izquierda(nodo)

        if balance > 1 and personaje.id.lower().strip() > nodo.izquierdo.personaje.id.lower().strip():
            nodo.izquierdo = self._rotacion_izquierda(nodo.izquierdo)
            return self._rotacion_derecha(nodo)

        if balance < -1 and personaje.id.lower().strip() < nodo.derecho.personaje.id.lower().strip():
            nodo.derecho = self._rotacion_derecha(nodo.derecho)
            return self._rotacion_izquierda(nodo)

        return nodo



    def buscar(self, char_id: str):
        """Busca un personaje por ID en O(log n) garantizado."""
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
        resultados = []
        def _inorder(nodo):
            if nodo:
                _inorder(nodo.izquierdo)
                resultados.append(nodo.personaje)
                _inorder(nodo.derecho)
        _inorder(self.raiz)
        return resultados

    def preorder(self):
        resultados = []
        def _preorder(nodo):
            if nodo:
                resultados.append(nodo.personaje)
                _preorder(nodo.izquierdo)
                _preorder(nodo.derecho)
        _preorder(self.raiz)
        return resultados

    def postorder(self):
        resultados = []
        def _postorder(nodo):
            if nodo:
                _postorder(nodo.izquierdo)
                _postorder(nodo.derecho)
                resultados.append(nodo.personaje)
        _postorder(self.raiz)
        return resultados
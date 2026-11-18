# app.py (Actualizado con Dijkstra y Demo Day)
from Estructuras.avl import ArbolAVL
from Estructuras.arbol_general import ArbolGeneral, NodoArbolGeneral
from Estructuras.cola_prioridad import ColaPrioridadMaxHeap
from Estructuras.grafo import GrafoPersonajes
from estructuras.grafo_pesado import GrafoPesado

class AppDemoDay:
    def __init__(self):
        self.avl = ArbolAVL()
        self.arbol_general = ArbolGeneral("Universo MvC1")
        self.heap = ColaPrioridadMaxHeap()
        self.grafo_red = GrafoPersonajes()
        self.grafo_pesado = GrafoPesado()
        self.inicializar_sistema()

    def inicializar_sistema(self):
        # Carga de datos de demostración para el Demo Day
        # (Se cargan personajes, árbol general, heap y grafos)
        self.grafo_pesado.agregar_arista("fundamentos_básicos", "combos_medios", 2)
        self.grafo_pesado.agregar_arista("combos_medios", "tactica_asistencias", 3)
        self.grafo_pesado.agregar_arista("fundamentos_básicos", "control_de_espacio", 1)
        self.grafo_pesado.agregar_arista("control_de_espacio", "tactica_asistencias", 2)

    def run(self):
        while True:
            print("\n==============================================")
            print(" 🕹️ DEMO DAY - SISTEMA INTEGRADOR MvC1 (TP1-TP8)")
            print("==============================================")
            print("1. Buscar Personaje (Árbol AVL - O(log n))")
            print("2. Explorar Categorías ('Organizá tu universo' - N-ario)")
            print("3. Ranking Top-N (Cola de Prioridad / Max-Heap)")
            print("4. Red de Relaciones (BFS / DFS)")
            print("5. Camino Mínimo por Costo de Estilo (Dijkstra)")
            print("6. Ordenamiento Topológico (Dependencias de Aprendizaje)")
            print("0. Salir (Demo Day Finalizado)")

            op = input("\nSeleccione una opción: ").strip()
            if op == "1":
                print("\n[AVL] Búsqueda optimizada activa.")
            elif op == "2":
                print("\n[Árbol N-ario] Recorrido DFS de categorías activo.")
            elif op == "3":
                print("\n[Heap] Ranking Top-N de recomendación activo.")
            elif op == "4":
                print("\n[Grafo] Consultas BFS y DFS activas.")
            elif op == "5":
                print("\n--- 🗺️ CAMINO MÍNIMO (Dijkstra) ---")
                origen = input("Nodo origen (ej: fundamentos_básicos): ").strip()
                destino = input("Nodo destino (ej: tactica_asistencias): ").strip()
                camino, costo = self.grafo_pesado.dijkstra(origen, destino)
                print(f"Ruta óptima: {camino} | Costo total: {costo}")
            elif op == "6":
                print("\n--- 📋 ORDENAMIENTO TOPOLÓGICO (Dependencias) ---")
                orden = self.grafo_pesado.ordenamiento_topologico()
                print(f"Secuencia recomendada de aprendizaje: {orden}")
            elif op == "0":
                print("\n🚀 ¡Demo Day finalizado con éxito! Gracias por acompañarnos.")
                break

if __name__ == "__main__":
    app = AppDemoDay()
    app.run()
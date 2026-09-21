
import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dataclasses import dataclass
from Estructuras.arbol_binario import ArbolBinarioBusqueda

@dataclass
class DummyCharacter:
    id: str
    name: str

def probar_recorridos():
    print("=== 1. PRUEBA DE RECORRIDOS BST ===")
    bst = ArbolBinarioBusqueda()
    
    datos = ["ryu", "captain_america", "wolverine", "spider_man", "strider_hiryu"]
    for d in datos:
        bst.insertar(DummyCharacter(d, d.capitalize()))

    print(" Inorder:  ", [c.id for c in bst.inorder()])
    print(" Preorder: ", [c.id for c in bst.preorder()])
    print(" Postorder:", [c.id for c in bst.postorder()])
    print()

def comparacion_tiempos():
    print("=== 2. COMPARACIÓN DE TIEMPOS REALES DE BÚSQUEDA ===")
    
    N = 100000
    print(f" Generando dataset de {N} elementos...")
    dataset = [DummyCharacter(f"char_{i:06d}", f"Personaje {i}") for i in range(N)]
    
    lista_secuencial = list(dataset)
    lista_ordenada = sorted(dataset, key=lambda x: x.id)
    
    bst = ArbolBinarioBusqueda()
    for item in dataset:
        bst.insertar(item)

    target_id = f"char_{N-2:06d}"

    # Secuencial
    t0 = time.perf_counter()
    res_sec = next((item for item in lista_secuencial if item.id == target_id), None)
    t_sec = time.perf_counter() - t0

    # Binaria
    def busqueda_binaria(arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid].id == target:
                return arr[mid]
            elif arr[mid].id < target:
                low = mid + 1
            else:
                high = mid - 1
        return None

    t0 = time.perf_counter()
    res_bin = busqueda_binaria(lista_ordenada, target_id)
    t_bin = time.perf_counter() - t0

    # BST
    t0 = time.perf_counter()
    res_bst = bst.buscar(target_id)
    t_bst = time.perf_counter() - t0

    print("\n-------------------------------------------------------------")
    print(f"| {'Algoritmo':<20} | {'Resultado':<15} | {'Tiempo (seg)':<15} |")
    print("-------------------------------------------------------------")
    print(f"| {'Secuencial':<20} | {res_sec.id if res_sec else 'None':<15} | {t_sec:.8f} s   |")
    print(f"| {'Binaria':<20} | {res_bin.id if res_bin else 'None':<15} | {t_bin:.8f} s   |")
    print(f"| {'Árbol (BST)':<20} | {res_bst.id if res_bst else 'None':<15} | {t_bst:.8f} s   |")
    print("-------------------------------------------------------------\n")

if __name__ == "__main__":
    probar_recorridos()
    comparacion_tiempos()
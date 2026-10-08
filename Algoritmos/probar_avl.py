
import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dataclasses import dataclass
from Estructuras.arbol_binario import ArbolBinarioBusqueda
from Estructuras.avl import ArbolAVL
from Estructuras.arbol_general import ArbolGeneral, NodoArbolGeneral

@dataclass
class DummyCharacter:
    id: str
    name: str

def probar_rotaciones_y_recorridos():
    print("=== 1. PRUEBA DE AVL (RECORRIDOS Y BALANCE) ===")
    avl = ArbolAVL()
    
   
    datos = ["a_captain", "b_ryu", "c_spider", "d_strider", "e_wolverine"]
    for d in datos:
        avl.insertar(DummyCharacter(d, d.capitalize()))

    print(" Inorder:  ", [c.id for c in avl.inorder()])
    print(" Preorder: ", [c.id for c in avl.preorder()])
    print(" Postorder:", [c.id for c in avl.postorder()])
    print(f" Altura de la raíz AVL: {avl.raiz.altura} (Optimizada)\n")

def probar_arbol_general():
    print("=== 2. PRUEBA DE ÁRBOL GENERAL N-ARIO ===")
    arbol = ArbolGeneral("MvC1")
    faccion = arbol.raiz.agregar_hijo(NodoArbolGeneral("Marvel"))
    estilo = faccion.agregar_hijo(NodoArbolGeneral("Rushdown"))
    estilo.agregar_hijo(NodoArbolGeneral("Spider-Man"))

    print(" Recorrido Amplitud (BFS):")
    for nombre, nivel, _ in arbol.recorrido_amplitud():
        print(f"  Level {nivel}: {nombre}")
    print()

def comparacion_casos_desbalanceados():
    print("=== 3. COMPARACIÓN REAL DE TIEMPOS (BST DESBALANCEADO VS AVL) ===")
    
    N = 20000  
    print(f" Insertando {N} elementos ordenados secuencialmente...")
    dataset = [DummyCharacter(f"char_{i:06d}", f"Personaje {i}") for i in range(N)]

    bst = ArbolBinarioBusqueda()
    avl = ArbolAVL()

    for item in dataset:
        bst.insertar(item)
        avl.insertar(item)

    target_id = f"char_{N-1:06d}" 

    t0 = time.perf_counter()
    res_bst = bst.buscar(target_id)
    t_bst = time.perf_counter() - t0

    t0 = time.perf_counter()
    res_avl = avl.buscar(target_id)
    t_avl = time.perf_counter() - t0

    print("\n------------------------------------------------------------------")
    print(f"| {'Estructura':<20} | {'Resultado':<12} | {'Tiempo Búsqueda (seg)':<22} |")
    print("------------------------------------------------------------------")
    print(f"| {'BST (Degenerado)':<20} | {res_bst.id if res_bst else 'None':<12} | {t_bst:.8f} s            |")
    print(f"| {'AVL (Balanceado)':<20} | {res_avl.id if res_avl else 'None':<12} | {t_avl:.8f} s            |")
    print("------------------------------------------------------------------\n")

if __name__ == "__main__":
    probar_rotaciones_y_recorridos()
    probar_arbol_general()
    comparacion_casos_desbalanceados()
# app.py
from dataclasses import dataclass
from Estructuras.avl import ArbolAVL
from Estructuras.arbol_general import ArbolGeneral, NodoArbolGeneral

@dataclass
class Character:
    id: str
    name: str
    faction: str
    type: str
    style_category: str
    history: str
    pros: str
    cons: str
    best_assists: list
    combos: dict

    def display_info(self):
        print(f"\n=== {self.name.upper()} ({self.faction} - {self.type}) ===")
        print(f"Estilo: {self.style_category}")
        print(f"Historia: {self.history}")
        print(f"Pros: {self.pros}")
        print(f"Contras: {self.cons}")
        print(f"Asistencias: {', '.join(self.best_assists)}")
        print("Combos:")
        for console, combo in self.combos.items():
            print(f"  [{console}]: {combo}")


class CharacterDatabase:
    def __init__(self):
        self.avl = ArbolAVL()
        self.arbol_general = ArbolGeneral("Universo Marvel vs Capcom")
        self.load_data()

    def get_by_id(self, char_id):
        return self.avl.buscar(char_id)

    def load_data(self):
        raw_data = [
            Character(
                "captain_america", "Captain America", "Marvel", "Inicial", "Balanced",
                "Steve Rogers, líder de los Avengers.",
                "Buenos proyectiles y supers que pegan durísimo.",
                "Se queda vendido si pierde el escudo.",
                ["Psylocke", "Colossus", "Cyclops"],
                {"Arcade": "LP, LK, MP, MK -> 236+P", "PS1": "Cuadrado, X -> 236+P", "Dreamcast": "X, A -> 236+P"}
            ),
            Character(
                "spider_man", "Spider-Man", "Marvel", "Inicial", "Rushdown",
                "Peter Parker, ágil y rápido.",
                "Velocidad alta, movilidad aérea y buenos mix-ups.",
                "Poca vida y defensa baja.",
                ["Psylocke", "Sentinel", "Juggernaut"],
                {"Arcade": "LK, MK -> Jump -> LP, MP -> 236+PP", "PS1": "X, Círculo -> Saltar -> 236+L1", "Dreamcast": "A, B -> 236+L/R"}
            ),
            Character(
                "wolverine", "Wolverine", "Marvel", "Inicial", "Rushdown",
                "Mutante con garras de adamantium.",
                "Presión constante en la esquina y combos largos.",
                "Sufre contra zoners por su corto alcance.",
                ["Psylocke", "Colossus", "Magneto"],
                {"Arcade": "c.LK, c.MK -> 236+P", "PS1": "Abajo+X -> 236+P", "Dreamcast": "Abajo+A -> 236+P"}
            ),
            Character(
                "ryu", "Ryu", "Capcom", "Inicial", "Balanced",
                "Luchador que puede transformar su estilo a Ken o Akuma.",
                "Súper versátil por las transformaciones.",
                "Tienes que aprender a jugar 3 personajes en uno.",
                ["Psylocke", "Colossus", "Cyclops"],
                {"Arcade": "c.LK, c.MK -> 236+P", "PS1": "Abajo+X -> 236+P", "Dreamcast": "Abajo+A -> 236+P"}
            ),
            Character(
                "strider_hiryu", "Strider Hiryu", "Capcom", "Inicial", "Rushdown",
                "Ninja de élite con espada de plasma.",
                "Top tier del juego. Teleport y robots insoportables.",
                "Poca salud.",
                ["Psylocke", "Colossus", "Cyclops"],
                {"Arcade": "LP, MP, HP -> 214+P", "PS1": "Cuadrado, Triángulo -> 214+P", "Dreamcast": "X, Y -> 214+P"}
            )
        ]

        for c in raw_data:
            self.avl.insertar(c)

        nodo_marvel = self.arbol_general.raiz.agregar_hijo(NodoArbolGeneral("Marvel"))
        nodo_capcom = self.arbol_general.raiz.agregar_hijo(NodoArbolGeneral("Capcom"))

        estilos_marvel = {}
        estilos_capcom = {}

        for c in raw_data:
            padre_faccion = nodo_marvel if c.faction.lower() == "marvel" else nodo_capcom
            mapa_estilos = estilos_marvel if c.faction.lower() == "marvel" else estilos_capcom

            if c.style_category not in mapa_estilos:
                nodo_estilo = padre_faccion.agregar_hijo(NodoArbolGeneral(f"Estilo: {c.style_category}"))
                mapa_estilos[c.style_category] = nodo_estilo

            mapa_estilos[c.style_category].agregar_hijo(NodoArbolGeneral(c.name, c))


class App:
    def __init__(self):
        self.db = CharacterDatabase()

    def run(self):
        while True:
            print("\n--- MENU MvC1 (TP4/TP5 - AVL & Árbol N-ario) ---")
            print("1. Buscar Personaje (Usa Árbol AVL)")
            print("2. Explorar Categorías (Usa Árbol N-ario)")
            print("3. Asistencias Top")
            print("0. Salir")

            op = input("\nOpción: ")
            if op == "1":
                self.buscar_avl()
            elif op == "2":
                self.explorar_categorias()
            elif op == "3":
                print("\nTop Asistencias: Psylocke (anti-air/combo), Colossus (armor), Cyclops (beam).")
            elif op == "0":
                break

    def buscar_avl(self):
        print("\nPersonajes disponibles en el AVL:")
        for c in self.db.avl.inorder():
            print(f"- [{c.id}] {c.name}")

        cid = input("\nEscribe el ID para ver detalle: ").strip()
        if cid:
            char = self.db.get_by_id(cid)
            if char:
                char.display_info()
            else:
                print("❌ Personaje no encontrado mediante AVL.")

    def explorar_categorias(self):
        print("\n--- JERARQUÍA DEL DOMINIO (Árbol N-ario - DFS) ---")
        elementos = self.db.arbol_general.recorrido_profundidad()
        for nombre, nivel, datos in elementos:
            indentacion = "  " * nivel
            icono = "📁" if nivel < 2 else "👤"
            print(f"{indentacion}{icono} {nombre}")


if __name__ == "__main__":
    main = App()
    main.run()
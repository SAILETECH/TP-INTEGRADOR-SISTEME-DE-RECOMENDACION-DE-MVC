from dataclasses import dataclass

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
        self.characters = {}
        self.load_data()

    def get_by_id(self, char_id):
        return self.characters.get(char_id.lower().strip())

    def filter_chars(self, faction=None, char_type=None):
        results = list(self.characters.values())
        if faction:
            results = [c for c in results if c.faction.lower() == faction.lower()]
        if char_type:
            results = [c for c in results if c.type.lower() == char_type.lower()]
        return results

    def load_data(self):
        # Datos de personajes
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
            self.characters[c.id.lower()] = c


class App:
    def __init__(self):
        self.db = CharacterDatabase()

    def run(self):
        while True:
            print("\n--- MENU MvC1 ---")
            print("1. Buscar por Estilo")
            print("2. Ver Personajes")
            print("3. Asistencias Top")
            print("0. Salir")

            op = input("\nOpción: ")
            if op == "1":
                self.test_estilo()
            elif op == "2":
                self.ver_catalogo()
            elif op == "3":
                print("\nTop Asistencias: Psylocke (anti-air/combo), Colossus (armor), Cyclops (beam).")
            elif op == "0":
                break

    def test_estilo(self):
        print("\nEstilos: (A) Rushdown | (B) Zoner | (C) Tank | (D) Balanced")
        res = input("Elige: ").upper()
        mapping = {"A": "Rushdown", "B": "Zoner", "C": "Tank", "D": "Balanced"}
        estilo = mapping.get(res, "Balanced")

        filtrados = [c for c in self.db.characters.values() if c.style_category == estilo]
        print(f"\nRecomendados ({estilo}):")
        for c in filtrados:
            print(f"- {c.name} ({c.faction})")

    def ver_catalogo(self):
        print("\nPersonajes disponibles:")
        for c in self.db.characters.values():
            print(f"- [{c.id}] {c.name}")

        cid = input("\nEscribe el ID para ver detalle (o Enter para salir): ").strip()
        char = self.db.get_by_id(cid)
        if char:
            char.display_info()


if __name__ == "__main__":
    main = App()
    main.run()
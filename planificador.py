from deque_TAD import Deque, UnderflowError

MENU = """
--- DEQUE: PLANIFICADOR FLEXIBLE ---
1. Agregar tarea urgente (frente)
2. Agregar tarea normal (final)
3. Atender por el frente
4. Atender por el final
5. Ver estado
6. Ver estructura completa
7. Cargar datos de prueba
0. Volver
"""


class Planificador:
    def __init__(self):
        self.cola = Deque[str]()

    def agregar_inicial(self, tarea: str) -> None:
        self.cola.insertar_frente(tarea)

    def agregar_final(self, tarea: str) -> None:
        self.cola.insertar_final(tarea)

    def atender_inicial(self) -> str:
        return self.cola.eliminar_frente()

    def atender_final(self) -> str:
        return self.cola.eliminar_final()

    def mostrar(self) -> None:
        if self.cola.esta_vacio():
            print("  Frente: None | Final: None")
        else:
            print(f"  Frente: {self.cola.consultar_frente()}")
            print(f"  Final: {self.cola.consultar_final()}")
        print(f"  Tareas: {self.cola.tamanio()}")

    def ver_estructura(self) -> None:
        print("  Deque doblemente enlazado (frente -> final):")
        actual = self.cola.frente
        while actual is not None:
            print(f"    Nodo {id(actual)} -> {actual.dato}")
            actual = actual.siguiente
        print("    None")
        print("  (cada nodo guarda tambien 'anterior' hacia el frente)")

    def cargar_datos_de_prueba(self) -> None:
        for tarea in ["Actualizar base de datos", "Imprimir informe"]:
            self.agregar_final(tarea)
        for tarea in ["Respaldo urgente", "Correccion critica"]:
            self.agregar_inicial(tarea)


def menu_planificador():
    planificador = Planificador()

    while True:
        print(MENU)
        opcion = input("Opcion: ").strip()

        if opcion == "0":
            print("Volviendo al menu principal...")
            break

        if opcion == "1":
            tarea = input("Tarea urgente: ")
            planificador.agregar_inicial(tarea)
            print(f"Agregada al frente: {tarea}")
            planificador.mostrar()

        elif opcion == "2":
            tarea = input("Tarea normal: ")
            planificador.agregar_final(tarea)
            print(f"Agregada al final: {tarea}")
            planificador.mostrar()

        elif opcion == "3":
            try:
                print(f"Atendida por el frente: {planificador.atender_inicial()}")
            except UnderflowError as e:
                print(f"Error: {e}")
            planificador.mostrar()

        elif opcion == "4":
            try:
                print(f"Atendida por el final: {planificador.atender_final()}")
            except UnderflowError as e:
                print(f"Error: {e}")
            planificador.mostrar()

        elif opcion == "5":
            planificador.mostrar()

        elif opcion == "6":
            planificador.ver_estructura()

        elif opcion == "7":
            planificador.cargar_datos_de_prueba()
            print("Datos de prueba cargados.")
            planificador.mostrar()

        else:
            print("Opcion no valida.")

        print()


if __name__ == "__main__":
    menu_planificador()

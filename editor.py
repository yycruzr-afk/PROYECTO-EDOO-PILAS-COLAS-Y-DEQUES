from pila import Pila, PilaVaciaError

MENU = """
--- PILA: DESHACER ACCIONES ---
1. Ejecutar accion
2. Deshacer
3. Ver estado
4. Ver estructura completa
5. Cargar datos de prueba
0. Volver
"""


class Editor:
    def __init__(self):
        self.acciones = Pila[str]()

    def ejecutar(self, accion: str) -> None:
        self.acciones.apilar(accion)

    def deshacer(self) -> str:
        return self.acciones.desapilar()

    def mostrar(self) -> None:
        print(f"  Acciones en la pila: {self.acciones.obtener_tamanio()}")
        if self.acciones.esta_vacia():
            print("  Cima: None")
        else:
            print(f"  Cima: {self.acciones.consultar_cima()}")

    def ver_estructura(self) -> None:
        print("  Pila enlazada (cima -> base):")
        actual = self.acciones.cima
        while actual is not None:
            print(f"    Nodo {id(actual)} -> {actual.dato}")
            actual = actual.siguiente
        print("    None (base de la pila)")

    def cargar_datos_de_prueba(self) -> None:
        for accion in [
            "Abrir documento",
            "Escribir parrafo",
            "Insertar tabla",
            "Guardar archivo"
        ]:
            self.ejecutar(accion)


def menu_editor():
    editor = Editor()

    while True:
        print(MENU)
        opcion = input("Opcion: ").strip()

        if opcion == "0":
            print("Volviendo al menu principal...")
            break

        if opcion == "1":
            accion = input("Accion a ejecutar: ")
            editor.ejecutar(accion)
            print(f"Ejecutada: {accion}")
            editor.mostrar()

        elif opcion == "2":
            try:
                print(f"Deshecho: {editor.deshacer()}")
            except PilaVaciaError as e:
                print(f"Error: {e}")
            editor.mostrar()

        elif opcion == "3":
            editor.mostrar()

        elif opcion == "4":
            editor.ver_estructura()

        elif opcion == "5":
            editor.cargar_datos_de_prueba()
            print("Datos de prueba cargados.")
            editor.mostrar()

        else:
            print("Opcion no valida.")

        print()


if __name__ == "__main__":
    menu_editor()

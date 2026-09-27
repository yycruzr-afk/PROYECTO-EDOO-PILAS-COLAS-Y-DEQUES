from cola_circular import ColaCircular

MENU = """
--- COLA CIRCULAR: BUFFER DE CAPTURA ---
1. Capturar dato
2. Procesar dato (desencolar)
3. Consultar frente
4. Ver estado
5. Ver estructura completa
6. Cargar datos de prueba
0. Volver
"""


class BufferCaptura:
    def __init__(self, capacidad: int):
        self.capacidad = capacidad
        self.buffer = ColaCircular[str](capacidad)

    def capturar(self, dato: str) -> None:
        self.buffer.encolar(dato)

    def procesar(self) -> str:
        return self.buffer.desencolar()

    def mostrar(self) -> None:
        print(f"  Frente (indice): {self.buffer.frente}")
        print(f"  Final (indice): {self.buffer.final}")
        print(f"  Cantidad: {self.buffer.cantidad}/{self.capacidad}")
        print(f"  Vacia: {self.buffer.esta_vacia()} | Llena: {self.buffer.esta_llena()}")

    def ver_estructura(self) -> None:
        print(f"  Arreglo circular de capacidad {self.capacidad}:")
        self.buffer.mostrar()

    def cargar_datos_de_prueba(self) -> None:
        for i in range(self.capacidad):
            self.buffer.encolar(f"L{i + 1:02d}")


def menu_captura():
    capacidad = int(input("Capacidad del buffer: ") or 4)
    buffer = BufferCaptura(capacidad)

    while True:
        print(MENU)
        opcion = input("Opcion: ").strip()

        if opcion == "0":
            print("Volviendo al menu principal...")
            break

        if opcion == "1":
            dato = input("Dato a capturar: ")
            try:
                buffer.capturar(dato)
                print(f"Capturado: {dato}")
            except OverflowError as e:
                print(f"Error: {e}")
            buffer.mostrar()

        elif opcion == "2":
            try:
                print(f"Procesado: {buffer.procesar()}")
            except IndexError as e:
                print(f"Error: {e}")
            buffer.mostrar()

        elif opcion == "3":
            try:
                print(f"Frente: {buffer.buffer.consultar_frente()}")
            except IndexError as e:
                print(f"Error: {e}")

        elif opcion == "4":
            buffer.mostrar()

        elif opcion == "5":
            buffer.ver_estructura()

        elif opcion == "6":
            buffer.cargar_datos_de_prueba()
            print("Datos de prueba cargados.")
            buffer.mostrar()

        else:
            print("Opcion no valida.")

        print()


if __name__ == "__main__":
    menu_captura()

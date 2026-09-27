from expresiones import Expresiones

MENU = """
--- PILA: PROCESADOR DE EXPRESIONES ---
1. Infija a postfija
2. Infija a prefija
3. Evaluar postfija
4. Evaluar prefija
5. Cargar datos de prueba
0. Volver
"""

OPERACIONES = {
    "1": ("Infija a Postfija", Expresiones.infija_a_postfija),
    "2": ("Infija a Prefija", Expresiones.infija_a_prefija),
    "3": ("Evaluar Postfija", Expresiones.evaluar_postfija),
    "4": ("Evaluar Prefija", Expresiones.evaluar_prefija),
}

EJEMPLOS = [
    "A + B * (C - D)",
    "(A + B) * (C - D)",
    "A ^ B ^ C",
    "8 2 / 3 -",
    "5.5 2.5 +",
    "2 3 2 ^ ^",
    "- / 8 2 3",
]


def menu_procesador():
    while True:
        print(MENU)
        opcion = input("Opcion: ").strip()

        if opcion == "0":
            print("Volviendo al menu principal...")
            break

        if opcion == "5":
            cargar_datos_de_prueba()
            print()
            continue

        if opcion not in OPERACIONES:
            print("Opcion no valida.")
            print()
            continue

        nombre, metodo = OPERACIONES[opcion]
        expresion = input("Expresion: ")

        try:
            print(f"{nombre}: {metodo(expresion)}")
        except Exception as e:
            print(f"Error: {type(e).__name__}: {e}")

        print()


def cargar_datos_de_prueba():
    print("  Expresiones de ejemplo:")
    for expresion in EJEMPLOS:
        print(f"    {expresion}")
    print("  (copie una en la opcion 1, 2, 3 o 4)")


if __name__ == "__main__":
    menu_procesador()

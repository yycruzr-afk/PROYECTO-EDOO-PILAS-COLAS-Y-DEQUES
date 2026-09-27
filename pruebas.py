import os
import runpy

CARPETA = os.path.dirname(os.path.abspath(__file__)) + "\\pruebas\\"

MENU = """
========================================
    MENU DE PRUEBAS - EDOO
========================================
1. Pilas
2. Expresiones
3. Colas
4. Colas Circulares
5. Deques
0. Salir
========================================
"""

ARCHIVOS = {
    "1": "pruebas_pila.py",
    "2": "pruebas_expresiones.py",
    "3": "prueba_cola.py",
    "4": "prueba_cola_circular.py",
    "5": "Prueba_Deque.py",
}


def correr(archivo):
    runpy.run_path(CARPETA + archivo, run_name="__main__")


while True:
    print(MENU)
    opcion = input("Seleccione una opcion: ").strip()

    if opcion == "0":
        print("Saliendo...")
        break

    if opcion in ARCHIVOS:
        print()
        correr(ARCHIVOS[opcion])
        print()
    else:
        print("Opcion no valida.")

    input("Presione Enter para continuar...")
    print()

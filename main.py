import editor
import mesa_ayuda
import procesador
import captura
import planificador

MENU = """
==================================================
    CENTRO DE SERVICIOS DIGITALES - EDOO
==================================================
1. Deshacer acciones         (Pila)
2. Procesador de expresiones (Pila)
3. Mesa de ayuda             (Cola)
4. Buffer de captura         (Cola circular)
5. Planificador flexible     (Deque)
0. Salir
==================================================
"""

MODULOS = {
    "1": ("Deshacer acciones", editor.menu_editor),
    "2": ("Procesador de expresiones", procesador.menu_procesador),
    "3": ("Mesa de ayuda", mesa_ayuda.menu_mesa_ayuda),
    "4": ("Buffer de captura", captura.menu_captura),
    "5": ("Planificador flexible", planificador.menu_planificador),
}


while True:
    print(MENU)
    opcion = input("Seleccione un modulo: ").strip()

    if opcion == "0":
        print("Saliendo...")
        break

    if opcion in MODULOS:
        nombre, menu = MODULOS[opcion]
        print()
        print(f"### {nombre} ###")
        menu()
    else:
        print("Opcion no valida.")

    print()

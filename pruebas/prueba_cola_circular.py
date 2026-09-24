import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cola_circular import ColaCircular


def probar_cola_circular():
    print("PRUEBAS COLA CIRCULAR")

    cola = ColaCircular[str](3)

    def mostrar_estado():
        arreglo_fisico = getattr(cola, "_ColaCircular__datos")
        print(f"Arreglo: {arreglo_fisico} | Frente={cola.frente} | Final={cola.final} | Cantidad={cola.cantidad}")

    # P01: Insertar en estado parcial
    print("\nP01: Insercion parcial")
    cola.encolar("A")
    mostrar_estado()
    print("Estado: PASO")

    # P02: Llenar la cola hasta capacidad maxima (3/3)
    print("\nP02: Llenar cola")
    cola.encolar("B")
    cola.encolar("C")
    mostrar_estado()
    print("Estado: PASO")

    # P03: Intentar encolar en cola llena para provocar OverflowError
    print("\nP03: Overflow")
    try:
        cola.encolar("D")
    except OverflowError as e:
        print(f"Error capturado: {e}")
        mostrar_estado()
        print("Estado: PASO")

    # P04: Desencolar elemento para liberar un casillero
    print("\nP04: Desencolar (liberacion)")
    atendido = cola.desencolar()
    print(f"Elemento: {atendido}")
    mostrar_estado()
    print("Estado: PASO")

    # P05: Encolar elemento con Wrap Around para reutilizar el indice 0
    print("\nP05: Wrap Around")
    cola.encolar("X")
    mostrar_estado()
    print("Estado: PASO")

    # P06: Desencolar todos los elementos hasta vaciar la cola
    print("\nP06: Vaciado completo")
    e1 = cola.desencolar()
    e2 = cola.desencolar()
    e3 = cola.desencolar()
    print(f"Retirados: {e1}, {e2}, {e3}")
    mostrar_estado()
    print("Estado: PASO")

    # P07: Intentar desencolar en cola vacia para provocar IndexError (Underflow)
    print("\nP07: Underflow")
    try:
        cola.desencolar()
    except IndexError as e:
        print(f"Error capturado: {e}")
        mostrar_estado()
        print("Estado: PASO")


probar_cola_circular()
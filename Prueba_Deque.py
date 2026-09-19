from deque_TAD import Deque, UnderflowError


def mostrar_estado(deque):
    print("Frente:", deque.consultar_frente() if not deque.esta_vacio() else "None")
    print("Final:", deque.consultar_final() if not deque.esta_vacio() else "None")
    print("Tamaño:", deque.tamanio())


def prueba_deque_vacio():
    print("\n========== P01: DEQUE VACÍO ==========")

    deque = Deque()

    print("Estado inicial:")
    print("Frente: None")
    print("Final: None")
    print("Tamaño:", deque.tamanio())

    print("\nOperación: esta_vacio()")
    resultado = deque.esta_vacio()

    print("Esperado: True")
    print("Obtenido:", resultado)

    if resultado:
        print("Resultado: PASÓ")
    else:
        print("Resultado: FALLÓ")


def prueba_insertar_frente():
    print("\n========== P02: INSERTAR POR EL FRENTE ==========")

    deque = Deque()

    print("Operación: insertar_frente(10)")
    deque.insertar_frente(10)

    mostrar_estado(deque)

    if deque.consultar_frente() == 10 and deque.consultar_final() == 10:
        print("Resultado: PASÓ")
    else:
        print("Resultado: FALLÓ")


def prueba_insertar_final():
    print("\n========== P03: INSERTAR POR EL FINAL ==========")

    deque = Deque()

    print("Operación: insertar_final(20)")
    deque.insertar_final(20)

    print("Operación: insertar_final(30)")
    deque.insertar_final(30)

    mostrar_estado(deque)

    if (deque.consultar_frente() == 20 and
            deque.consultar_final() == 30 and
            deque.tamanio() == 2):
        print("Resultado: PASÓ")
    else:
        print("Resultado: FALLÓ")


def prueba_insertar_ambos_extremos():
    print("\n========== P04: INSERTAR POR AMBOS EXTREMOS ==========")

    deque = Deque()

    print("Operación: insertar_final(20)")
    deque.insertar_final(20)

    print("Operación: insertar_frente(10)")
    deque.insertar_frente(10)

    print("Operación: insertar_final(30)")
    deque.insertar_final(30)

    mostrar_estado(deque)

    if (deque.consultar_frente() == 10 and
            deque.consultar_final() == 30 and
            deque.tamanio() == 3):
        print("Resultado: PASÓ")
    else:
        print("Resultado: FALLÓ")


def prueba_eliminar_frente():
    print("\n========== P05: ELIMINAR POR EL FRENTE ==========")

    deque = Deque()

    deque.insertar_final(10)
    deque.insertar_final(20)
    deque.insertar_final(30)

    print("Estado antes:")
    mostrar_estado(deque)

    print("\nOperación: eliminar_frente()")
    eliminado = deque.eliminar_frente()

    print("Elemento eliminado:", eliminado)

    print("\nEstado después:")
    mostrar_estado(deque)

    if (eliminado == 10 and
            deque.consultar_frente() == 20 and
            deque.tamanio() == 2):
        print("Resultado: PASÓ")
    else:
        print("Resultado: FALLÓ")


def prueba_eliminar_final():
    print("\n========== P06: ELIMINAR POR EL FINAL ==========")

    deque = Deque()

    deque.insertar_final(10)
    deque.insertar_final(20)
    deque.insertar_final(30)

    print("Estado antes:")
    mostrar_estado(deque)

    print("\nOperación: eliminar_final()")
    eliminado = deque.eliminar_final()

    print("Elemento eliminado:", eliminado)

    print("\nEstado después:")
    mostrar_estado(deque)

    if (eliminado == 30 and
            deque.consultar_final() == 20 and
            deque.tamanio() == 2):
        print("Resultado: PASÓ")
    else:
        print("Resultado: FALLÓ")


def prueba_de_un_nodo_a_cero():
    print("\n========== P07: DE UN NODO A CERO ==========")

    deque = Deque()

    deque.insertar_final(100)

    print("Estado antes:")
    mostrar_estado(deque)

    print("\nOperación: eliminar_frente()")
    eliminado = deque.eliminar_frente()

    print("Elemento eliminado:", eliminado)

    print("\nEstado después:")
    print("Frente:", deque.frente)
    print("Final:", deque.final)
    print("Tamaño:", deque.tamanio())

    if (eliminado == 100 and
            deque.frente is None and
            deque.final is None and
            deque.tamanio() == 0):
        print("Resultado: PASÓ")
    else:
        print("Resultado: FALLÓ")


def prueba_uso_como_pila():
    print("\n========== P08: DEQUE COMO PILA (LIFO) ==========")

    deque = Deque()

    print("Insertamos: 10, 20, 30 por el final")

    deque.insertar_final(10)
    deque.insertar_final(20)
    deque.insertar_final(30)

    print("\nEstado:")
    mostrar_estado(deque)

    print("\nEliminamos por el final:")

    primero = deque.eliminar_final()
    segundo = deque.eliminar_final()
    tercero = deque.eliminar_final()

    print("Orden de salida:", primero, segundo, tercero)

    if primero == 30 and segundo == 20 and tercero == 10:
        print("Resultado: PASÓ - comportamiento LIFO")
    else:
        print("Resultado: FALLÓ")


def prueba_uso_como_cola():
    print("\n========== P09: DEQUE COMO COLA (FIFO) ==========")

    deque = Deque()

    print("Insertamos: 10, 20, 30 por el final")

    deque.insertar_final(10)
    deque.insertar_final(20)
    deque.insertar_final(30)

    print("\nEstado:")
    mostrar_estado(deque)

    print("\nEliminamos por el frente:")

    primero = deque.eliminar_frente()
    segundo = deque.eliminar_frente()
    tercero = deque.eliminar_frente()

    print("Orden de salida:", primero, segundo, tercero)

    if primero == 10 and segundo == 20 and tercero == 30:
        print("Resultado: PASÓ - comportamiento FIFO")
    else:
        print("Resultado: FALLÓ")


def prueba_underflow():
    print("\n========== P10: UNDERFLOW ==========")

    deque = Deque()

    print("Estado:")
    mostrar_estado(deque)

    print("\nIntentamos eliminar por el frente:")

    try:
        deque.eliminar_frente()
        print("Resultado: FALLÓ")
    except UnderflowError as e:
        print("Excepción controlada:", e)
        print("Resultado: PASÓ")


def ejecutar_pruebas():
    prueba_deque_vacio()
    prueba_insertar_frente()
    prueba_insertar_final()
    prueba_insertar_ambos_extremos()
    prueba_eliminar_frente()
    prueba_eliminar_final()
    prueba_de_un_nodo_a_cero()
    prueba_uso_como_pila()
    prueba_uso_como_cola()
    prueba_underflow()


if __name__ == "__main__":
    ejecutar_pruebas()
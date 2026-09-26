from pila import Pila, PilaVaciaError

def prueba_pila_vacia():
    print("\n========== P01: PILA VACÍA ==========")

    pila = Pila()

    print("Estado antes:")
    print("Cima: None")
    print("Tamaño:", pila.obtener_tamanio())

    resultado = pila.esta_vacia()

    print("\nOperación: esta_vacia()")
    print("Esperado: True")
    print("Obtenido:", resultado)

    if resultado is True:
        print("Estado: APROBADO")
    else:
        print("Estado: NO APROBADO")


def prueba_un_elemento():
    print("\n========== P02: UN ELEMENTO ==========")

    pila = Pila()

    print("Estado antes:")
    print("Cima: None")
    print("Tamaño:", pila.obtener_tamanio())

    pila.apilar(10)

    print("\nOperación: apilar(10)")

    esperado_cima = 10
    esperado_tamanio = 1

    obtenido_cima = pila.consultar_cima()
    obtenido_tamanio = pila.obtener_tamanio()

    print("Estado después:")
    print("Cima:", obtenido_cima)
    print("Tamaño:", obtenido_tamanio)

    print("\nEsperado:")
    print("Cima:", esperado_cima)
    print("Tamaño:", esperado_tamanio)

    print("\nObtenido:")
    print("Cima:", obtenido_cima)
    print("Tamaño:", obtenido_tamanio)

    if (obtenido_cima == esperado_cima and
            obtenido_tamanio == esperado_tamanio):
        print("Estado: APROBADO")
    else:
        print("Estado: NO APROBADO")


def prueba_varios_elementos():
    print("\n========== P03: VARIOS ELEMENTOS ==========")

    pila = Pila()

    print("Estado antes:")
    print("Cima: None")
    print("Tamaño:", pila.obtener_tamanio())

    pila.apilar(10)
    pila.apilar(20)
    pila.apilar(30)

    print("\nOperación: apilar(10), apilar(20), apilar(30)")

    esperado_cima = 30
    esperado_tamanio = 3

    obtenido_cima = pila.consultar_cima()
    obtenido_tamanio = pila.obtener_tamanio()

    print("Estado después:")
    print("Cima:", obtenido_cima)
    print("Tamaño:", obtenido_tamanio)

    print("\nEsperado:")
    print("Cima:", esperado_cima)
    print("Tamaño:", esperado_tamanio)

    print("\nObtenido:")
    print("Cima:", obtenido_cima)
    print("Tamaño:", obtenido_tamanio)

    if (obtenido_cima == esperado_cima and
            obtenido_tamanio == esperado_tamanio):
        print("Estado: APROBADO")
    else:
        print("Estado: NO APROBADO")


def prueba_vaciado():
    print("\n========== P04: VACIADO DE LA PILA ==========")

    pila = Pila()

    pila.apilar(10)
    pila.apilar(20)
    pila.apilar(30)

    print("Estado antes:")
    print("Cima:", pila.consultar_cima())
    print("Tamaño:", pila.obtener_tamanio())

    primero = pila.desapilar()
    segundo = pila.desapilar()
    tercero = pila.desapilar()

    print("\nOperación:")
    print("desapilar() hasta vaciar la pila")

    print("\nElementos retirados:")
    print(primero)
    print(segundo)
    print(tercero)

    print("\nEstado después:")
    print("Cima: None")
    print("Tamaño:", pila.obtener_tamanio())
    print("¿Está vacía?:", pila.esta_vacia())

    esperado = [30, 20, 10]

    obtenido = [primero, segundo, tercero]

    print("\nEsperado:")
    print("Elementos retirados:", esperado)
    print("Pila vacía: True")

    print("\nObtenido:")
    print("Elementos retirados:", obtenido)
    print("Pila vacía:", pila.esta_vacia())

    if (obtenido == esperado and
            pila.esta_vacia() and
            pila.obtener_tamanio() == 0):
        print("Estado: APROBADO")
    else:
        print("Estado: NO APROBADO")


def prueba_underflow():
    print("\n========== P05: UNDERFLOW ==========")

    pila = Pila()

    print("Estado antes:")
    print("Cima: None")
    print("Tamaño:", pila.obtener_tamanio())

    print("\nOperación: desapilar() sobre una pila vacía")

    try:
        pila.desapilar()

        print("Esperado: controlar el error mediante una excepción")
        print("Obtenido: no se produjo ninguna excepción")
        print("Estado: NO APROBADO")

    except PilaVaciaError as e:
        print("Esperado: excepción por intentar desapilar una pila vacía")
        print("Obtenido:", e)
        print("Estado: APROBADO")


def ejecutar_pruebas():
    print("\n========================================")
    print("          PRUEBAS DE LA PILA")
    print("========================================")

    prueba_pila_vacia()
    prueba_un_elemento()
    prueba_varios_elementos()
    prueba_vaciado()
    prueba_underflow()

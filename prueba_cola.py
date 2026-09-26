from cola_enlazada import Cola


def estado_cola(cola: Cola) -> str:
    elementos = []
    actual = cola.frente

    while actual is not None:
        elementos.append(str(actual.dato))
        actual = actual.siguiente

    contenido = " -> ".join(elementos) if elementos else "VACIA"

    return (
        f"Frente: {cola.frente.dato if cola.frente else None}, "
        f"Final: {cola.final.dato if cola.final else None}, "
        f"Tamaño: {cola.tamanio()}, "
        f"Contenido: {contenido}"
    )


def mostrar_prueba(
    numero: str,
    nombre: str,
    antes: str,
    operacion: str,
    despues: str,
    esperado: str,
    obtenido: str,
    aprobado: bool
) -> None:

    print(f"\nP{numero} - {nombre}")
    print(f"Antes: {antes}")
    print(f"Operación: {operacion}")
    print(f"Después: {despues}")
    print(f"Esperado: {esperado}")
    print(f"Obtenido: {obtenido}")
    print(f"Estado: {'APROBADO' if aprobado else 'FALLIDO'}")


def prueba_cola_vacia() -> None:
    cola = Cola()

    antes = estado_cola(cola)

    operacion = "Consultar si está vacía y tamaño"

    vacia = cola.esta_vacia()
    tamanio = cola.tamanio()

    despues = estado_cola(cola)

    esperado = "Cola vacía y tamaño 0"
    obtenido = f"Vacia: {vacia}, Tamaño: {tamanio}"

    aprobado = vacia and tamanio == 0

    mostrar_prueba(
        "01",
        "Cola vacía",
        antes,
        operacion,
        despues,
        esperado,
        obtenido,
        aprobado
    )


def prueba_un_elemento() -> None:
    cola = Cola()

    antes = estado_cola(cola)

    cola.encolar("S01")

    despues = estado_cola(cola)

    esperado = "Frente: S01, Final: S01, Tamaño: 1"
    obtenido = (
        f"Frente: {cola.frente_dato()}, "
        f"Final: {cola.final.dato}, "
        f"Tamaño: {cola.tamanio()}"
    )

    aprobado = (
        cola.frente_dato() == "S01"
        and cola.final.dato == "S01"
        and cola.tamanio() == 1
    )

    mostrar_prueba(
        "02",
        "Un elemento",
        antes,
        "Encolar S01",
        despues,
        esperado,
        obtenido,
        aprobado
    )


def prueba_varios_elementos() -> None:
    cola = Cola()

    cola.encolar("S01")
    cola.encolar("S02")
    cola.encolar("S03")

    antes = estado_cola(cola)

    esperado = "Frente: S01, Final: S03, Tamaño: 3"
    obtenido = (
        f"Frente: {cola.frente_dato()}, "
        f"Final: {cola.final.dato}, "
        f"Tamaño: {cola.tamanio()}"
    )

    despues = estado_cola(cola)

    aprobado = (
        cola.frente_dato() == "S01"
        and cola.final.dato == "S03"
        and cola.tamanio() == 3
    )

    mostrar_prueba(
        "03",
        "Varios elementos",
        antes,
        "Mantener S01, S02 y S03 en la cola",
        despues,
        esperado,
        obtenido,
        aprobado
    )


def prueba_fifo() -> None:
    cola = Cola()

    cola.encolar("S01")
    cola.encolar("S02")
    cola.encolar("S03")

    antes = estado_cola(cola)

    primero = cola.desencolar()
    segundo = cola.desencolar()
    tercero = cola.desencolar()

    despues = estado_cola(cola)

    esperado = "S01 -> S02 -> S03"
    obtenido = f"{primero} -> {segundo} -> {tercero}"

    aprobado = [primero, segundo, tercero] == ["S01", "S02", "S03"]

    mostrar_prueba(
        "04",
        "Conservación FIFO",
        antes,
        "Desencolar tres elementos",
        despues,
        esperado,
        obtenido,
        aprobado
    )


def prueba_vaciado() -> None:
    cola = Cola()

    cola.encolar("S01")
    cola.encolar("S02")
    cola.encolar("S03")

    antes = estado_cola(cola)

    cola.desencolar()
    cola.desencolar()
    cola.desencolar()

    despues = estado_cola(cola)

    esperado = "Frente: None, Final: None, Tamaño: 0"
    obtenido = (
        f"Frente: {cola.frente}, "
        f"Final: {cola.final}, "
        f"Tamaño: {cola.tamanio()}"
    )

    aprobado = (
        cola.esta_vacia()
        and cola.tamanio() == 0
        and cola.frente is None
        and cola.final is None
    )

    mostrar_prueba(
        "05",
        "Vaciado de la cola",
        antes,
        "Desencolar hasta dejar la cola vacía",
        despues,
        esperado,
        obtenido,
        aprobado
    )


def prueba_underflow() -> None:
    cola = Cola()

    antes = estado_cola(cola)

    try:
        cola.desencolar()

        despues = estado_cola(cola)

        esperado = "Debe producirse un error al desencolar una cola vacía"
        obtenido = "No se produjo ningún error"
        aprobado = False

    except Exception as e:

        despues = estado_cola(cola)

        esperado = "Debe producirse un error al desencolar una cola vacía"
        obtenido = f"Se produjo el error: {type(e).__name__}"
        aprobado = True

    mostrar_prueba(
        "06",
        "Underflow",
        antes,
        "Desencolar una cola vacía",
        despues,
        esperado,
        obtenido,
        aprobado
    )


def ejecutar_pruebas() -> None:
    print("========================================")
    print(" PRUEBAS - COLA ENLAZADA")
    print("========================================")

    prueba_cola_vacia()
    prueba_un_elemento()
    prueba_varios_elementos()
    prueba_fifo()
    prueba_vaciado()
    prueba_underflow()


if __name__ == "__main__":
    ejecutar_pruebas()
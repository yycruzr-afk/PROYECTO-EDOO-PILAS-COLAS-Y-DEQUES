from cola_enlazada import Cola
from modelos import Solicitud


class MesaDeAyuda:
    def __init__(self):
        self.cola = Cola[Solicitud]()

    def registrar_solicitud(self, solicitud: Solicitud) -> None:
        actual = self.cola.frente

        while actual is not None:
            if actual.dato.codigo == solicitud.codigo:
                raise ValueError("El código de solicitud ya existe")
            actual = actual.siguiente

        self.cola.encolar(solicitud)

    def consultar_proxima(self) -> Solicitud:
        return self.cola.frente_dato()

    def atender_solicitud(self) -> Solicitud:
        return self.cola.desencolar()

    def mostrar_cola(self) -> None:
        solicitudes = self.cola.mostrar()

        if not solicitudes:
            print("La cola está vacía")
            return

        print("\nSolicitudes pendientes:")
        for solicitud in solicitudes:
            print(solicitud)

    def mostrar_estado(self) -> None:
        if self.cola.esta_vacia():
            frente = "None"
            final = "None"
        else:
            frente = self.cola.frente.dato.codigo
            final = self.cola.final.dato.codigo

        print(f"Frente: {frente}")
        print(f"Final: {final}")
        print(f"Tamaño: {self.cola.tamanio()}")


def prueba_mesa_ayuda():
    mesa = MesaDeAyuda()

    print("=== COLA VACÍA ===")
    mesa.mostrar_estado()

    print("\n=== REGISTRANDO SOLICITUDES ===")

    s1 = Solicitud(
        "S01",
        "Cristopher",
        "Problema con acceso al sistema",
        "08:00"
    )

    s2 = Solicitud(
        "S02",
        "Ana",
        "No puede ingresar a su correo",
        "08:05"
    )

    s3 = Solicitud(
        "S03",
        "Luis",
        "Problema con la plataforma virtual",
        "08:10"
    )

    mesa.registrar_solicitud(s1)
    mesa.mostrar_estado()

    mesa.registrar_solicitud(s2)
    mesa.mostrar_estado()

    mesa.registrar_solicitud(s3)
    mesa.mostrar_estado()

    print("\n=== MOSTRAR COLA ===")
    mesa.mostrar_cola()

    print("\n=== CONSULTAR PRÓXIMA ===")
    print(mesa.consultar_proxima())

    print("\n=== ATENDER SOLICITUD ===")
    atendida = mesa.atender_solicitud()
    print("Atendida:", atendida)
    mesa.mostrar_estado()

    print("\n=== REGISTRAR S04 ===")

    s4 = Solicitud(
        "S04",
        "María",
        "Problema con contraseña",
        "08:20"
    )

    mesa.registrar_solicitud(s4)
    mesa.mostrar_cola()
    mesa.mostrar_estado()

    print("\n=== ATENDIENDO RESTANTES ===")

    while not mesa.cola.esta_vacia():
        print("Atendiendo:", mesa.atender_solicitud())

    mesa.mostrar_estado()

    print("\n=== UNDERFLOW ===")

    try:
        mesa.atender_solicitud()
    except IndexError as e:
        print(e)

    print("\n=== CÓDIGO DUPLICADO ===")

    try:
        mesa.registrar_solicitud(
            Solicitud(
                "S01",
                "Pedro",
                "Solicitud duplicada",
                "09:00"
            )
        )
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    prueba_mesa_ayuda()
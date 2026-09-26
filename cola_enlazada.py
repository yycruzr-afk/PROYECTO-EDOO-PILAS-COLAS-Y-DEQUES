from typing import Generic, TypeVar, Optional

T = TypeVar("T")


class NodoCola(Generic[T]):
    def __init__(self, dato: T):
        self.dato = dato
        self.siguiente: Optional["NodoCola[T]"] = None


class Cola(Generic[T]):
    def __init__(self):
        self.frente: Optional[NodoCola[T]] = None
        self.final: Optional[NodoCola[T]] = None
        self._tamanio = 0

    def encolar(self, dato: T) -> None:
        nuevo = NodoCola(dato)

        if self.esta_vacia():
            self.frente = nuevo
            self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo

        self._tamanio += 1

    def desencolar(self) -> T:
        if self.esta_vacia():
            raise IndexError("Underflow: la cola está vacía")

        dato = self.frente.dato
        self.frente = self.frente.siguiente
        self._tamanio -= 1

        if self._tamanio == 0:
            self.final = None

        return dato

    def frente_dato(self) -> T:
        if self.esta_vacia():
            raise IndexError("La cola está vacía")

        return self.frente.dato

    def esta_vacia(self) -> bool:
        return self.frente is None

    def tamanio(self) -> int:
        return self._tamanio

    def mostrar(self) -> list[T]:
        elementos = []
        actual = self.frente

        while actual is not None:
            elementos.append(actual.dato)
            actual = actual.siguiente

        return elementos
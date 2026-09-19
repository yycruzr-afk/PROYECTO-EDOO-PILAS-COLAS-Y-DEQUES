from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class UnderflowError(Exception):
    pass

class NodoDeque(Generic[T]):
    def __init__(self, dato: T):
        self.dato: T = dato
        self.anterior: Optional["NodoDeque[T]"] = None
        self.siguiente: Optional["NodoDeque[T]"] = None

class Deque(Generic[T]):
    def __init__(self):
        self.frente: Optional["NodoDeque[T]"] = None
        self.final: Optional["NodoDeque[T]"] = None
        # Se usa _tamanio con guion bajo para evitar conflictos con el método tamanio()
        self._tamanio: int = 0

    def esta_vacio(self) -> bool:
        return self._tamanio == 0

    def tamanio(self) -> int:
        return self._tamanio

    def insertar_frente(self, dato: T) -> None:
        nuevo_nodo = NodoDeque(dato)
        if self.esta_vacio():
            self.frente = self.final = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.frente
            self.frente.anterior = nuevo_nodo
            self.frente = nuevo_nodo
        self._tamanio += 1

    def insertar_final(self, dato: T) -> None:
        nuevo_nodo = NodoDeque(dato)
        if self.esta_vacio():
            self.frente = self.final = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.final
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        self._tamanio += 1

    def eliminar_frente(self) -> T:
        if self.esta_vacio():
            raise UnderflowError("Error: El Deque está vacío, no se puede eliminar por el frente.")
        
        dato_eliminado = self.frente.dato
        
        if self.frente == self.final:
            self.frente = self.final = None
        else:
            self.frente = self.frente.siguiente
            self.frente.anterior = None
            
        self._tamanio -= 1
        return dato_eliminado

    def eliminar_final(self) -> T:
        if self.esta_vacio():
            raise UnderflowError("Error: El Deque está vacío, no se puede eliminar por el final.")
        
        dato_eliminado = self.final.dato
        
        if self.frente == self.final:
            self.frente = self.final = None
        else:
            self.final = self.final.anterior
            self.final.siguiente = None
            
        self._tamanio -= 1
        return dato_eliminado

    def consultar_frente(self) -> T:
        if self.esta_vacio():
            raise UnderflowError("Error: El Deque está vacío, no hay frente para consultar.")
        return self.frente.dato

    def consultar_final(self) -> T:
        if self.esta_vacio():
            raise UnderflowError("Error: El Deque está vacío, no hay final para consultar.")
        return self.final.dato
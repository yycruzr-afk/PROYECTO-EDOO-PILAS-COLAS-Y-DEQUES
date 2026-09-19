from typing import Generic, TypeVar

T = TypeVar("T")

class ColaCircular(Generic[T]):
    def __init__(self, capacidad: int) -> None:
        self.__datos = [None] * capacidad
        self.capacidad = capacidad
        self.frente = 0
        self.final = 0
        self.cantidad = 0
        
    def encolar(self, dato: T) -> None:
        
        if self.cantidad == self.capacidad:
            raise OverflowError("Error: La cola circular esta llena")
        
        self.__datos[self.final] = dato
        self.cantidad += 1
        
        if self.final == self.capacidad-1:
            self.final = 0
        else:
            self.final = self.final + 1
            
    def desencolar(self) -> T | None:
        if self.cantidad == 0:
            raise IndexError("Error: La cola esta vacia")
        
        dato_recuperado = self.__datos[self.frente]
        self.__datos[self.frente] = None
        self.cantidad -= 1
        
        if self.frente == self.capacidad - 1:
            self.frente = 0
        else:
            self.frente = self.frente + 1
            
        return dato_recuperado
    
    def consultar_frente(self) -> T | None:
        if self.cantidad == 0:
            raise IndexError("Error: La cola esta vacia")
        
        return self.__datos[self.frente]
    
    def esta_vacia(self) -> bool:
        if self.cantidad == 0:
            return True
        else:
            return False
        
    def esta_llena(self) -> bool:
        if self.cantidad == self.capacidad:
            return True
        else:
            return False
        
    def tamanio(self) -> int:
        return self.capacidad
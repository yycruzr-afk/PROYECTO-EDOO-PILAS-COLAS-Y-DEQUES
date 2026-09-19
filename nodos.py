from typing import Generic, TypeVar, Optional
T = TypeVar("T")
class NodoPila(Generic[T]):
    def __init__(self, dato: T):
        self.dato: T = dato
        self.siguiente: Optional["NodoPila[T]"] = None
        
class NodoDeque(Generic[T]):
    def __init__(self, dato: T):
        self.dato: T = dato
        self.anterior: Optional["NodoDeque[T]"] = None
        self.siguiente: Optional["NodoDeque[T]"] = None

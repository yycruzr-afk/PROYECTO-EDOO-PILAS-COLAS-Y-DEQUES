from typing import Generic, TypeVar
from nodos import NodoPila

T = TypeVar("T")
class PilaVaciaError(Exception):
    pass

class Pila(Generic[T]):
    def __init__(self):
        self.__cima = None
        self.__tamanio = 0

    def apilar(self, dato: T) -> None:
        nuevo = NodoPila(dato)
        nuevo.siguiente = self.__cima
        self.__cima = nuevo
        self.__tamanio += 1

    def desapilar(self) -> T:
        if self.esta_vacia():
            raise PilaVaciaError("Underflow: No se puede desapilar, la pila está vacía.")
        
        dato = self.__cima.dato
        self.__cima = self.__cima.siguiente
        self.__tamanio -= 1
        return dato
    
    def consultar_cima(self) -> T:
        if self.esta_vacia():
            raise PilaVaciaError("Error: No se puede consultar la cima de una pila vacía.")
        
        return self.__cima.dato
    
    def esta_vacia(self) -> bool:
        return self.__cima is None
    
    def obtener_tamanio(self) -> int:
        return self.__tamanio
    
    def mostrar(self) -> None:
        actual = self.__cima
        print("Cima -> ", end="")
        while actual is not None:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("Base")

    def demostracion(self):
        print("===== DEMOSTRACIÓN DE LA PILA =====")
        self.apilar(10)
        print("\n1. apilar(10)")
        self.mostrar()
        
        self.apilar(20)
        print("\n2. apilar(20)")
        self.mostrar()
        
        self.apilar(30)
        print("\n3. apilar(30)")
        self.mostrar()
        
        print("\n4. consultar_cima()")
        print("Elemento de la cima:", self.consultar_cima())
        self.mostrar()
        
        print("\n5. desapilar()")
        print("Elemento eliminado:", self.desapilar())
        self.mostrar()
        
        self.apilar(40)
        print("\n6. apilar(40)")
        self.mostrar()
        
        print("\n7. desapilar()")
        print("Elemento eliminado:", self.desapilar())
        self.mostrar()
        
        print("\n8. desapilar()")
        print("Elemento eliminado:", self.desapilar())
        self.mostrar()
        
        print("\n9. desapilar()")
        print("Elemento eliminado:", self.desapilar())
        self.mostrar()
        
        print("\n10. desapilar() - UNDERFLOW")
        try:
            self.desapilar()
        except PilaVaciaError as e:
            print(e)
            
        self.mostrar()

from typing import Generic, TypeVar
from nodos import NodoPila
T = TypeVar("T")
class Pila(Generic[T]):
    def __init__(self):
        self.cima = None
        self.tamanio = 0

    def apilar(self, dato: T) -> None:
        nuevo = NodoPila(dato)
        nuevo.siguiente = self.cima
        self.cima = nuevo
        self.tamanio += 1

    def desapilar(self) -> T:
        if self.cima is None:
            raise Exception("La pila está vacía")
        dato = self.cima.dato
        self.cima = self.cima.siguiente
        self.tamanio -= 1
        return dato
    
    def consultar_cima(self) -> T:
        if self.cima is None:
            raise Exception("La pila está vacía")
        return self.cima.dato
    
    def esta_vacia(self) -> bool:
        return self.cima is None
    
    def obtener_tamanio(self) -> int:
        return self.tamanio
    
    def mostrar(self) -> None:
        actual = self.cima
        print("Cima -> ", end="")
        while actual is not None:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("Base")

    def demostracion(self):
        print("===== DEMOSTRACIÓN DE LA PILA =====")
        self.apilar(10)
        print("\n1. apilar(10)")
        self.mostrar_estado()
        self.apilar(20)
        print("\n2. apilar(20)")
        self.mostrar_estado()
        self.apilar(30)
        print("\n3. apilar(30)")
        self.mostrar_estado()
        print("\n4. cima()")
        print("Elemento de la cima:", self.cima())
        self.mostrar_estado()
        print("\n5. desapilar()")
        print("Elemento eliminado:", self.desapilar())
        self.mostrar_estado()
        self.apilar(40)
        print("\n6. apilar(40)")
        self.mostrar_estado()
        print("\n7. desapilar()")
        print("Elemento eliminado:", self.desapilar())
        self.mostrar_estado()
        print("\n8. desapilar()")
        print("Elemento eliminado:", self.desapilar())
        self.mostrar_estado()
        print("\n9. desapilar()")
        print("Elemento eliminado:", self.desapilar())
        self.mostrar_estado()
        print("\n10. desapilar() - UNDERFLOW")
        try:
            self.desapilar()
        except Exception as e:
            print("Error:", e)
        self.mostrar_estado()
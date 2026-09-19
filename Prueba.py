from deque import Deque, UnderflowError

def mostrar_estado(d: Deque):
    
    if d.esta_vacio():
        print("Estado actual: [] (Vacío) | Tamaño: 0")
        return
    
    elementos = []
    actual = d.frente
    while actual is not None:
        elementos.append(str(actual.dato))
        actual = actual.siguiente
        
    print(f"Estado actual (Frente -> Final): [{', '.join(elementos)}] | Tamaño: {d.tamanio()}")

def main():
    d = Deque()
    while True:
        print("\n=== DEMOSTRACIÓN DE DEQUE ===")
        print("1. Insertar al frente")
        print("2. Insertar al final")
        print("3. Eliminar del frente")
        print("4. Eliminar del final")
        print("5. Consultar extremos (Frente y Final)")
        print("6. Salir al menú principal")
        
        opcion = input("Elige una opción: ")
        
        try:
            if opcion == '1':
                dato = input("Ingresa el dato a insertar al FRENTE: ")
                d.insertar_frente(dato)
            elif opcion == '2':
                dato = input("Ingresa el dato a insertar al FINAL: ")
                d.insertar_final(dato)
            elif opcion == '3':
                dato_eliminado = d.eliminar_frente()
                print(f"-> Se eliminó '{dato_eliminado}' del frente.")
            elif opcion == '4':
                dato_eliminado = d.eliminar_final()
                print(f"-> Se eliminó '{dato_eliminado}' del final.")
            elif opcion == '5':
                if not d.esta_vacio():
                    print(f"-> Dato en el Frente: {d.consultar_frente()}")
                    print(f"-> Dato en el Final: {d.consultar_final()}")
                else:
                    print("-> El Deque está vacío.")
            elif opcion == '6':
                print("Saliendo de la demostración del Deque...")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
            
            mostrar_estado(d)
            
        except UnderflowError as e:
            print(e)
            mostrar_estado(d)

main()
import sys
import os

# Permite importar los módulos ubicados en la carpeta raíz del proyecto
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from expresiones import Expresiones


def ejecutar_prueba(id_prueba, descripcion, funcion, esperado):
    try:
        obtenido = funcion()

        estado = "OK" if obtenido == esperado else "FALLO"

        print(
            f"{id_prueba} | "
            f"{descripcion} | "
            f"Esperado: {esperado} | "
            f"Obtenido: {obtenido} | "
            f"{estado}"
        )

    except Exception as e:
        print(
            f"{id_prueba} | "
            f"{descripcion} | "
            f"Esperado: {esperado} | "
            f"Obtenido: ERROR: {e} | "
            f"FALLO"
        )


def ejecutar_prueba_error(
    id_prueba,
    descripcion,
    funcion,
    tipo_error
):
    try:
        funcion()

        print(
            f"{id_prueba} | "
            f"{descripcion} | "
            f"Esperado: {tipo_error.__name__} | "
            f"Obtenido: No se produjo error | "
            f"FALLO"
        )

    except tipo_error as e:
        print(
            f"{id_prueba} | "
            f"{descripcion} | "
            f"Esperado: {tipo_error.__name__} | "
            f"Obtenido: {e} | "
            f"OK"
        )

    except Exception as e:
        print(
            f"{id_prueba} | "
            f"{descripcion} | "
            f"Esperado: {tipo_error.__name__} | "
            f"Obtenido: {type(e).__name__}: {e} | "
            f"FALLO"
        )


print("======================================================")
print("       PRUEBAS DE PROCESAMIENTO DE EXPRESIONES")
print("======================================================")
# P01 - INFIJA A POSTFIJA
ejecutar_prueba(
    "P01",
    "Infija a Postfija",
    lambda: Expresiones.infija_a_postfija(
        "A + B * (C - D)"
    ),
    "A B C D - * +"
)
# P02 - INFIJA A PREFIJA
ejecutar_prueba(
    "P02",
    "Infija a Prefija",
    lambda: Expresiones.infija_a_prefija(
        "(A + B) * (C - D)"
    ),
    "* + A B - C D"
)
# P03 - EVALUACIÓN POSTFIJA
ejecutar_prueba(
    "P03",
    "Evaluación Postfija",
    lambda: Expresiones.evaluar_postfija(
        "8 2 / 3 -"
    ),
    1
)
# P04 - EVALUACIÓN PREFIJA
ejecutar_prueba(
    "P04",
    "Evaluación Prefija",
    lambda: Expresiones.evaluar_prefija(
        "- / 8 2 3"
    ),
    1
)
# P05 - PRECEDENCIA
ejecutar_prueba(
    "P05",
    "Precedencia de operadores",
    lambda: Expresiones.infija_a_postfija(
        "A + B * C"
    ),
    "A B C * +"
)
# P06 - PARÉNTESIS
ejecutar_prueba(
    "P06",
    "Paréntesis",
    lambda: Expresiones.infija_a_postfija(
        "(A + B) * C"
    ),
    "A B + C *"
)
# P07 - POTENCIA / ASOCIATIVIDAD DERECHA
ejecutar_prueba(
    "P07",
    "Asociatividad derecha de potencia - Postfija",
    lambda: Expresiones.infija_a_postfija(
        "A ^ B ^ C"
    ),
    "A B C ^ ^"
)
# P08 - NÚMEROS DECIMALES
ejecutar_prueba(
    "P08",
    "Evaluación con decimales",
    lambda: Expresiones.evaluar_postfija(
        "5.5 2 +"
    ),
    7.5
)
# P09 - DIVISIÓN
ejecutar_prueba(
    "P09",
    "Operación de división",
    lambda: Expresiones.evaluar_postfija(
        "8 2 /"
    ),
    4
)
# P10 - RESTA Y ORDEN DE OPERANDOS
ejecutar_prueba(
    "P10",
    "Orden de operandos en resta",
    lambda: Expresiones.evaluar_postfija(
        "8 3 -"
    ),
    5
)
# P11 - DIVISIÓN ENTRE CERO
ejecutar_prueba_error(
    "P11",
    "División entre cero",
    lambda: Expresiones.evaluar_postfija(
        "8 0 /"
    ),
    ZeroDivisionError
)
# P12 - PARÉNTESIS DESBALANCEADOS
ejecutar_prueba_error(
    "P12",
    "Paréntesis desbalanceados",
    lambda: Expresiones.infija_a_postfija(
        "A + (B * C"
    ),
    ValueError
)
# P13 - OPERADORES CONSECUTIVOS
ejecutar_prueba_error(
    "P13",
    "Operadores consecutivos",
    lambda: Expresiones.infija_a_postfija(
        "A + * B"
    ),
    ValueError
)
# P14 - ASOCIATIVIDAD DERECHA EN PREFIJA
ejecutar_prueba(
    "P14",
    "Asociatividad derecha de potencia - Prefija",
    lambda: Expresiones.infija_a_prefija(
        "A ^ B ^ C"
    ),
    "^ A ^ B C"
)
# P15 - EVALUACIÓN DE POTENCIA EN POSTFIJA
ejecutar_prueba(
    "P15",
    "Evaluación de potencia - Postfija",
    lambda: Expresiones.evaluar_postfija(
        "2 3 2 ^ ^"
    ),
    512
)
# P16 - EVALUACIÓN DE POTENCIA EN PREFIJA
ejecutar_prueba(
    "P16",
    "Evaluación de potencia - Prefija",
    lambda: Expresiones.evaluar_prefija(
        "^ 2 ^ 3 2"
    ),
    512
)
# P17 - EXPRESIÓN CON DECIMALES
ejecutar_prueba(
    "P17",
    "Operación con varios decimales",
    lambda: Expresiones.evaluar_postfija(
        "5.5 2.5 +"
    ),
    8
)
# P18 - SÍMBOLO INVÁLIDO
ejecutar_prueba_error(
    "P18",
    "Símbolo inválido",
    lambda: Expresiones.infija_a_postfija(
        "A + B @ C"
    ),
    ValueError
)
# P19 - EXPRESIÓN INCOMPLETA
ejecutar_prueba_error(
    "P19",
    "Expresión incompleta",
    lambda: Expresiones.infija_a_postfija(
        "A + B *"
    ),
    ValueError
)
# P20 - FALTAN OPERANDOS EN POSTFIJA
ejecutar_prueba_error(
    "P20",
    "Faltan operandos en postfija",
    lambda: Expresiones.evaluar_postfija(
        "8 +"
    ),
    ValueError
)
# P21 - FALTAN OPERANDOS EN PREFIJA
ejecutar_prueba_error(
    "P21",
    "Faltan operandos en prefija",
    lambda: Expresiones.evaluar_prefija(
        "+ 8"
    ),
    ValueError
)
# P22 - OPERANDOS DE MÁS EN POSTFIJA
ejecutar_prueba_error(
    "P22",
    "Operandos de más en postfija",
    lambda: Expresiones.evaluar_postfija(
        "8 2 3 +"
    ),
    ValueError
)
print("\n======================================================")
print("                  FIN DE LAS PRUEBAS")
print("======================================================")
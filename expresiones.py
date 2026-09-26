from typing import List, Union
from pila import Pila
Numero = Union[int, float]
class Expresiones:
    OPERADORES = {"+", "-", "*", "/", "^"}
    PRECEDENCIA = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3
    }
    ASOCIATIVIDAD_DERECHA = {"^"}

    # ==========================================================
    # TOKENIZACIÓN
    # ==========================================================
    @staticmethod
    def tokenizar(expresion: str) -> List[str]:
        """
        Divide una expresión en tokens.
        """
        if not isinstance(expresion, str):
            raise TypeError("La expresión debe ser una cadena de texto.")
        expresion = expresion.strip()
        if not expresion:
            raise ValueError("La expresión no puede estar vacía.")
        tokens = []
        i = 0
        while i < len(expresion):
            # Ignorar espacios
            if expresion[i].isspace():
                i += 1
                continue
            # Número entero o decimal
            if expresion[i].isdigit() or expresion[i] == ".":
                inicio = i
                puntos = 0
                while i < len(expresion) and (
                    expresion[i].isdigit() or expresion[i] == "."
                ):
                    if expresion[i] == ".":
                        puntos += 1
                    i += 1
                numero = expresion[inicio:i]
                if puntos > 1:
                    raise ValueError(
                        f"Número decimal inválido: {numero}"
                    )
                if numero == ".":
                    raise ValueError(
                        "El punto debe formar parte de un número."
                    )
                tokens.append(numero)
                continue
            # Identificadores: A, B, variable1, etc.
            if expresion[i].isalpha() or expresion[i] == "_":
                inicio = i
                while (
                    i < len(expresion)
                    and (
                        expresion[i].isalnum()
                        or expresion[i] == "_"
                    )
                ):
                    i += 1
                tokens.append(expresion[inicio:i])
                continue
            # Operadores y paréntesis
            if expresion[i] in Expresiones._simbolos():
                tokens.append(expresion[i])
                i += 1
                continue
            raise ValueError(
                f"Símbolo inválido encontrado: '{expresion[i]}'"
            )
        return tokens
    @staticmethod
    def _simbolos() -> set:
        return Expresiones.OPERADORES | {"(", ")"}

    @staticmethod
    def es_operador(token: str) -> bool:
        return token in Expresiones.OPERADORES

    @staticmethod
    def es_operando(token: str) -> bool:
        return (
            token not in Expresiones.OPERADORES
            and token not in {"(", ")"}
        )

    @staticmethod
    def validar_tokens(tokens: List[str]) -> None:
        if not tokens:
            raise ValueError("La expresión está vacía.")
        balance = 0
        espera_operando = True
        for token in tokens:
            if espera_operando:
                if Expresiones.es_operando(token):
                    espera_operando = False
                elif token == "(":
                    balance += 1
                else:
                    raise ValueError(
                        f"Se esperaba un operando y se encontró: '{token}'"
                    )
            else:
                if Expresiones.es_operador(token):
                    espera_operando = True
                elif token == ")":
                    balance -= 1
                    if balance < 0:
                        raise ValueError(
                            "Existen paréntesis de cierre sin correspondencia."
                        )
                else:
                    raise ValueError(
                        f"Falta un operador antes de: '{token}'"
                    )
        # La expresión no puede terminar esperando un operando
        if espera_operando:
            raise ValueError(
                "La expresión está incompleta: falta un operando."
            )
        # Todos los paréntesis deben estar cerrados
        if balance != 0:
            raise ValueError(
                "Los paréntesis no están balanceados."
            )
    # INFija -> POSTFija
    @staticmethod
    def infija_a_postfija(expresion: str) -> str:
        tokens = Expresiones.tokenizar(expresion)
        Expresiones.validar_tokens(tokens)
        pila = Pila[str]()
        salida = []
        for token in tokens:
            # Operando
            if Expresiones.es_operando(token):
                salida.append(token)
            # Paréntesis izquierdo
            elif token == "(":
                pila.apilar(token)
            # Paréntesis derecho
            elif token == ")":
                while not pila.esta_vacia() and \
                        pila.consultar_cima() != "(":
                    salida.append(pila.desapilar())
                if pila.esta_vacia():
                    raise ValueError(
                        "Paréntesis desbalanceados."
                    )
                # Eliminar '('
                pila.desapilar()
            # Operador
            else:
                while (
                    not pila.esta_vacia()
                    and pila.consultar_cima() != "("
                    and (
                        Expresiones.PRECEDENCIA[
                            pila.consultar_cima()
                        ] > Expresiones.PRECEDENCIA[token]
                        or (
                            Expresiones.PRECEDENCIA[
                                pila.consultar_cima()
                            ] == Expresiones.PRECEDENCIA[token]
                            and token not in Expresiones.ASOCIATIVIDAD_DERECHA
                        )
                    )
                ):
                    salida.append(pila.desapilar())
                pila.apilar(token)
        # Vaciar la pila
        while not pila.esta_vacia():
            operador = pila.desapilar()
            if operador in {"(", ")"}:
                raise ValueError(
                    "Paréntesis desbalanceados."
                )
            salida.append(operador)
        return " ".join(salida)
    # INFija -> PREFIJA
    @staticmethod
    def infija_a_prefija(expresion: str) -> str:
        tokens = Expresiones.tokenizar(expresion)
        Expresiones.validar_tokens(tokens)
        # Invertir tokens y cambiar paréntesis
        tokens_invertidos = []
        for token in reversed(tokens):
            if token == "(":
                tokens_invertidos.append(")")
            elif token == ")":
                tokens_invertidos.append("(")
            else:
                tokens_invertidos.append(token)
        pila = Pila[str]()
        salida = []
        for token in tokens_invertidos:
            if Expresiones.es_operando(token):
                salida.append(token)
            elif token == "(":
                pila.apilar(token)
            elif token == ")":
                while not pila.esta_vacia() and \
                        pila.consultar_cima() != "(":
                    salida.append(pila.desapilar())
                if pila.esta_vacia():
                    raise ValueError(
                        "Paréntesis desbalanceados."
                    )
                pila.desapilar()
            else:
                while (
                    not pila.esta_vacia()
                    and pila.consultar_cima() != "("
                    and (
                        Expresiones.PRECEDENCIA[
                            pila.consultar_cima()
                        ] > Expresiones.PRECEDENCIA[token]
                        or (
                            Expresiones.PRECEDENCIA[
                                pila.consultar_cima()
                            ] == Expresiones.PRECEDENCIA[token]
                            and token in Expresiones.ASOCIATIVIDAD_DERECHA
                        )
                    )
                ):
                    salida.append(pila.desapilar())
                pila.apilar(token)
        while not pila.esta_vacia():
            operador = pila.desapilar()
            if operador in {"(", ")"}:
                raise ValueError(
                    "Paréntesis desbalanceados."
                )
            salida.append(operador)
        # Invertir el resultado
        salida.reverse()
        return " ".join(salida)
    # EVALUACIÓN POSTFIJA
    @staticmethod
    def evaluar_postfija(expresion: str) -> Numero:
        tokens = Expresiones.tokenizar(expresion)
        if not tokens:
            raise ValueError("La expresión está vacía.")
        pila = Pila[float]()
        for token in tokens:
            # Operando
            if Expresiones.es_operando(token):
                try:
                    numero = float(token)
                except ValueError:
                    raise ValueError(
                        f"Para evaluar se necesita un número: '{token}'"
                    )
                pila.apilar(numero)
            # Operador
            elif Expresiones.es_operador(token):
                if pila.obtener_tamanio() < 2:
                    raise ValueError(
                        "Faltan operandos para realizar la operación."
                    )
                derecho = pila.desapilar()
                izquierdo = pila.desapilar()
                resultado = Expresiones._operar(
                    izquierdo,
                    derecho,
                    token
                )
                pila.apilar(resultado)
            else:
                raise ValueError(
                    f"Token inválido: '{token}'"
                )
        if pila.obtener_tamanio() != 1:
            raise ValueError(
                "La expresión postfija es inválida."
            )
        return Expresiones._normalizar_numero(
            pila.desapilar()
        )
    # EVALUACIÓN PREFIJA
    @staticmethod
    def evaluar_prefija(expresion: str) -> Numero:
        tokens = Expresiones.tokenizar(expresion)
        if not tokens:
            raise ValueError("La expresión está vacía.")
        pila = Pila[float]()
        # En prefija se recorre de derecha a izquierda
        for token in reversed(tokens):
            if Expresiones.es_operando(token):
                try:
                    numero = float(token)
                except ValueError:
                    raise ValueError(
                        f"Para evaluar se necesita un número: '{token}'"
                    )
                pila.apilar(numero)
            elif Expresiones.es_operador(token):
                if pila.obtener_tamanio() < 2:
                    raise ValueError(
                        "Faltan operandos para realizar la operación."
                    )
                izquierdo = pila.desapilar()
                derecho = pila.desapilar()
                resultado = Expresiones._operar(
                    izquierdo,
                    derecho,
                    token
                )
                pila.apilar(resultado)
            else:
                raise ValueError(
                    f"Token inválido: '{token}'"
                )
        if pila.obtener_tamanio() != 1:
            raise ValueError(
                "La expresión prefija es inválida."
            )
        return Expresiones._normalizar_numero(
            pila.desapilar()
        )
    # OPERACIONES
    @staticmethod
    def _operar(
        izquierdo: float,
        derecho: float,
        operador: str
    ) -> float:
        if operador == "+":
            return izquierdo + derecho
        if operador == "-":
            return izquierdo - derecho
        if operador == "*":
            return izquierdo * derecho
        if operador == "/":
            if derecho == 0:
                raise ZeroDivisionError(
                    "No se puede dividir entre cero."
                )
            return izquierdo / derecho
        if operador == "^":
            return izquierdo ** derecho
        raise ValueError(
            f"Operador no reconocido: {operador}"
        )
    @staticmethod
    def _normalizar_numero(numero: float) -> Numero:
        if numero.is_integer():
            return int(numero)
        return numero
import math

class CalculadoraPi:
    def __init__(self):
        pass

    def obter_valor_pi(self):
        return math.pi

calculadora = CalculadoraPi()
print("O valor de Pi é:", calculadora.obter_valor_pi())

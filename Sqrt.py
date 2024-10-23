import math

class CalculadoraRaizQuadrada:
    def __init__(self, numero):
        self.numero = numero

    def calcular_raiz_quadrada(self):
        return math.sqrt(self.numero)

calculadora = CalculadoraRaizQuadrada(25)
print("Raiz quadrada de", calculadora.numero, "é:", calculadora.calcular_raiz_quadrada())

import math

class CalculadoraLogaritmoNatural:
    def __init__(self, numero):
        self.numero = numero

    def calcular_logaritmo_natural(self):
        return math.log(self.numero)

calculadora = CalculadoraLogaritmoNatural(10)
print("Logaritmo natural de", calculadora.numero, "é:", calculadora.calcular_logaritmo_natural())

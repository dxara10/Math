import math

class CalculadoraFatorial:
    def __init__(self, numero):
        self.numero = numero

    def calcular_fatorial(self):
        return math.factorial(self.numero)

calculadora = CalculadoraFatorial(5)
print("Fatorial de", calculadora.numero, "é:", calculadora.calcular_fatorial())

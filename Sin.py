import math

class CalculadoraSeno:
    def __init__(self, angulo):
        self.angulo = angulo

    def calcular_seno(self):
        return math.sin(math.radians(self.angulo))

calculadora = CalculadoraSeno(45)
print("Seno de", calculadora.angulo, "graus é:", calculadora.calcular_seno())

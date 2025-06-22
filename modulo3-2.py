import math

class Figura:
    def area(self):
        pass  # Método abstracto

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

figuras = [Circulo(5), Rectangulo(4, 6)]
for figura in figuras:
    print("Área:", figura.area())
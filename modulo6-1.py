# Módulo 6: Poliformisfo, Interfaces y Clases Abstractas

# 1. Polimorfismo en la práctica
# Ej. función que procesa pagos en diferentes métodos

class TarjetaCredito:
    def pagar(self, monto):
        print(f"Pagando {monto} con tarjeta de crédito")

class PayPal:
    def pagar(self, monto):
        print(f"Pagando {monto} con PayPal")


def procesar_pago(objeto, monto):
    """Duck typing: no importa el tipo, solo que tenga el metodo pagar"""
    objeto.pagar(monto)


# uso
tc = TarjetaCredito()
pp = PayPal()

procesar_pago(tc, 100)
procesar_pago(pp, 200)

print()
print()


# 2. Interfaces y clases abstractas
# Ej. uso de abc y @abstractmethod

from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio ** 2

class Rectangulo(FiguraGeometrica):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

# uso
# fg = FiguraGeometrica() No se puede instanciar
c = Circulo(5)
r = Rectangulo(4, 5)
print(c.area())
print(r.area())

print()
print()

# 3. isinstance / issubclass vs Duck Typing
from abc import ABC

class MiInterfaz(ABC):
    pass

class MiClase:
    pass

MiInterfaz.register(MiClase)
print(isinstance(MiClase(), MiInterfaz))

print()
print()


# 4. Protocolos informales

class MiIterable:
    def __iter__(self):
        return iter([1, 2, 3])

for x in MiIterable():
    print(x)


print()
print()













# Implementación general integradora

from abc import ABC, abstractmethod

# Interfaz de pago
class MetodoPago(ABC):
    @abstractmethod
    def pagar(self, monto):
        pass

class TarjetaCredito(MetodoPago):
    def pagar(self, monto):
        print(f"Pagando {monto} con tarjeta de crédito.")

class PayPal(MetodoPago):
    def pagar(self, monto):
        print(f"Pagando {monto} con PayPal.")

# Interfaz de repositorio
class RepositorioDatos(ABC):
    @abstractmethod
    def guardar(self, obj):
        pass

    @abstractmethod
    def recuperar(self, id):
        pass

class RepositorioEnMemoria(RepositorioDatos):
    def __init__(self):
        self.datos = {}

    def guardar(self, obj):
        self.datos[obj['id']] = obj

    def recuperar(self, id):
        return self.datos.get(id)

# Protocolo iterable
class ColeccionPagos:
    def __init__(self, pagos):
        self.pagos = pagos

    def __iter__(self):
        return iter(self.pagos)

# uso integrado
def procesar_pagos(pagos, monto):
    for pago in pagos:
        pago.pagar(monto)

tc = TarjetaCredito()
pp = PayPal()
procesar_pagos([tc, pp], 150)
print()

repo = RepositorioEnMemoria()
repo.guardar({'id': 2, 'nombre': 'Ana'})
print(repo.recuperar(2))
print()

coleccion = ColeccionPagos([tc, pp])
for metodo in coleccion:
    metodo.pagar(50)

# fin de implemtación
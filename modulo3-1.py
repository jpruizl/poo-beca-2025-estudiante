"""
Los cuatro pilares fundamenentales de la POO
Aplicando los principios de:
1. Abstracción
2. Encapsulamiento
3. Herrencia
4. Polimorfismo
"""

# Abstracción
# consiste en mostrar solo los detalles esenciales de un
# objeto, ocultando su complejidad interna.

print('Ej. Abstracción')
class Cafetera:
    def encender(self):
        print('Cafetera encendida')

    def preparar_cafe(self):
        print('Preparando cafe')


cafetera = Cafetera()
cafetera.preparar_cafe()

print()

# Encapsulamiento
# Es el principio de ocultar datos internos y proteger el
# estado del objeto. Se logra restringiendo el acceso a 
# ciertos atributos/métodos.

# Convenciones en Python:
# _atributo: atributo 'protegido' uso interno (por convención)
# __atributo: nombre manipulado (name mangling), más protegido.

print('Ej. Encapsulamiento')
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo # encapsulamiento
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
    
    def obtener_saldo(self):
        return self.__saldo


cuenta = CuentaBancaria('Juan', 1000)
cuenta.depositar(500)
print(cuenta.obtener_saldo())
# print(cuenta.__saldo)
print(cuenta.titular)

print()

# Herencia
# Permite que una clase herede atributos y métodos de otra clase.
# Promueve la reutilización del código.

print('Ej. Herencia')
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print('El animal hace un sonido')

class Perro(Animal):
    def hablar(self):
        print(f'{self.nombre} dice ¡Guau!')


class Gato(Animal):
    def hablar(self):
        print(f'{self.nombre} dice ¡Miau!')


class Cangrejo(Animal):
    pass

p = Perro('Fido')
p.hablar()

print()

g = Gato('Whiskers')
g.hablar()

print()

c = Cangrejo('Nemo')
c.hablar()

print


# Polimorfismo
# Capacidad de usar el mismo método en diferentes objetos y 
# obtener comportamiento distintos.

print('Ej. Polimorfismo')
class Gato:
    def hablar(self):
        print('Miau')

class Perro:
    def hablar(self):
        print('Guau')


# Polimorfismo
animales = [Gato(), Perro()]
for animal in animales:
    animal.hablar()

print()
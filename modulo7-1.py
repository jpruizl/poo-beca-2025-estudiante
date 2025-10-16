# Módulo 7: Integración de Caracteristicas Avanzadas de Clases en Python

"""
Conceptos avanzados de POO aplicando métodos especiales, propiedades,
métodos de clase y estáticos, atributos de clase e instancia, encapsulamiento
y manejo de excepciones personalizadas.
"""

# Ej.1 - Métodos Especiales "dunder methods" y Sobrecarga de Operadores
# Ejemplo: Personalizando la representación y la suma de objetos

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):  # dunder method para representación como string
        return f"({self.x}, {self.y})"

    def __add__(self, otro):  # dunder method para sobrecargar el operador +
        return Punto(self.x + otro.x, self.y + otro.y)

    def __eq__(self, otro): # dunder method para sobrecargar el operador ==
        return self.x == otro.x and self.y == otro.y


# Prueba
p1 = Punto(1, 2)
p2 = Punto(3, 4)
p3 = p1 + p2  # Internamente llama a p1.__add__(p2)
print(p3)  # Internamente llama a p3.__str__()
print(p1 == Punto(1,2))  # True -> Internamente llama a p1.__eq__(Punto(1,2))

print()
print()

# Ej.2 - Métodos de Clase vs. Métodos Estáticos

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def desde_cadena(cls, cadena):
        nombre, edad = cadena.split(",")
        return cls(nombre, int(edad))

    @staticmethod
    def es_mayor_de_edad(edad):
        return edad >= 18

# Prueba
p = Persona.desde_cadena("Ana,30")
print(p.nombre)
print(Persona.es_mayor_de_edad(20))

print()
print()

# Ej.3 - Atributos de Clase vs. Instancia
class Contador:
    instancias = 0  # atributo de clase

    def __init__(self):
        Contador.instancias += 1
        self.id = Contador.instancias  # atributo de instancia

# Prueba
c1 = Contador()
c2 = Contador()
print(Contador.instancias)
print(c1.id, c2.id)
print(vars(c1)) 
print(Contador.__dict__)


print()
print()


# Ej.4 - Encapsulación con Propiedades
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self._precio = precio
    
    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor

# Prueba
p = Producto("Libro", 100)
p.precio = 120
# p.precio = -5


print()
print()


# Ej.5 - __slots__ (Mención breve)
class Punto2D:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Ej.6 - Manejo de Excepciones Orientado a Objetos

class ErrorAplicacion(Exception):
    pass

class ErrorValorNegativo(ErrorAplicacion):
    pass

# Prueba
try:
    raise ErrorValorNegativo('Valor negativo no permitido')
except ErrorAplicacion as e:
    print(e)


# Caso Práctico: Clase Fracción
"""
Implementa una fraccion con numerador y denominador, usando propiedades,
métodos especiales y un constructor alternativo.
"""

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador  # Usará la propiedad

    @property
    def denominador(self):
        return self._denominador

    @denominador.setter
    def denominador(self, valor):
        if valor == 0:
            raise ValueError("El denominador no puede ser cero")
        self._denominador = valor

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __add__(self, otra):
        if not isinstance(otra, Fraccion):
            return NotImplemented
        num = self.numerador * otra.denominador + otra.numerador * self.denominador
        den = self.denominador * otra.denominador
        return Fraccion(num, den)

    @classmethod
    def desde_cadena(cls, cadena):
        partes = cadena.split("/")
        if len(partes) != 2:
            raise ValueError("Formato inválido")
        return cls(int(partes[0]), int(partes[1]))

# Prueba
f1 = Fraccion(1, 2)
f2 = Fraccion.desde_cadena("3/4")
f3 = f1 + f2
print(f3)  # 10/8




# Ejemplo procedimental
""" def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar('Juan') """

# Programación orientada a objetos
# Agreguemos Atributos
class Persona:
    # Constructor de la clase
    def __init__(self, nombre, edad):
        # Atributos de la clase
        self.nombre = nombre
        self.edad = edad
                
    def saludar(self):
        print(f"Hola, {self.nombre}, tienes {self.edad} años.")



# Instanciar un Objeto de la clase Persona
p1 = Persona('Juan', 30)
# Llamar al método saludar del objeto p1
p1.saludar()

print()

p2 = Persona('Ana', 25)
# Llamar al método saludar del objeto p2    
p2.saludar()

print()

# Ej. Modelando una Cafetera
class Cafetera:
    def __init__(self, marca, capacidad):
        self.marca = marca
        self.capacidad = capacidad
    
    def servir_cafe(self):
        print('Sirviendo café caliente ☕')


mi_cafetera = Cafetera('Oster', 1.5)
print(mi_cafetera.marca)
mi_cafetera.servir_cafe()

print()

mi_cafetera2 = Cafetera('BD', 2.0)
print(mi_cafetera2.capacidad)

print()

# Area de un Rectangulo
class Rectangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura


r = Rectangulo(4, 5)
print("Area del rectangulo:", r.area())

"""
1. ¿Qué diferencia hay entre una clase y un objeto?
2. ¿Qué función cumple `self` en los métodos?
3. ¿Por qué usar programación orientada a objetos?
4. ¿Cómo crear una instancia de una clase en Python?

Tarea que consta de tres ejercicios.
tareas se entregan: tareas@juanpageek.com
"""
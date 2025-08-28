# Módulo 5: Herencia Avanzada y Composición de Objetos

# 1. Repaso de Herencia Simple
class Animal:
    def hablar(self):
        print("El animal hace un sonido")

class Perro(Animal):
    def hablar(self):
        super().hablar()
        print("El perro ladra")

p = Perro()
p.hablar()
print()
print()

# 2. Herencia Múltiple y MRO
class A:
    def metodo(self):
        print("A.metodo")

class B:
    def metodo(self):
        print("B.metodo")

class C(B, A):
    pass

c = C()
c.metodo() #llama al método de clase A
print()
print()


# MRO (Method Resolution Order)
"""
El MRO define el orden en que Python busca métodos/atributos
en presencia de múltiples superclases. Python 3 usa el algoritmo
llamado C3 linearization.
"""

print(C.__mro__)
print()
print()


# 3. Buenos hábitos con Herencia Múltiple y Mixins
"""
- Evitar jerarquías tipo diamente complicadas.
- Usar mixins para funcionalidades adicionales.
"""
class LogginMixin:
    def log(self, mensaje):
        print(f"[Log] {mensaje}")

class Servicio(LogginMixin):
    def ejecutar(self):
        self.log("Servicio ejecutado")

s = Servicio()
s.ejecutar()
print()
print()


# 4. Composición de Objetos
"""
La composición es una alternativa a la herencia.
Un objeto contiene instancias de otras clases para reutilizar 
funcionalidad.

Ventajas de la composición:
- Reducción de acoplamiento
- Mayor flexibilidad
"""
class Motor:
    def enceder(self):
        print("Motor encendido")

class Vehiculo:
    def __init__(self):
        self.motor = Motor()

    def arrancar(self):
        self.motor.enceder()
        print("Vehiculo en marcha")


v = Vehiculo()
v.arrancar()
print()
print()


# 5. Principios de Diseño OO
"""
Alta cohesión: Cada clase debe tener una responsabilidad clara.
Bajo acomplamiento: Las clases deben ser lo más independiente posible.
"""

# 6. Ejemplo Integrador: Herencia y Composición
"""
Jerarquía de empleados donde un Gerente hereda de Empleado y
compone una lista de subordinados.
"""
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def trabajar(self):
        print(f"{self.nombre} esta trabajando.")

class Gerente(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.subordinados = []
    
    def agregar_subordinado(self, empleado):
        self.subordinados.append(empleado)
    
    def trabajar(self):
        print(f"{self.nombre} esta gestionando el equipo.")
        for e in self.subordinados:
            e.trabajar()

class Ingeniero(Empleado):
    def trabajar(self):
        print(f"{self.nombre} esta desarrollando software")

# Ejemplo de uso
juan = Ingeniero("Juan")
luis = Ingeniero("Luis")
ana = Gerente("Ana")
ana.agregar_subordinado(juan)
ana.agregar_subordinado(luis)
ana.trabajar()
print()
print()


# Resumen de nuestro módulo 5
"""
- La herencia múltiple y la composición son herramientas
poderosas para diseñar sistemas OO flexibles.
- El MRO ayuda a entender cómo Python resuelve métodos en jerarquías
complejas.
- La composición suele ser preferible para reducir acomplamiento y
aumentar la flexibilidad.
"""



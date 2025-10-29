"""
class Personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud

    def atacar(self, otro):
        pass # Implementar lógica de ataque

class Guerrero(Personaje):
    def __init__(self, nombre, salud, fuerza):
        super().__init__(nombre, salud)
        self.fuerza = fuerza

    def atacar(self, otro):
        otro.salud -= self.fuerza
        print(f"{self.nombre} ataca a {otro.nombre} causando {self.fuerza} de daño.")


class Mago(Personaje):
    def __init__ (self, nombre, salud, mana):
        super().__init__(nombre, salud)
        self.mana = mana

    def lanzar_hechizo(self, otro):
        if self.mana >= 10:
            otro.salud -= 15
            self.mana -= 10
            print(f"{self.nombre} lanza un hechizo a {otro.nombre} causando 15 de daño.")
        else:
            print(f"{self.nombre} no tiene suficiente mana para lanzar un hechizo.")

# Ejemplo de uso
guerrero = Guerrero("Aragorn", 100, 20)
mago = Mago("Gandalf", 80, 50)
guerrero.atacar(mago)
mago.lanzar_hechizo(guerrero)
"""

print()
print()

"""
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante(Persona):
    def __init__(self, nombre, notas):
        super().__init__(nombre)
        self.notas = notas
    
    def promedio(self):
        return sum(self.notas) / len(self.notas)

class Profesor(Persona):
    pass

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []
    
    def inscribir(self, estudiante):
        self.estudiantes.append(estudiante)

    def listar_estudiantes(self):
        for estudiante in self.estudiantes:
            print(f"Estudiante: {estudiante.nombre}")

# Ejemplo de uso
curso = Curso("Matemáticas")
estudiante1 = Estudiante("Ana", [90, 85, 88])
estudiante2 = Estudiante("Luis", [78, 82, 80])
curso.inscribir(estudiante1)
curso.inscribir(estudiante2)    
curso.listar_estudiantes()
"""

print()
print()


from abc import ABC, abstractmethod

class RepositorioContacto(ABC):
    @abstractmethod
    def guardar(self, contacto):
        pass

    @abstractmethod
    def cargar(self):
        pass

class AgendaArchivo(RepositorioContacto):
    def __init__(self, archivo):    
        self.archivo = archivo

    def guardar(self, contacto):
        try:
            with open(self.archivo, 'a') as f:
                f.write(contacto + '\n')
        except IOError as e:
            print(f"Error al guardar el contacto: {e}")

    def cargar(self):
        try:
            with open(self.archivo, 'r') as f:
                return f.readlines()
        except IOError as e:
            print(f"Error al cargar los contactos: {e}")
            return []   


# Ejemplo de uso
agenda = AgendaArchivo('contactos.txt')
agenda.guardar('Juan Perez, 588-1444')
contactos = agenda.cargar()
print(contactos)


print()
print()

class Personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud
    
    @classmethod
    def personaje_predeterminado(cls):
        return cls("Personaje Generico", 100)
    
    @staticmethod
    def calcular_dano(base, multiplicador):
        return base * multiplicador

# Ejemplo de uso
personaje = Personaje.personaje_predeterminado()
print(f"Nombre: {personaje.nombre}, Salud: {personaje.salud}")

dano = Personaje.calcular_dano(10, 2)
print(f"Daño calculado: {dano}")


print()
print()

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []
    
    @classmethod
    def curso_predeterminado(cls):
        curso = cls("Curso Predeterminado")
        curso.estudiantes.append("Estudiante Generico")
        return curso
    
    @staticmethod
    def es_nota_valida(nota):
        return 0 <= nota <= 100

# Ejemplo de uso
curso = Curso.curso_predeterminado()
print(f"Nombre del curso: {curso.nombre}, Estudiantes: {curso.estudiantes}")

print(Curso.es_nota_valida(85))  # True
print(Curso.es_nota_valida(150)) # False
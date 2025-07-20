import json
import os
from contacto import Contacto

class AgendaContactos:
    """
    Clase que gestiona una colección de contactos.

    Attributes:
        contactos (list): Lista de objetos Contacto
        ruta_archivo (str): Ruta al archivo de almacenamiento
    """
    def __init__(self, ruta_archivo="contactos.json"):
        """
        Inicializa una nueva agenda de contactos.
        Args:
            ruta_archivo (str, optional): Rutal al archivo para guardar los contactos
        """
        self.contactos = []
        self.ruta_archivo = ruta_archivo
        # Intentar cargar contactos existentes si el archivo existe
        self.cargar()

    def agregar(self, contacto):
        """
        Añade un nuevo contacto a la agenda.
        Args:
             contacto (Contacto): El contacto a añadir
        Returns:
            bool: True si se agregó correctamente,
                  False si ya existe
        """
        # Verificar si ya existe un contacto con el mismo nombre
        for c in self.contactos:
            if c.nombre.lower() == contacto.nombre.lower():
                return False

        # Si no existe, lo añadimos
        self.contactos.append(contacto)
        return True

    def buscar(self, termino):
        """
        Busca contactos que coincidan con el término de búsqueda.
        Args:
            termino (str): Término a buscar en nombre, teléfono o email
        Returns:
            list: Lista de contactos que coinciden con la búsqueda.
        """
        resultados = []
        termino = termino.lower()

        for contacto in self.contactos:
            if (termino in contacto.nombre.lower() or
                termino in contacto.telefono.lower() or
                termino in contacto.email.lower()):
                resultados.append(contacto)

        return resultados

    def actualizar(self, nombre_actual, nombre=None, telefono=None, email=None, direccion=None):
        """
        Actualiza un contacto existente.
        Args:
            nombre_actual (str): Nombre del contacto a actualizar
            nombre (str, optional): Nuevo nombre
            telefono (str, optional): Nuevo teléfono
            email (str, optional): Nuevo email
            direccion (str, optional): Nueva dirección
        """
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre_actual.lower():
                contacto.actualizar(nombre, telefono, email, direccion)
                return True
        return False

    def eliminar(self, nombre):
        """
        Elimina un contacto de la agenfa.
        Args:
            nombre (str): Nombre del contacto a eliminar
        Returns:
            bool: True si se elimina correctamente, False si no se encontró
        """
        for i, contacto in enumerate(self.contactos):
            if contacto.nombre.lower() == nombre.lower():
                del self.contactos[i]
                return True
        return False

    def listar(self):
        """
        Devuelve la lista completa de contactos.
        Returns:
            list: Lista de todos los contactos
        """
        return self.contactos

    def guardar(self):
        """
        bool: True si se guardó correctamente
              False en caso contrario
        """
        try:
            # Convertir objetos Contacto a diccionarios
            datos = []
            for contacto in self.contactos:
                datos.append({
                    "nombre": contacto.nombre,
                    "telefono": contacto.telefono,
                    "email": contacto.email,
                    "direccion": contacto.direccion
                })

            # Guardar en formato JSON
            with open(self.ruta_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error al guardar: {e}")
            return False

    def cargar(self):
            """
            Carga los contactos desde un archivo JSON.
            Returns:
                bool: True si se cargó correctamente,
                      False en caso contrario
            """
            if not os.path.exists(self.ruta_archivo):
                return  False

            try:
                with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
                    datos = json.load(archivo)

                # Convertir diccionarios a objetos Contacto
                self.contactos = []
                for dato in datos:
                    contacto = Contacto(
                        dato["nombre"],
                        dato["telefono"],
                        dato.get("email", ""),
                        dato.ger("direccion", "")
                    )
                    self.contactos.append(contacto)
                return True
            except Exception as e:
                print(f'Error al cargar: {e}')
                return False

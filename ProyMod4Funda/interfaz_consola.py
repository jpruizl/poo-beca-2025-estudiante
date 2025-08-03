from agenda_contactos import AgendaContactos
from contacto import Contacto


class InterfazConsola:
    """
    Clase que maneja la interacción con el usuario a través de la consola.

    Attributes:
        agenda (AgendaContactos): La agenda de contactos que se manipulará
    """

    def __init__(self):
        """Inicializa la interfaz con una nueva agenda de contactos."""
        self.agenda = AgendaContactos()

    def mostrar_menu(self):
        """Muestra el menú principal de la aplicación."""
        print("\n===== AGENDA DE CONTACTOS =====")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Listar todos los contactos")
        print("6. Guardar cambios")
        print("0. Salir")
        print("==============================")

    def ejecutar(self):
        """Ejecuta el bucle principal de la interfaz."""
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_contacto()
            elif opcion == "2":
                self.buscar_contacto()
            elif opcion == "3":
                self.actualizar_contacto()
            elif opcion == "4":
                self.eliminar_contacto()
            elif opcion == "5":
                self.listar_contactos()
            elif opcion == "6":
                self.guardar_cambios()
            elif opcion == "0":
                # Preguntar si quiere guardar antes de salir
                if input("¿Desea guardar los cambios antes de salir? (s/n): ").lower() == 's':
                    self.guardar_cambios()
                print("¡Hasta pronto!")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def agregar_contacto(self):
        """Solicita datos al usuario y agrega un nuevo contacto."""
        print("\n--- Agregar nuevo contacto ---")
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email (opcional): ")
        direccion = input("Dirección (opcional): ")

        nuevo_contacto = Contacto(nombre, telefono, email, direccion)

        if self.agenda.agregar(nuevo_contacto):
            print(f"✓ Contacto '{nombre}' agregado correctamente.")
        else:
            print(f"✗ Ya existe un contacto con el nombre '{nombre}'.")

    def buscar_contacto(self):
        """Busca y muestra contactos según el término de búsqueda."""
        print("\n--- Buscar contacto ---")
        termino = input("Introduzca nombre, teléfono o email: ")

        resultados = self.agenda.buscar(termino)

        if resultados:
            print(f"\nSe encontraron {len(resultados)} contactos:")
            for i, contacto in enumerate(resultados, 1):
                print(f"\n--- Contacto {i} ---")
                print(contacto)
        else:
            print("No se encontraron contactos con ese término.")

    def actualizar_contacto(self):
        """Actualiza la información de un contacto existente."""
        print("\n--- Actualizar contacto ---")
        nombre = input("Nombre del contacto a actualizar: ")

        # Buscar si existe el contacto
        resultados = self.agenda.buscar(nombre)
        contacto_encontrado = None

        for contacto in resultados:
            if contacto.nombre.lower() == nombre.lower():
                contacto_encontrado = contacto
                break

        if contacto_encontrado:
            print(f"\nContacto encontrado:\n{contacto_encontrado}")
            print("\nIntroduzca los nuevos datos (deje en blanco para mantener el valor actual):")

            nuevo_nombre = input(f"Nuevo nombre [{contacto_encontrado.nombre}]: ")
            nuevo_telefono = input(f"Nuevo teléfono [{contacto_encontrado.telefono}]: ")
            nuevo_email = input(f"Nuevo email [{contacto_encontrado.email}]: ")
            nueva_direccion = input(f"Nueva dirección [{contacto_encontrado.direccion}]: ")

            # Si se dejó en blanco, mantener el valor actual
            nuevo_nombre = None if nuevo_nombre == "" else nuevo_nombre
            nuevo_telefono = None if nuevo_telefono == "" else nuevo_telefono
            nuevo_email = None if nuevo_email == "" else nuevo_email
            nueva_direccion = None if nueva_direccion == "" else nueva_direccion

            if self.agenda.actualizar(contacto_encontrado.nombre, nuevo_nombre,
                                      nuevo_telefono, nuevo_email, nueva_direccion):
                print("✓ Contacto actualizado correctamente.")
            else:
                print("✗ No se pudo actualizar el contacto.")
        else:
            print(f"✗ No se encontró un contacto con el nombre '{nombre}'.")

    def eliminar_contacto(self):
        """Elimina un contacto existente."""
        print("\n--- Eliminar contacto ---")
        nombre = input("Nombre del contacto a eliminar: ")

        if self.agenda.eliminar(nombre):
            print(f"✓ Contacto '{nombre}' eliminado correctamente.")
        else:
            print(f"✗ No se encontró un contacto con el nombre '{nombre}'.")

    def listar_contactos(self):
        """Muestra todos los contactos de la agenda."""
        print("\n--- Lista de contactos ---")
        contactos = self.agenda.listar()

        if contactos:
            for i, contacto in enumerate(contactos, 1):
                print(f"\n--- Contacto {i} ---")
                print(contacto)
            print(f"\nTotal: {len(contactos)} contactos")
        else:
            print("La agenda está vacía.")

    def guardar_cambios(self):
        """Guarda los cambios en el archivo."""
        if self.agenda.guardar():
            print("✓ Cambios guardados correctamente.")
        else:
            print("✗ Error al guardar los cambios.")
from interfaz_consola import InterfazConsola

def main():
    """Función principal que inicia la aplicación."""
    print("Bienvenido al Sistema de Administración de Contactos")
    app = InterfazConsola()
    app.ejecutar()

if __name__ == "__main__":
    main()
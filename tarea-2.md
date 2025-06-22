# Tarea: Fundamentos de la Programación Orientada a Objetos (POO)

## Introducción

¡Hola, futuros ingenieros de software!

En esta tarea, exploraremos los cuatro pilares fundamentales de la Programación Orientada a Objetos (POO): Abstracción, Encapsulamiento, Herencia y Polimorfismo. Comprender y aplicar estos conceptos es crucial para escribir código modular, reutilizable y fácil de mantener.

El objetivo es que implementes soluciones que demuestren tu comprensión de cada pilar. Puedes usar el lenguaje de programación de tu elección (Java, Python, C#, C++, etc.), pero asegúrate de que el código sea claro y esté bien comentado.

## Los Cuatro Pilares de la POO

Antes de empezar con los ejercicios, recordemos brevemente cada pilar:

1.  **Abstracción**: Se enfoca en mostrar solo la información esencial y ocultar los detalles de implementación complejos. Permite definir la "qué" hace un objeto sin preocuparse por el "cómo".
2.  **Encapsulamiento**: Es el mecanismo de agrupar datos (atributos) y los métodos (funciones) que operan sobre esos datos dentro de una única unidad (clase). También implica restringir el acceso directo a algunos de los componentes de un objeto, protegiendo así la integridad de los datos.
3.  **Herencia**: Permite que una clase (clase hija o subclase) herede propiedades y comportamientos de otra clase (clase padre o superclase). Esto promueve la reutilización de código y establece una relación "es un" (e.g., un `Perro` *es un* `Animal`).
4.  **Polimorfismo**: Significa "muchas formas". Permite que objetos de diferentes clases respondan a la misma llamada de método de maneras distintas, siempre y cuando compartan una interfaz común o una superclase. Esto se logra a menudo a través de la sobreescritura de métodos (method overriding) o interfaces.

## Ejercicios

### Ejercicio 1: El Reino Animal

**Objetivo**: Demostrar Abstracción, Encapsulamiento y Herencia.

Imagina que estás construyendo un sistema para gestionar diferentes tipos de animales en un zoológico virtual.

**Instrucciones**:

1.  **Clase Base `Animal`**:
    *   Crea una clase base llamada `Animal`.
    *   Esta clase debe tener atributos privados como `nombre` (String) y `edad` (int).
    *   Implementa un constructor para inicializar estos atributos.
    *   Aplica **Encapsulamiento** proporcionando métodos públicos `getNombre()`, `getEdad()`, `setNombre()`, `setEdad()`.
    *   Define un método abstracto `hacerSonido()` (o un método virtual que pueda ser sobreescrito) que no tome argumentos y no devuelva nada. Este método representará el sonido característico de cada animal.
    *   Define un método concreto `comer()` que imprima un mensaje genérico como "El animal está comiendo.".

2.  **Clases Derivadas `Perro` y `Gato`**:
    *   Crea dos clases, `Perro` y `Gato`, que **hereden** de la clase `Animal`.
    *   Cada clase debe tener un constructor que llame al constructor de la clase base.
    *   **Sobreescribe** el método `hacerSonido()` en cada clase para que imprima el sonido específico del animal (e.g., "Guau guau!" para `Perro`, "Miau miau!" para `Gato`).

3.  **Clase de Prueba (`Main` o similar)**:
    *   En tu método principal, crea instancias de `Perro` y `Gato`.
    *   Llama a los métodos `getNombre()`, `getEdad()`, `comer()` y `hacerSonido()` para cada instancia.
    *   Demuestra cómo puedes tratar a un `Perro` o un `Gato` como un `Animal` (por ejemplo, en una lista de `Animales`) y llamar a `hacerSonido()` para observar el comportamiento polimórfico (aunque el polimorfismo se verá más a fondo en el Ejercicio 2, aquí ya se empieza a vislumbrar).

### Ejercicio 2: Calculadora de Formas Geométricas

**Objetivo**: Demostrar Abstracción y Polimorfismo.

Vas a construir una aplicación que calcule el área y el perímetro de diferentes formas geométricas.

**Instrucciones**:

1.  **Clase Abstracta `Forma`**:
    *   Crea una clase abstracta llamada `Forma`.
    *   Esta clase debe tener un método abstracto `calcularArea()` que devuelva un `double`.
    *   Esta clase debe tener un método abstracto `calcularPerimetro()` que devuelva un `double`.
    *   (Opcional) Puedes añadir un atributo `nombre` para la forma y su encapsulamiento.

2.  **Clases Concretas `Circulo` y `Rectangulo`**:
    *   Crea dos clases, `Circulo` y `Rectangulo`, que **hereden** de la clase `Forma`.
    *   `Circulo` debe tener un atributo para el `radio`.
    *   `Rectangulo` debe tener atributos para `ancho` y `alto`.
    *   Implementa los constructores para inicializar sus atributos.
    *   **Sobreescribe** los métodos `calcularArea()` y `calcularPerimetro()` en cada clase con la lógica específica para esa forma.
        *   Para `Circulo`: Área = π * radio², Perímetro = 2 * π * radio.
        *   Para `Rectangulo`: Área = ancho * alto, Perímetro = 2 * (ancho + alto).

3.  **Clase de Prueba (`Main` o similar)**:
    *   Crea una lista (o array) de objetos de tipo `Forma`.
    *   Añade instancias de `Circulo` y `Rectangulo` a esta lista.
    *   Itera sobre la lista y, para cada `Forma`, llama a `calcularArea()` y `calcularPerimetro()`.
    *   Observa cómo, a pesar de que todas las llamadas se hacen a través de una referencia de tipo `Forma`, el método correcto (específico de `Circulo` o `Rectangulo`) es invocado. Esto es el **Polimorfismo** en acción.
    *   Imprime los resultados de área y perímetro para cada forma.

## Entrega

*   Tu código fuente bien organizado en archivos separados por clase.
*   Un archivo README.md (o similar) explicando brevemente cómo compilar y ejecutar tu solución, y cualquier consideración especial.
*   Asegúrate de que tu código esté bien comentado y siga buenas prácticas de programación.

¡Mucha suerte y a programar!
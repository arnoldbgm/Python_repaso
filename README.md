
### **Ejercicio 1: Variables y Tipos de Datos**
**Historia:** Eres un desarrollador que está creando un sistema para gestionar la información de los empleados de una empresa.

**Tarea:**
1. Define una variable `nombre` con el nombre del empleado.
2. Define una variable `edad` con la edad del empleado.
3. Define una variable `salario` con el salario mensual del empleado.
4. Imprime un mensaje que incluya todas las variables anteriores. En terminal debe salir

```shell
Empleado: Juan, Edad: 33, Salario: 5000
```
---

### **Ejercicio 2: Estructuras de Control**
**Historia:** Eres un programador que está desarrollando una aplicación para una tienda en línea. Necesitas implementar una función para aplicar descuentos según la cantidad de productos comprados.

**Tarea:**
1. Pide al usuario que ingrese el monto de los productos comprados.
2. Si la monto es mayor o igual a 100, aplica un descuento del 20%.
3. Si la monto es mayor o igual a 50, aplica un descuento del 10%.
4. Si la monto es menor a 5, no aplica ningún descuento.
5. Imprime solo que porcentaje se le debe de descontar.

```shell
EJEMPLO
Bienvenido a mi sistema ¿Cuanto es el monto de su compra?   80
Le corresponde un descuento de 10%
```

---

### **Ejercicio 3: Funciones**
**Historia:** Eres un profesor que quiere automatizar el cálculo de las notas finales de tus estudiantes. Necesitas crear una función que calcule el promedio de una lista de notas.

**Tarea:**
1. Define una función `calcular_promedio` que reciba una lista de notas y retorne el promedio.
2. Llama a la función con una lista de notas y muestra el promedio.

```python
def calcular_promedio(notas):
    # Aqui debes de colocar el codigo que calcule el promedio
    pass

notas_alumno = [85, 90, 78, 92, 88]
promedio = calcular_promedio(notas_alumno)
print(f"El promedio del alumno es: {promedio}")
```

---

### **Ejercicio 4: Listas**
**Historia:** Eres un administrador de un supermercado que necesita gestionar el inventario de productos.

**Tarea:**
1. Crea una lista llamada `inventario` con algunos productos.
2. Añade un nuevo producto al final de la lista.
3. Elimina un producto de la lista.
4. Busca un producto en la lista e imprime su índice.

```python
# Este es tu inventario con el realiza todo las acciones solicitadas
inventario = ["manzanas", "bananas", "naranjas"]
```

---

### **Ejercicio 5: Diccionarios**
**Historia:** Eres un desarrollador que está creando un sistema para gestionar la información de los estudiantes en una escuela.

**Tarea:**
1. Crea un diccionario llamado `estudiante` con claves `nombre`, `edad`, y `curso`.
2. Añade una clave `nota_final` con un valor.
3. Elimina la clave `edad`.
4. Imprime en pantalla el `nombre` del estudiante.

```python
estudiante = {"nombre": "Lucía", "edad": 20, "curso": "Historia"}
```

### **Ejercicio 6: Bucles**
**Historia:** Eres un desarrollador que está creando una aplicación para gestionar las tareas de los empleados en una empresa.

**Tarea 1:**
1. Crea una lista de tareas llamada `tareas` con algunas tareas iniciales.
2. Usa un bucle `for` para imprimir cada tarea en la lista.

```python
tareas = ["Revisar correos", "Hacer llamadas", "Preparar informe"]
for tarea in tareas:
    print(tarea)
```


---


### **Ejercicio 6: Programación Orientada a Objetos (POO)**
**Historia:** Eres un desarrollador que está creando un sistema para gestionar una flota de vehículos en una empresa de alquiler de coches.

**Tarea:**
1. Define una clase `Coche` con atributos `marca`, `modelo`, y `año`.
2. Define un método `descripcion` que imprima una descripción del coche.
3. Crea una instancia de `Coche` y llama al método `descripcion`.

```python
# Completa lo que falta, SUERTE 👏
class Coche:
   #Este es tu constructor
    def __init__(self, marca, modelo, año):
   #Este es tu metodo
    def descripcion(self):

```

---

### **Ejercicio 7: Herencia**
**Historia:** Eres un desarrollador que está creando un sistema para gestionar animales en un zoológico. Necesitas implementar herencia para los diferentes tipos de animales.

**Tarea:**
1. Define una clase base `Animal` con un método `hacer_sonido`.
2. Define una clase derivada `Perro` que herede de `Animal` y sobrescriba el método `hacer_sonido`.
3. Crea una instancia de `Perro` y llama al método `hacer_sonido`.

---

### **Ejercicio 8: Ejercicio de Repaso General**
**Historia:** Eres un desarrollador que está creando un sistema para gestionar una biblioteca.

**Tarea:**
1. Define una clase `Libro` con atributos `titulo`, `autor`, y `año`.
2. Define una clase `Biblioteca` con una `lista` de libros.
3. Implementa métodos en `Biblioteca` mostrar todos los libros.

```python
class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

class Biblioteca:
    def __init__(self):
        self.libros = []

    def añadir_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        for libro in self.libros:
            print(f"{libro.titulo} por {libro.autor} ({libro.año})")

libro1 = Libro("El Quijote", "Miguel de Cervantes", 1605)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
mi_biblioteca = Biblioteca()
mi_biblioteca.añadir_libro(libro1)
mi_biblioteca.añadir_libro(libro2)
mi_biblioteca.mostrar_libros()
```
---


Claro, aquí tienes una guía detallada sobre cómo configurar un entorno virtual y ejecutar las pruebas.

## Cómo Ejecutar las Pruebas

### 1. Crear un Entorno Virtual

Un entorno virtual permite gestionar las dependencias del proyecto sin interferir con otras configuraciones de Python en tu sistema.

1. **Navega al Directorio del Proyecto**:
   Abre la terminal o el símbolo del sistema y cambia al directorio de tu proyecto. Por ejemplo:

   ```bash
   cd ruta/a/tu/proyecto
   ```

2. **Crear el Entorno Virtual**:
   Usa el siguiente comando para crear un entorno virtual llamado `venv`:

   ```bash
   python -m venv venv
   ```

   Esto creará un directorio `venv` en tu proyecto que contendrá el entorno virtual.

3. **Activar el Entorno Virtual**:
   - **En Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - **En macOS y Linux**:

     ```bash
     source venv/bin/activate
     ```

   Después de activar el entorno, deberías ver el nombre del entorno virtual en el prompt de la terminal.

### 2. Instalar Dependencias

Con el entorno virtual activado, instala `pytest`, que es la herramienta utilizada para ejecutar las pruebas.

```bash
pip install pytest
```

### 3. Ejecutar las Pruebas

Para ejecutar todas las pruebas en tu proyecto, utiliza el siguiente comando:

```bash
pytest -v
```

Este comando ejecutará todas las pruebas en los archivos que comienzan con `test_` y mostrará un informe detallado de los resultados. La opción `-v` habilita el modo detallado, mostrando más información sobre cada prueba.

### 4. Revisar Resultados

Después de ejecutar las pruebas, verás un informe que indica si cada prueba pasó o falló. El resultado se verá algo así:

```
============================= test session starts ==============================
platform win32 -- Python 3.12.4, pytest-8.3.1, pluggy-1.5.0
rootdir: D:\Programacion\Codigo_Tecsup\Backend\G-20\Python\Ejercicios
collected 2 items

test_ejercicio_1.py ....                                                   [ 50%]
test_ejercicio_2.py ....                                                   [ 100%]

============================== 2 passed in 0.12s ===============================
```

En el informe, `.` indica que una prueba pasó, mientras que `F` indicaría una prueba fallida.
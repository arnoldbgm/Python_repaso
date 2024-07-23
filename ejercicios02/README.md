Claro, aquí tienes los ejercicios con la historia, pero sin la solución:

---

### Ejercicio 1: Filtrar Adultos
**Historia**: En una base de datos de empleados, se necesita extraer todos los empleados que son mayores de 18 años.

```python
# Datos
empleados = [
    {"nombre": "Ana", "apellido": "Gómez", "edad": 24, "estado_civil": "soltero", "genero": "femenino"},
    {"nombre": "Luis", "apellido": "Martínez", "edad": 17, "estado_civil": "soltero", "genero": "masculino"},
    {"nombre": "Sofía", "apellido": "Sánchez", "edad": 30, "estado_civil": "casado", "genero": "femenino"},
    {"nombre": "Pedro", "apellido": "Fernández", "edad": 22, "estado_civil": "soltero", "genero": "masculino"}
]

# Solución esperada
```

**Salida Esperada**:
```
{'nombre': 'Ana', 'apellido': 'Gómez', 'edad': 24, 'estado_civil': 'soltero', 'genero': 'femenino'}
{'nombre': 'Sofía', 'apellido': 'Sánchez', 'edad': 30, 'estado_civil': 'casado', 'genero': 'femenino'}
{'nombre': 'Pedro', 'apellido': 'Fernández', 'edad': 22, 'estado_civil': 'soltero', 'genero': 'masculino'}
```

---

### Ejercicio 2: Filtrar Menores de Edad
**Historia**: En una base de datos escolar, se necesita obtener la lista de estudiantes que son menores de 18 años.

```python
# Datos
estudiantes = [
    {"nombre": "Carlos", "apellido": "Ramos", "edad": 19, "estado_civil": "soltero", "genero": "masculino"},
    {"nombre": "Lucía", "apellido": "Hernández", "edad": 17, "estado_civil": "soltero", "genero": "femenino"},
    {"nombre": "Miguel", "apellido": "Fernández", "edad": 22, "estado_civil": "casado", "genero": "masculino"},
    {"nombre": "Elena", "apellido": "García", "edad": 15, "estado_civil": "soltero", "genero": "femenino"}
]

# Solución esperada
```

**Salida Esperada**:
```
{'nombre': 'Lucía', 'apellido': 'Hernández', 'edad': 17, 'estado_civil': 'soltero', 'genero': 'femenino'}
{'nombre': 'Elena', 'apellido': 'García', 'edad': 15, 'estado_civil': 'soltero', 'genero': 'femenino'}
```

---

### Ejercicio 3: Filtrar Casados
**Historia**: En una base de datos de usuarios, se necesita obtener la lista de personas que están casadas.

```python
# Datos
usuarios = [
    {"nombre": "Marta", "apellido": "González", "edad": 28, "estado_civil": "casado", "genero": "femenino"},
    {"nombre": "Ricardo", "apellido": "Martínez", "edad": 35, "estado_civil": "casado", "genero": "masculino"},
    {"nombre": "Jorge", "apellido": "Díaz", "edad": 20, "estado_civil": "soltero", "genero": "masculino"},
    {"nombre": "Paula", "apellido": "Ramírez", "edad": 25, "estado_civil": "soltero", "genero": "femenino"}
]

# Solución esperada
```

**Salida Esperada**:
```
{'nombre': 'Marta', 'apellido': 'González', 'edad': 28, 'estado_civil': 'casado', 'genero': 'femenino'}
{'nombre': 'Ricardo', 'apellido': 'Martínez', 'edad': 35, 'estado_civil': 'casado', 'genero': 'masculino'}
```

---

### Ejercicio 4: Filtrar por Género
**Historia**: En una encuesta de empleo, se necesita listar todos los candidatos de género masculino.

```python
# Datos
candidatos = [
    {"nombre": "Mario", "apellido": "Álvarez", "edad": 32, "estado_civil": "soltero", "genero": "masculino"},
    {"nombre": "Sofía", "apellido": "García", "edad": 28, "estado_civil": "casado", "genero": "femenino"},
    {"nombre": "Andrés", "apellido": "Morales", "edad": 26, "estado_civil": "soltero", "genero": "masculino"},
    {"nombre": "Ana", "apellido": "Torres", "edad": 30, "estado_civil": "casado", "genero": "femenino"}
]

# Solución esperada
```

**Salida Esperada**:
```
{'nombre': 'Mario', 'apellido': 'Álvarez', 'edad': 32, 'estado_civil': 'soltero', 'genero': 'masculino'}
{'nombre': 'Andrés', 'apellido': 'Morales', 'edad': 26, 'estado_civil': 'soltero', 'genero': 'masculino'}
```

---

### Ejercicio 5: Filtrar Solteros Jóvenes
**Historia**: En una base de datos de clientes, se necesita obtener los clientes solteros menores de 20 años.

```python
# Datos
clientes = [
    {"nombre": "Luis", "apellido": "Ramírez", "edad": 19, "estado_civil": "soltero", "genero": "masculino"},
    {"nombre": "Laura", "apellido": "Martínez", "edad": 16, "estado_civil": "soltero", "genero": "femenino"},
    {"nombre": "Javier", "apellido": "Moreno", "edad": 22, "estado_civil": "soltero", "genero": "masculino"},
    {"nombre": "María", "apellido": "Fernández", "edad": 18, "estado_civil": "casado", "genero": "femenino"}
]

# Solución esperada
```

**Salida Esperada**:
```
{'nombre': 'Luis', 'apellido': 'Ramírez', 'edad': 19, 'estado_civil': 'soltero', 'genero': 'masculino'}
{'nombre': 'Laura', 'apellido': 'Martínez', 'edad': 16, 'estado_civil': 'soltero', 'genero': 'femenino'}
```

---

### Ejercicio 6: Contar Personas por Estado Civil
**Historia**: En una organización, se necesita contar cuántas personas hay en cada estado civil para realizar un estudio demográfico.

```python
# Datos
personas = [
    {"nombre": "Juan", "apellido": "Pérez", "edad": 25, "estado_civil": "soltero", "genero": "masculino"},
    {"nombre": "María", "apellido": "Gómez", "edad": 30, "estado_civil": "casado", "genero": "femenino"},
    {"nombre": "Pedro", "apellido": "Sánchez", "edad": 17, "estado_civil": "soltero", "genero": "masculino"},
    {"nombre": "Ana", "apellido": "López", "edad": 22, "estado_civil": "casado", "genero": "femenino"},
    {"nombre": "Laura", "apellido": "Martínez", "edad": 16, "estado_civil": "soltero", "genero": "femenino"}
]

# Solución esperada
```

**Salida Esperada**:
```
{'soltero': 3, 'casado': 2}
```

---

### Ejercicio 7: Agrupar Personas por Género
**Historia**: En una encuesta, se quiere agrupar a las personas por género para realizar análisis estadísticos.

```python
# Datos
personas = [
    {"nombre": "Juan", "apellido": "Pérez", "edad": 25, "estado_civil": "soltero", "genero": "masculino"},
    {"nombre": "María", "apellido": "Gómez", "edad": 30, "estado_civil": "casado", "genero": "femenino"},
    {"nombre": "Pedro", "apellido": "Sánchez", "edad": 17, "estado_civil": "soltero", "genero": "masculino"},
    {"nombre": "Ana", "apellido": "López", "edad": 22, "estado_civil": "casado", "genero": "femenino"},
    {"nombre": "Laura", "apellido": "Martínez",

 "edad": 16, "estado_civil": "soltero", "genero": "femenino"}
]

# Solución esperada
```

**Salida Esperada**:
```
{'masculino': [{'nombre': 'Juan', 'apellido': 'Pérez', 'edad': 25, 'estado_civil': 'soltero', 'genero': 'masculino'}, {'nombre': 'Pedro', 'apellido': 'Sánchez', 'edad': 17, 'estado_civil': 'soltero', 'genero': 'masculino'}],
 'femenino': [{'nombre': 'María', 'apellido': 'Gómez', 'edad': 30, 'estado_civil': 'casado', 'genero': 'femenino'}, {'nombre': 'Ana', 'apellido': 'López', 'edad': 22, 'estado_civil': 'casado', 'genero': 'femenino'}, {'nombre': 'Laura', 'apellido': 'Martínez', 'edad': 16, 'estado_civil': 'soltero', 'genero': 'femenino'}]}
```

---

### Ejercicio 8: Filtrar Personas Mayores de Edad Solteras
**Historia**: Un servicio de seguros desea filtrar a los clientes que son solteros y mayores de 30 años para una oferta especial.

```python
# Datos
clientes = [
    {"nombre": "Luis", "apellido": "Ramírez", "edad": 34, "estado_civil": "soltero", "genero": "masculino"},
    {"nombre": "Ana", "apellido": "Torres", "edad": 28, "estado_civil": "casado", "genero": "femenino"},
    {"nombre": "Pedro", "apellido": "Moreno", "edad": 40, "estado_civil": "soltero", "genero": "masculino"},
    {"nombre": "Clara", "apellido": "García", "edad": 31, "estado_civil": "soltero", "genero": "femenino"}
]

# Solución esperada
```

**Salida Esperada**:
```
{'nombre': 'Luis', 'apellido': 'Ramírez', 'edad': 34, 'estado_civil': 'soltero', 'genero': 'masculino'}
{'nombre': 'Pedro', 'apellido': 'Moreno', 'edad': 40, 'estado_civil': 'soltero', 'genero': 'masculino'}
{'nombre': 'Clara', 'apellido': 'García', 'edad': 31, 'estado_civil': 'soltero', 'genero': 'femenino'}
```

---

### Ejercicio 9: Filtrar Menores de Edad y Casados
**Historia**: Una empresa está realizando una revisión y necesita obtener la lista de empleados que son menores de edad y están casados (aunque no es común, es para un caso especial).

```python
# Datos
empleados = [
    {"nombre": "Carlos", "apellido": "López", "edad": 17, "estado_civil": "casado", "genero": "masculino"},
    {"nombre": "María", "apellido": "Rodríguez", "edad": 22, "estado_civil": "soltero", "genero": "femenino"},
    {"nombre": "Laura", "apellido": "Jiménez", "edad": 16, "estado_civil": "casado", "genero": "femenino"},
    {"nombre": "Ricardo", "apellido": "García", "edad": 20, "estado_civil": "soltero", "genero": "masculino"}
]

# Solución esperada
```

**Salida Esperada**:
```
{'nombre': 'Carlos', 'apellido': 'López', 'edad': 17, 'estado_civil': 'casado', 'genero': 'masculino'}
{'nombre': 'Laura', 'apellido': 'Jiménez', 'edad': 16, 'estado_civil': 'casado', 'genero': 'femenino'}
```

---

### Ejercicio 10: Eliminar Menores de Edad
**Historia**: Una aplicación para eventos necesita eliminar de su lista de invitados a todas las personas menores de edad.

```python
# Datos
invitados = [
    {"nombre": "Miguel", "apellido": "Díaz", "edad": 25, "estado_civil": "soltero", "genero": "masculino"},
    {"nombre": "Sara", "apellido": "Pérez", "edad": 14, "estado_civil": "soltero", "genero": "femenino"},
    {"nombre": "Luis", "apellido": "Vázquez", "edad": 30, "estado_civil": "casado", "genero": "masculino"},
    {"nombre": "Lucía", "apellido": "Fernández", "edad": 17, "estado_civil": "soltero", "genero": "femenino"}
]

# Solución esperada
```

**Salida Esperada**:
```
{'nombre': 'Miguel', 'apellido': 'Díaz', 'edad': 25, 'estado_civil': 'soltero', 'genero': 'masculino'}
{'nombre': 'Luis', 'apellido': 'Vázquez', 'edad': 30, 'estado_civil': 'casado', 'genero': 'masculino'}
```

---

### Ejercicio 11: Listar Nombres y Apellidos de Casados
**Historia**: Un sitio de encuentros en línea quiere enviar un correo electrónico a todas las personas casadas. Necesitan listar solo los nombres y apellidos.

```python
# Datos
personas = [
    {"nombre": "Juan", "apellido": "Pérez", "edad": 25, "estado_civil": "soltero", "genero": "masculino"},
    {"nombre": "María", "apellido": "Gómez", "edad": 30, "estado_civil": "casado", "genero": "femenino"},
    {"nombre": "Pedro", "apellido": "Sánchez", "edad": 17, "estado_civil": "soltero", "genero": "masculino"},
    {"nombre": "Ana", "apellido": "López", "edad": 22, "estado_civil": "casado", "genero": "femenino"},
    {"nombre": "Laura", "apellido": "Martínez", "edad": 16, "estado_civil": "soltero", "genero": "femenino"}
]

# Solución esperada
```

**Salida Esperada**:
```
{'nombre': 'María', 'apellido': 'Gómez'}
{'nombre': 'Ana', 'apellido': 'López'}
```

---

### Ejercicio 12: Ordenar por Edad
**Historia**: En una plataforma de análisis de datos, se necesita ordenar a las personas por edad de manera ascendente para preparar un informe.

```python
# Datos
personas = [
    {"nombre": "Juan", "apellido": "Pérez", "edad": 25, "estado_civil": "soltero", "genero": "masculino"},
    {"nombre": "María", "apellido": "Gómez", "edad": 30, "estado_civil": "casado", "genero": "femenino"},
    {"nombre": "Pedro", "apellido": "Sánchez", "edad": 17, "estado_civil": "soltero", "genero": "masculino"},
    {"nombre": "Ana", "apellido": "López", "edad": 22, "estado_civil": "casado", "genero": "femenino"},
    {"nombre": "Laura", "apellido": "Martínez", "edad": 16, "estado_civil": "soltero", "genero": "femenino"}
]

# Solución esperada
```

**Salida Esperada**:
```
{'nombre': 'Laura', 'apellido': 'Martínez', 'edad': 16, 'estado_civil': 'soltero', 'genero': 'femenino'}
{'nombre': 'Pedro', 'apellido': 'Sánchez', 'edad': 17, 'estado_civil': 'soltero', 'genero': 'masculino'}
{'nombre': 'Ana', 'apellido': 'López', 'edad': 22, 'estado_civil': 'casado', 'genero': 'femenino'}
{'nombre': 'Juan', 'apellido': 'Pérez', 'edad': 25, 'estado_civil': 'soltero', 'genero': 'masculino'}
{'nombre': 'María', 'apellido': 'Gómez', 'edad': 30, 'estado_civil': 'casado', 'genero': 'femenino'}
```

---

### Ejercicio 13: Contar Número de Mujeres Casadas
**Historia**: Un centro de apoyo familiar necesita saber cuántas mujeres casadas hay en su base de datos para un programa de ayuda.

```python
# Datos
personas = [
    {"nombre": "Juan", "apellido": "Pérez", "edad": 25, "estado_civil": "soltero", "genero": "masculino"},
    {"nombre": "María

", "apellido": "Gómez", "edad": 30, "estado_civil": "casado", "genero": "femenino"},
    {"nombre": "Pedro", "apellido": "Sánchez", "edad": 17, "estado_civil": "soltero", "genero": "masculino"},
    {"nombre": "Ana", "apellido": "López", "edad": 22, "estado_civil": "casado", "genero": "femenino"},
    {"nombre": "Laura", "apellido": "Martínez", "edad": 16, "estado_civil": "soltero", "genero": "femenino"}
]

# Solución esperada
```

**Salida Esperada**:
```
2
```

---

### Ejercicio 14: Filtrar Casados Menores de 30
**Historia**: En una campaña de marketing, se necesita obtener una lista de clientes casados menores de 30 años para una oferta especial.

```python
# Datos
clientes = [
    {"nombre": "Luis", "apellido": "Ramírez", "edad": 29, "estado_civil": "casado", "genero": "masculino"},
    {"nombre": "Ana", "apellido": "Torres", "edad": 28, "estado_civil": "casado", "genero": "femenino"},
    {"nombre": "Pedro", "apellido": "Moreno", "edad": 35, "estado_civil": "casado", "genero": "masculino"},
    {"nombre": "Clara", "apellido": "García", "edad": 31, "estado_civil": "casado", "genero": "femenino"}
]

# Solución esperada
```

**Salida Esperada**:
```
{'nombre': 'Luis', 'apellido': 'Ramírez', 'edad': 29, 'estado_civil': 'casado', 'genero': 'masculino'}
{'nombre': 'Ana', 'apellido': 'Torres', 'edad': 28, 'estado_civil': 'casado', 'genero': 'femenino'}
```

---

### Ejercicio 15: Listar Solteros de Edad Media
**Historia**: En una encuesta de mercado, se necesita listar a los solteros cuyo rango de edad está entre 20 y 30 años.

```python
# Datos
encuesta = [
    {"nombre": "Juan", "apellido": "Pérez", "edad": 25, "estado_civil": "soltero", "genero": "masculino"},
    {"nombre": "María", "apellido": "Gómez", "edad": 30, "estado_civil": "casado", "genero": "femenino"},
    {"nombre": "Pedro", "apellido": "Sánchez", "edad": 22, "estado_civil": "soltero", "genero": "masculino"},
    {"nombre": "Ana", "apellido": "López", "edad": 32, "estado_civil": "casado", "genero": "femenino"},
    {"nombre": "Laura", "apellido": "Martínez", "edad": 27, "estado_civil": "soltero", "genero": "femenino"}
]

# Solución esperada
```

**Salida Esperada**:
```
{'nombre': 'Juan', 'apellido': 'Pérez', 'edad': 25, 'estado_civil': 'soltero', 'genero': 'masculino'}
{'nombre': 'Pedro', 'apellido': 'Sánchez', 'edad': 22, 'estado_civil': 'soltero', 'genero': 'masculino'}
{'nombre': 'Laura', 'apellido': 'Martínez', 'edad': 27, 'estado_civil': 'soltero', 'genero': 'femenino'}
```

---
# PRACT2 - Colas (Implementación con Listas Enlazadas)

Práctica desarrollada para la asignatura de Estructura de Datos.

## Descripción
Este proyecto implementa una estructura de datos de tipo **Cola (Queue)** bajo el principio **FIFO** (*First In, First Out* - Primero en entrar, primero en salir) utilizando una **lista enlazada** en Python.

## Estructura del Código
* **`Node`**: Clase auxiliar que almacena el valor del elemento y una referencia al siguiente nodo.
* **`LinkedQueue`**: Clase principal que gestiona la cola mediante dos punteros (`head` y `tail`) para garantizar eficiencia en las operaciones de inserción y extracción.

## Métodos Principales
* `enqueue(item)`: Añade un elemento al final de la cola.
* `dequeue()`: Extrae y retorna el elemento del frente de la cola.
* `first()`: Consulta el elemento del frente sin eliminarlo.
* `is_empty()`: Comprueba si la cola no contiene elementos.
* `__len__()`: Retorna el tamaño total de la cola.

## Ejecución
Puedes probar el funcionamiento ejecutando el script directamente:
```bash
python queue.py

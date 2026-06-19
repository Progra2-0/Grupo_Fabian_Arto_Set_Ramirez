# Proyecto N°2 — Simulación de Auto-Home de un Brazo Robótico

## Descripción

Este programa simula el proceso de **auto-home** de un brazo robótico
compuesto por 4 eslabones. El auto-home es la rutina mediante la cual el
brazo vuelve a su posición de origen (posición cero) antes de comenzar un
juego de damas.

Cada eslabón tiene una posición en los ejes X e Y. Al iniciar el programa,
estas posiciones se generan de forma aleatoria dentro del rango de 0 a 360.
Luego, el programa simula el avance de cada eslabón hasta que ambas
posiciones llegan a 0, momento en el cual ese eslabón completó su auto-home.

## Funcionamiento del programa

El programa se ejecuta una sola vez y sigue estos pasos:

1. Se definen los 4 eslabones del brazo (`id1`, `id2`, `id3`, `id4`).
2. Para cada eslabón se generan valores aleatorios de X e Y entre 0 y 360.
3. Cada eslabón avanza hacia la posición (0, 0) restando sus coordenadas de
   a 1 hasta llegar al origen.
4. Cada vez que un eslabón llega a (0, 0), la función correspondiente retorna
   `true` y se imprime su mensaje de término.
5. Cuando los 4 eslabones han retornado `true`, se muestra un mensaje
   indicando que todos completaron el auto-home correctamente.

## Estructura del código

El programa está organizado en una estructura y tres funciones, siguiendo las
partes de la tarea:

- **Estructura `Eslabon`**: agrupa el identificador (`int id`) y las dos
  posiciones (`float x`, `float y`) de cada eslabón.

- **`generarEslabon(Eslabon *e, int id)`**: recibe un puntero al eslabón y le
  asigna su identificador y posiciones aleatorias entre 0 y 360. Al trabajar
  con punteros, modifica el eslabón original directamente.

- **`avance_eslabon(Eslabon *e)`**: recibe un puntero al eslabón y, mediante un
  ciclo `while`, reduce sus posiciones X e Y hasta llegar a 0. Retorna un valor
  booleano `true` cuando el auto-home se completa.

- **`main()`**: crea los 4 eslabones, genera sus posiciones iniciales, ejecuta
  el auto-home de cada uno y muestra los mensajes de término.

## Ejemplo de salida

Las posiciones iniciales cambian en cada ejecución, ya que son aleatorias:

```
Posicion inicial -> id: 1, x: 322.00, y: 245.00
Posicion inicial -> id: 2, x: 87.00, y: 301.00
Posicion inicial -> id: 3, x: 14.00, y: 159.00
Posicion inicial -> id: 4, x: 250.00, y: 33.00

--- Iniciando proceso de auto-home ---

Eslabon 1 terminado
Eslabon 2 terminado
Eslabon 3 terminado
Eslabon 4 terminado

Todos los eslabones realizaron auto-home correctamente.
```

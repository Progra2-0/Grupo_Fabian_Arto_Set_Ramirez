#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

// ============================================================
// PARTE 1 - Definicion de la estructura del eslabon

typedef struct {
    int id;     // Identificador del eslabon
    float x;    // Posicion en X
    float y;    // Posicion en Y
} Eslabon;

// ============================================================
// PARTE 2 - Funcion para generar la posicion inicial aleatoria

void generarEslabon(Eslabon *e, int id) {
    (*e).id = id;
    (*e).x = (float)(rand() % 361);   
    (*e).y = (float)(rand() % 361);   
}

// ============================================================
// PARTE 3 - Funcion para simular el avance hacia auto-home

bool avance_eslabon(Eslabon *e) {
    while ((*e).x > 0 || (*e).y > 0) {
        if ((*e).x > 0) {
            (*e).x = (*e).x - 1;
        }
        if ((*e).y > 0) {
            (*e).y = (*e).y - 1;
        }
    }
    return true;
}

// ============================================================
// PARTE 4 

int main() {
    srand(time(NULL));

    // Definicion de los 4 eslabones obligatorios
    Eslabon id1, id2, id3, id4;

    // Generacion de posiciones iniciales aleatorias para cada eslabon
    generarEslabon(&id1, 1);
    generarEslabon(&id2, 2);
    generarEslabon(&id3, 3);
    generarEslabon(&id4, 4);

    // Mostrar posiciones iniciales generadas
    printf("Posicion inicial -> id: %d, x: %.2f, y: %.2f\n", id1.id, id1.x, id1.y);
    printf("Posicion inicial -> id: %d, x: %.2f, y: %.2f\n", id2.id, id2.x, id2.y);
    printf("Posicion inicial -> id: %d, x: %.2f, y: %.2f\n", id3.id, id3.x, id3.y);
    printf("Posicion inicial -> id: %d, x: %.2f, y: %.2f\n", id4.id, id4.x, id4.y);

    printf("\n--- Iniciando proceso de auto-home ---\n\n");

    // Proceso de auto-home con verificacion del retorno booleano
    bool listo1 = avance_eslabon(&id1);
    if (listo1) {
        printf("Eslabon 1 terminado\n");
    }

    bool listo2 = avance_eslabon(&id2);
    if (listo2) {
        printf("Eslabon 2 terminado\n");
    }

    bool listo3 = avance_eslabon(&id3);
    if (listo3) {
        printf("Eslabon 3 terminado\n");
    }

    bool listo4 = avance_eslabon(&id4);
    if (listo4) {
        printf("Eslabon 4 terminado\n");
    }

    // Mensaje final 
    if (listo1 && listo2 && listo3 && listo4) {
        printf("\nTodos los eslabones realizaron auto-home correctamente.\n");
    }

    return 0;
}

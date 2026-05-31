# 🏆 Tarea 2: Simulador Mundialista con POO y Pandas

Esta tarea consiste en un simulador de una selección de fútbol candidata a ganar el Mundial 2026. Se modelan 11 jugadores titulares de **Portugal** mediante clases, donde cada uno tiene comportamientos propios según su posición (atajar, pasar, marcar, anotar, etc.). Los datos del equipo se procesan con **Pandas** para generar estadísticas y exportar la información a un archivo CSV.

---

## 📁 1. Estructura de la Entrega

```text
tarea_mundial_poo/
├── main.py                          # Programa principal: crea jugadores, ejecuta acciones y genera el CSV
├── jugadores.py                     # Clases (padre Jugador + hijas Portero, Defensa, Mediocampista, Delantero)
├── Informe_Portugal_campeon.pdf     # Informe teórico
├── README.md                        # Este archivo
└── output/
    └── titulares_portugal.csv       # CSV generado tras la ejecución
```

---

## 🇵🇹 2. Selección Elegida: Portugal

**Formación:** 4-4-2 (4 defensas, 4 mediocampistas, 2 delanteros)

| Dorsal | Jugador | Posición |
|--------|---------|----------|
| 22 | Diogo Costa | Portero |
| 4  | Rúben Dias | Defensa |
| 20 | João Cancelo | Defensa |
| 19 | Nuno Mendes | Defensa |
| 14 | Gonçalo Inácio | Defensa |
| 8  | Bruno Fernandes | Mediocampista |
| 15 | João Neves | Mediocampista |
| 16 | Matheus Nunes | Mediocampista |
| 10 | Bernardo Silva | Mediocampista |
| 7  | Cristiano Ronaldo | Delantero |
| 17 | Rafael Leão | Delantero |

---

## 📄 3. Informe

El archivo  [Informe_Portugal_campeon.pdf](./Informe_Portugal_campeon.pdf) contiene la justificación detallada de por qué Portugal sería el campeón del Mundo 2026, analizando cada línea del equipo (portero, defensa, mediocampo y ataque).

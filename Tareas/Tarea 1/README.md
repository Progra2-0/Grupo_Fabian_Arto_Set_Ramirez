# 🤖 Tarea 1: Sistema de Análisis Robótico

Este proyecto implementa un sistema modular en Python para analizar y visualizar el desempeño de políticas de navegación robótica (PPO vs PPO-Mask), replicando los resultados obtenidos en el paper de referencia.

---

## 📚 1. Análisis del Paper (Cuestionario Teórico)
*(Nota: La versión oficial y evaluada de este cuestionario se encuentra en el archivo [Analisis de paper.pdf](./Analisis%20de%20paper.pdf) adjunto en este repositorio).*

**1. ¿Qué problema del mundo real motiva el desarrollo de este trabajo?**
> *Respuesta:* []

**2. Identifique los sensores equipados en el robot. ¿Cuál es la justificación técnica?**
> *Respuesta:* []

**3. Explique la diferencia arquitectónica o algorítmica fundamental entre PPO y PPO-Mask.**
> *Respuesta:* []

**4. ¿Qué magnitud física o tipo de comportamiento penaliza de mayor manera el índice ISE?**
> *Respuesta:* []

---

## 🏗️ 2. Comprensión de la Arquitectura Modular

En proyectos de ingeniería, dividir el código es fundamental para la mantenibilidad y escalabilidad. Basándonos en la investigación solicitada, aplicamos los siguientes conceptos:

* **Módulos:** Cualquier archivo `.py` que contiene funciones, clases o variables enfocadas en una tarea específica para ser reutilizadas. En este proyecto, archivos como `metricas.py` y `cinematica.py` actúan como módulos independientes.
* **Paquetes y `__init__.py`:** Un paquete es un directorio que agrupa módulos relacionados. El archivo `__init__.py` es indispensable para que Python reconozca estas carpetas (`data`, `processing`, `visualization`) como paquetes importables.
* **La sentencia `import`:** Es la herramienta que nos permite conectar la lógica distribuida en los paquetes con el archivo orquestador (`main.py`), permitiendo un flujo de trabajo organizado y limpio.

---

## 📁 3. Estructura del Directorio
El código está orquestado por `main.py` y respeta estrictamente la arquitectura modular obligatoria definida en el enunciado, integrando el informe teórico requerido:

```text
tareal_robot_beach/
├── main.py                 # Punto de entrada: orquesta, no calcula
├── README.md               # Documentación: modularidad y dependencias
├── Analisis de paper.pdf   # Informe teórico (Parte 1)
├── data/                   # Datos del paper y generación de señales
│   ├── __init__.py
│   └── robot_data.py       
├── processing/             # Motor matemático y físico
│   ├── __init__.py
│   ├── metricas.py         # Cálculo de IAE, ISE, ITAE, ITSE
│   └── cinematica.py       # Modelo cinemático del robot
├── visualization/          # Comunicación visual
│   ├── __init__.py
│   └── graficos.py         # Generación de figuras con Matplotlib
└── resultados_graficos/    # Directorio destino para guardar los .png

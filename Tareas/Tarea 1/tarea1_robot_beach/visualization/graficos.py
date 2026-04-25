import matplotlib.pyplot as plt
import os
# Esta funcion dibuja un grafico  comparando metricas de dos formas (PPO y PPO-Mask)
def plot_metricas(diccionario_experimentos, ambiente, ruta):
    metricas = ["ISE", "IAE", "ITSE", "ITAE"] #Las Metricas que se quiere comparar 
    ppo_data = None
    ppo_mask_data = None
    
    # Recorremos el diccionario de experimentos para encontrar los datos que coincidan
    for clave, datos in diccionario_experimentos.items():
        if datos["ambiente"] == ambiente and datos["ruta"] == ruta:
            if datos["politica"] == "PPO":
                ppo_data = datos
            if datos["politica"] == "PPO-Mask":
                ppo_mask_data = datos

    plt.figure(figsize=(16, 6))
    plt.suptitle(f"Índices de error — {ambiente} | {ruta}")
    # gráfico de barras para cada métrica
    for i, metrica in enumerate(metricas):
        plt.subplot(1, 4, i+1) # Los 4 gráficos en una sola fila
        valores = [ppo_data[metrica], ppo_mask_data[metrica]]
        etiquetas = ["PPO", "PPO-Mask"]
        plt.bar(etiquetas, valores, color=["blue", "red"])
        plt.title(metrica)
        plt.ylabel("Valor del Índice")

    plt.tight_layout()
    # Guardamos el gráfico en una carpeta 
    os.makedirs("resultados_graficos", exist_ok=True)
    nombre_archivo = os.path.join("resultados_graficos", f"metricas_{ambiente}_{ruta}.png")
    plt.savefig(nombre_archivo, dpi=150)
    plt.close()

# Esta función dibuja lo que detecta un sensor LIDAR 
def plot_lidar(angulos, distancias, distancias_norm):
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.scatter(angulos, distancias) # ángulo vs distancia
    plt.title("¿A qué distancia están los objetos?\n(Eje X: Ángulo | Eje Y: Metros)")
    plt.xlabel("Ángulo de giro (0-360°)")
    plt.ylabel("Distancia detectada (m)")

    plt.subplot(1, 2, 2)
    plt.plot(angulos, distancias_norm, color="red") # Datos ya normalizados
    plt.title("Datos Normalizados\n(Lo que procesa la IA)")
    plt.xlabel("Sectores del sensor")
    plt.ylabel("Valor (0.0 a 1.0)")

    plt.tight_layout()

    os.makedirs("resultados_graficos", exist_ok=True)
    nombre_archivo = os.path.join("resultados_graficos", "mapa_lidar.png")
    plt.savefig(nombre_archivo, dpi=150)
    plt.close()

# Esta función dibuja trayectorias de dos maneras (PPO y PPO-Mask) junto con los waypoints.
def plot_trayectorias(x_ppo, y_ppo, x_mask, y_mask, waypoints, nombre):
    x_wp = []
    y_wp = []

    # Separamos las coordenadas de los waypoints
    for p in waypoints:
        x_wp.append(p[0])
        y_wp.append(p[1])

    # trayectorias y los puntos objetivo
    plt.figure(figsize=(8, 6))
    plt.plot(x_ppo, y_ppo, label="Trayectoria PPO")
    plt.plot(x_mask, y_mask, label="Trayectoria PPO-Mask", linestyle='--')
    plt.scatter(x_wp, y_wp, marker='s', color='black', label="Waypoints (Metas)")
    plt.axis('equal') # Para que las escalas X e Y sean proporcionales
    plt.title(f"Comparación de Navegación: Ruta {nombre.capitalize()}")
    plt.xlabel("Posición X (metros)")
    plt.ylabel("Posición Y (metros)")
    plt.legend()
    plt.tight_layout()

    os.makedirs("resultados_graficos", exist_ok=True)
    nombre_archivo = os.path.join("resultados_graficos", f"trayectorias_{nombre}.png")
    plt.savefig(nombre_archivo, dpi=150)
    plt.close()

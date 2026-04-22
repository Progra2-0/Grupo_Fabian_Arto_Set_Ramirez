import matplotlib.pyplot as plt
import os

def plot_metricas(diccionario_experimentos,ambiente,ruta):
    metricas = ["ISE", "IAE", "ITSE", "ITAE"]
    ppo_data = None
    ppo_mask_data = None

    for clave,datos in diccionario_experimentos.items():
            if datos["ambiente"] == ambiente and datos["ruta"] == ruta:
                if datos["politica"] == "PPO":
                    ppo_data = datos
                if datos["politica"] == "PPO-Mask":
                    ppo_mask_data = datos

    for i, metrica in enumerate(metricas):
        plt.subplot(1,4,i+1)
        valores=[ppo_data[metrica],ppo_mask_data[metrica]]
        etiquetas = ["PPO", "PPO-Mask"]
        plt.bar(etiquetas, valores, color=["blue", "red"])
        plt.title(metrica)
        plt.ylabel("Valor del Índice")

    os.makedirs("resultados_graficos", exist_ok=True)
    nombre_archivo = os.path.join("resultados_graficos", f"metricas_{ambiente}_{ruta}.png")
    plt.savefig(nombre_archivo, dpi=150)
    plt.close()

def plot_lidar(angulos, distancias, distancias_norm):
    plt.subplot(1, 2, 1)
    plt.scatter(angulos, distancias)
    plt.title("¿A qué distancia están los objetos?\n(Eje X: Ángulo | Eje Y: Metros)")
    plt.xlabel("Ángulo de giro (0-360°)")
    plt.ylabel("Distancia detectada (m)")
    
    plt.subplot(1, 2, 2)
    plt.plot(angulos, distancias_norm, color="red")
    plt.title("Datos Normalizados\n(Lo que procesa la IA)")
    plt.xlabel("Sectores del sensor")
    plt.ylabel("Valor (0.0 a 1.0)")
    
    os.makedirs("resultados_graficos", exist_ok=True)
    nombre_archivo = os.path.join("resultados_graficos", "mapa_lidar.png")
    plt.savefig(nombre_archivo, dpi=150)
    plt.close()

def plot_trayectorias(x_ppo, y_ppo, x_mask, y_mask, waypoints, nombre):

    x_wp = []
    y_wp = []

    for p in waypoints:
        x_wp.append(p[0])
        y_wp.append(p[1])
    
    plt.plot(x_ppo, y_ppo, label="Trayectoria PPO")
    plt.plot(x_mask, y_mask, label="Trayectoria PPO-Mask", linestyle='--')
    plt.scatter(x_wp, y_wp, marker='s', color='black', label="Waypoints (Metas)")
    plt.axis('equal')
    plt.title(nombre)
    plt.xlabel("Posición X (metros)")
    plt.ylabel("Posición Y (metros)")
    plt.legend()

    os.makedirs("resultados_graficos", exist_ok=True)
    nombre_archivo = os.path.join("resultados_graficos", f"{nombre}.png")
    plt.savefig(nombre_archivo, dpi=150)
    plt.close()

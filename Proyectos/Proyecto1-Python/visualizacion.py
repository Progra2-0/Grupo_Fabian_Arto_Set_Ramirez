import matplotlib.pyplot as plt
import numpy as np

def graficar_recoleccion_vs_bateria(resultados: dict):
    #EXTRACCION DE NOMBRES ROBOTS 
    nombres = list(resultados.keys())
    
    #EXTRACCION DE LISTAS 
    basura_total = [resultados[nombre]['basura_total'] for nombre in nombres]
    consumo_bateria = [resultados[nombre]['consumo_bateria'] for nombre in nombres]
    
    #GRAFICO DE BARRAS
    x = np.arange(len(nombres))
    ancho = 0.35 
    
    #EJES
    fig, ax = plt.subplots(figsize=(8, 6))
    
    #DESPLAZAMIENTO DE EJES
    barra_basura = ax.bar(x - ancho/2, basura_total, ancho, label='Basura Recolectada (kg)', color='green')
    barra_bateria = ax.bar(x + ancho/2, consumo_bateria, ancho, label='Batería Consumida (%)', color='red')
    
    # 4.ESTILO Y REQUERIMIENTOS
    ax.set_title('Rendimiento: Recolección vs Consumo Energético')
    ax.set_ylabel('Cantidad')
    
    #REEMPLAZO EJES X NOMBRES ROBOTS
    ax.set_xticks(x)
    ax.set_xticklabels(nombres)
    
    #SHOW LEYEND
    ax.legend()
    
    #FINAL TOUCHS
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    

    plt.show()
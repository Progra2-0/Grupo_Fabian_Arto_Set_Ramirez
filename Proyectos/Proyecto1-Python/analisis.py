import numpy as np

def comparar_rendimiento(datos: list) -> dict:

    arr = np.array(datos)
    nombres = np.unique(arr[:, 1])
    resultados = {}

    for nombre in nombres:       
        
        mask = arr[:, 1] == nombre
        
       
        bateria_filtrada = arr[mask, 4]
        bateria = bateria_filtrada.astype(float)
        
        basura_filtrada = arr[mask, 5]
        basura = basura_filtrada.astype(float)
        
        
        ultima_bateria = bateria[-1]
        consumo = 100.0 - ultima_bateria
        
        basura_total = basura[-1]
        
        
        if consumo > 0:
            eficiencia = basura_total / consumo
        else:
            eficiencia = 0.0
            
        resultados[nombre] = {
            'consumo_bateria': consumo,
            'basura_total': basura_total,
            'eficiencia': eficiencia
        }

    return resultados

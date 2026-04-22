import numpy as np

# calculo de el IAE (Integral of Absolute Error.
# suma el valor absoluto de los errores y lo multiplica por el paso de tiempo.
def calcular_IAE(errores,dt):
    return(float(np.sum(np.abs(errores))*dt))

# calcula el ISE (Integral of Squared Error).
# aquí se suman los errores al cuadrado y se multiplica por dt.
def calcular_ISE(errores,dt):
    return(float(np.sum(errores**2)*dt))
# Calcula el ITAE (Integral of Time-weighted Absolute Error).
# Similar al IAE, pero ahora cada error se multiplica por el tiempo en que ocurrio.
# O sea, errores tardíos pesan más que los iniciales.
def calcular_ITAE(errores,dt):
    tiempo=np.arange(len(errores))*dt
    return(float(np.sum(np.abs(errores)*tiempo)*dt))
# Calcula el ITSE (Integral of Time-weighted Squared Error).
# Igual que el anterior, pero con errores al cuadrado.
# Penaliza fuerte los errores grandes y ademas los que ocurren tarde
def calcular_ITSE(errores,dt):
    tiempo=np.arange(len(errores))*dt
    return(float(np.sum((errores**2)*tiempo)*dt))
#  calcula todas las métricas de una sola pasada y las devuelve en un diccionario.
# Además redondea los resultados a 2 decimales para que se vean más bonitos.
def calcular_todas_las_metricas(errores,dt):
    return {
        "ISE": round(calcular_ISE(errores, dt), 2),
        "IAE": round(calcular_IAE(errores, dt), 2),
        "ITSE": round(calcular_ITSE(errores, dt), 2),
        "ITAE": round(calcular_ITAE(errores, dt), 2)
    }
# Calcula la mejora porcentual entre PPO y PPO-Mask.
# cuánto mejoró PPO-Mask respecto a PPO en porcentaje.
def calcular_mejora(valor_ppo,valor_mask):
    return(round((valor_ppo-valor_mask)/valor_ppo*100))

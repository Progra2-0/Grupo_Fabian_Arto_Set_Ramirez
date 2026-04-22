import numpy as np

def calcular_IAE(errores,dt):
    return(float(np.sum(np.abs(errores))*dt))

def calcular_ISE(errores,dt):
    return(float(np.sum(errores**2)*dt))

def calcular_ITAE(errores,dt):
    tiempo=np.arange(len(errores))*dt
    return(float(np.sum(np.abs(errores)*tiempo)*dt))

def calcular_ITSE(errores,dt):
    tiempo=np.arange(len(errores))*dt
    return(float(np.sum((errores**2)*tiempo)*dt))

def calcular_todas_las_metricas(errores,dt):
    return {
        "ISE": round(calcular_ISE(errores, dt), 2),
        "IAE": round(calcular_IAE(errores, dt), 2),
        "ITSE": round(calcular_ITSE(errores, dt), 2),
        "ITAE": round(calcular_ITAE(errores, dt), 2)
    }

def calcular_mejora(valor_ppo,valor_mask):
    return(round((valor_ppo-valor_mask)/valor_ppo*100))

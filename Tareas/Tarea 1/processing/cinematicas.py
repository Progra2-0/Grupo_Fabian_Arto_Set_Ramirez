import numpy as np

def calcular_movimiento(x,y,theta,v,omega,dt=0.1):
    # Se calcula la nueva pose (x, y, theta) del robot.
    # Saturación de actuadores: Restringimos la velocidad máxima según las capacidades de los motores (Tabla 1 del paper)
    v = np.clip(v,-0.8,0.8)
    omega = np.clip(omega,-0.6,0.6)
    # Nueva posición = Posición actual + avance en ese eje
    x_nuevo = x*v*np.cos(theta)*dt
    y_nuevo = y*v*np.sin(theta)*dt
    # Nueva orientación = Orientación actual + giro
    theta_nuevo = theta + omega*dt
    return x_nuevo,y_nuevo,theta_nuevo

def distancia_al_objetivo(x,y,x_meta,y_meta):
    # Se aplica el teorema de Pitágoras para la distancia entre dos puntos
    return (np.sqrt((x_meta-x)**2 + (y_meta-y)**2))

def calcular_error_seguimiento(x_real,y_real,x_ideal,y_ideal):
    # Se compara la trayectoria ejecutada por el robot contra la ruta ideal.
    
    # Se encuentra la longitud de la lista más corta
    min_len = min(len(x_real),len(x_ideal))
    # Se recortan todos los arreglos a esa longitud mínima
    x_real = np.array(x_real[:min_len])
    y_real = np.array(y_real[:min_len])
    x_ideal = np.array(x_ideal[:min_len])
    y_ideal = np.array(y_ideal[:min_len])

    # Se calcula el error de distancia punto a punto de manera vectorizada
    return np.sqrt((x_real - x_ideal)**2 + (y_real - y_ideal)**2)

import numpy as np

def calcular_movimiento(x,y,theta,v,omega,dt=0.1):
    v = np.clip(v,-0.8,0.8)
    omega = np.clip(omega,-0.6,0.6)
    x_nuevo = x*v*np.cos(theta)*dt
    y_nuevo = y*v*np.sin(theta)*dt
    theta_nuevo = theta + omega*dt
    return x_nuevo,y_nuevo,theta_nuevo

def distancia_al_objetivo(x,y,x_meta,y_meta):
    return (np.sqrt((x_meta-x)**2 + (y_meta-y)**2))

def calcular_error_seguimiento(x_real,y_real,x_ideal,y_ideal):
    min_len = min(len(x_real),len(x_ideal))
    x_real = np.array(x_real[:min_len])
    y_real = np.array(y_real[:min_len])
    x_ideal = np.array(x_ideal[:min_len])
    y_ideal = np.array(y_ideal[:min_len])
    
    return np.sqrt((x_real - x_ideal)**2 + (y_real - y_ideal)**2)

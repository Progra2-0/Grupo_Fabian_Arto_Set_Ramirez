#Libreria necesaria para calcular como se mueve el robot en el espacio.
import math

# ATRIBUTOS Y ENCAPSULAMIENTO

# Aqui se define la clase principal, que funcionara como la plantilla para los otros robots.
class RobotBase:
    # Es la funcion que se ejecuta al crear un robot y configura su estado inicial. 
    # Se usa el doble guion para hacerlos extrictamente privados como se requiere.
    def __init__(self, nombre: str, capacidad_carga: float, x_inicial=0.0, y_inicial=0.0, yaw_inicial=0.0):
        self.__nombre = nombre
        self.__capacidad_carga = capacidad_carga
        self.__bateria = 100.0
        self.__pos_x = x_inicial
        self.__pos_y = y_inicial
        self.__yaw = yaw_inicial
        self.__basura_recolectada = 0.0
        self.__step_dt = 0.1
        
        # Estos atributos no necesitan proteccion para poder almacenar donde se dirigue el robot. 
        # Se inicializan en 5.0
        self.target_x = 5.0
        self.target_y = 5.0

    # Aqui se usan los getters necesarios que retornan las variables privadas definidas anteriormente para que el codigo main.py pueda leerlas.
    def get_nombre(self):
        return self.__nombre

    def get_bateria(self):
        return self.__bateria

    def get_pos_x(self):
        return self.__pos_x

    def get_pos_y(self):
        return self.__pos_y

    def get_yaw(self):
        return self.__yaw

    def get_basura_recolectada(self):
        return self.__basura_recolectada

    # Se definen los metodos protegidos necesarios para poder usarlos y modificarlos de manera interna.
    def _actualizar_pose(self, x, y, yaw): # Sobreescribe las coordenadas actuales del robot.
        self.__pos_x = x
        self.__pos_y = y
        self.__yaw = yaw

    def _reducir_bateria(self, cantidad): # Se resta energia y se asegura de que el porcentaje no baje de cero.
        self.__bateria -= cantidad
        if self.__bateria < 0.0:
            self.__bateria = 0.0

    def _recolectar_basura(self, cantidad): # Primero se calcula cuanto espacio le queda al robot.
        espacio_disponible = self.__capacidad_carga - self.__basura_recolectada
        if cantidad <= espacio_disponible: # Si la basura que se quiere recoger es menor o igual al espacio entonces la recoge toda.
            self.__basura_recolectada += cantidad
        else: # Si es mayor solo suma el espacio disponible para no sobrepasar el limite de carga.
            self.__basura_recolectada += espacio_disponible

# METODOS ESTATICOS
# Estas son funciones matematicas que no necesitan acceder a datos individuales de los robots, simplemente usan los valores que se les de entre los parentesis.

    @staticmethod
    def calc_dist_to_goal(pos_x, pos_y, target_x, target_y): # Se tiliza el teorema de Pitagoras para calcular la distancia entre el robot y la meta.
        return math.sqrt((target_x - pos_x)**2 + (target_y - pos_y)**2)

    @staticmethod
    def calc_yaw_error(pos_x, pos_y, yaw, target_x, target_y): # Calcula el angulo de error hacia el objetivo.
        theta_meta = math.atan2(target_y - pos_y, target_x - pos_x) # Se calcula el angulo absoluto hacia donde esta la meta (theta_meta).
        err = theta_meta - yaw # Se resta el yaw para encontrar el error.
        err_norm = (err + math.pi) % (2 * math.pi) - math.pi # Se normaliza para que este en el rango de [-pi,pi] radianes.
        return err_norm


# SIMULACION CINEMATICA
# Este es la base del movimiento del robot que recibe la velocidad para avanzar (v) y la velocidad para girar (w).

    def step(self, v, w):
        # Si el robot se queda sin bateria, devuelve una recompensa de 0.0 y True (Su simulacion termina).
        if self.__bateria <= 0:
            return 0.0, True
        
        # Se calcula el nuevo yaw y se normaliza
        yaw_nuevo = self.__yaw + w * self.__step_dt
        yaw_nuevo_norm = (yaw_nuevo + math.pi) % (2 * math.pi) - math.pi
        
        # Se calculan las nuevas posiciones X e Y multiplicando la velocidad lineal (v) por el coseno y seno del ángulo yaw normalizado respectivamente.
        x_nuevo = self.__pos_x + v * math.cos(yaw_nuevo_norm) * self.__step_dt
        y_nuevo = self.__pos_y + v * math.sin(yaw_nuevo_norm) * self.__step_dt
        
        # Se guardan los nuevos valores usando el metodo interno protegido.
        self._actualizar_pose(x_nuevo, y_nuevo, yaw_nuevo_norm)
        
        # Se Calculan la distancia y el error angular actual usando los métodos estáticos implementados anteriormente.
        distancia = self.calc_dist_to_goal(self.__pos_x, self.__pos_y, self.target_x, self.target_y)
        error_angular = self.calc_yaw_error(self.__pos_x, self.__pos_y, self.__yaw, self.target_x, self.target_y)
        
        # La recompensa (reward) se calcula restando la distancia con el error angular, penalizando el alejamiento.
        reward = -distancia - abs(error_angular)
        llegamos = False
        
        # Si la distancia es menor a 0.5 se considera que el robot llego al objetivo, se cambia llegamos a True y se suman 100 puntos a la recompensa.
        if distancia < 0.5:
            llegamos = True
            reward += 100.0
            
        # Se retornan los 2 valores
        return reward, llegamos


# METODOS ABSTRACTOS
# RobotBase es solo una plantilla estricta que no define como moverse ni limpiar.
# Esta parte lanza un error que obliga a las clases específicas (como el dron o el triciclo) a crear su propio codigo para estos fines.

    def mover(self):
        raise NotImplementedError("Las clases hijas deben implementar el método mover()")

    def limpiar(self):
        raise NotImplementedError("Las clases hijas deben implementar el método limpiar()")

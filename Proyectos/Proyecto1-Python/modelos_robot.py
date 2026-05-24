from robot_base import RobotBase
#RobotBase, la clase padre que contiene los métodos y atributos
#comunes que heredarán los tres tipos de robot definidos en este archivo.
import random # Se usa para generar la cantidad de basura recolectada de forma aleatoria.

# Cada clase hereda de RobotBase y sobrescribe mover() y limpiar()
# con valores propios, es decir se usa polimorfismo para que el mismo método, tenga un comportamiento distinto

# A continuación se define la primera clase hija, llamada RobotTresRuedas, 
# contiene un método específico de ella llamada calibrar_giro() y, los dos métodos heredados mover() y limpiar()
# que tiene un comportamiento específico para esta clase hija.

class RobotTresRuedas(RobotBase):
    # En el __init__ se ponen los valores que se van a agregar desde el main, que sería su nombre y el radio de la rueda
    def __init__(self, nombre: str, radio_rueda: float): 
        # Al agregar el super().__init__ estamos diciendo que vamos usar los atributos que entrega la clase padre, 
        # nombre: str, capacidad_carga: float, x_inicial=0.0, y_inicial=0.0, yaw_inicial=0.0, 
        # como se puede en ella ya viene establecido el valor de la capacidad de carga, en este caso es de 20.0.
        super().__init__(nombre,20.0)
        self.ruedas_calibradas=False
        self.radio_rueda = radio_rueda
    # Con todo lo anterior se crea un objeto con un cierto nombre, una cierta capacidad de carga,
    # un cierto radio de rueda y con sus posiciones iniciales (x,y,yaw).

    # Definimos el método único calibrar_giro(), esta cambia el estado de calibración y imprime un cierto mensaje en pantalla.
    def calibrar_giro(self):
        print(f"[{self.get_nombre()}] Calibrando triciclo con ruedas de {self.radio_rueda} cm...")
        self.ruedas_calibradas=True
    # Definimos el método mover() a través de herencia para usar el método de la clase padre step(0.8,0.2).
    def mover(self):
        reward,llegamos=super().step(0.8, 0.2)
        return reward,llegamos
    # Definimos el método limpiar() a través de herencia para usar dos métodos de la clase padre _reducir_bateria(2.0) 
    # y _recolectar_basura(numero random entre 0.5 y 1.5) 
    # Llevan el símbolo "_" porque deben acceder/modificar datos protegidos.
    def limpiar(self):
        self._reducir_bateria(2.0)
        self._recolectar_basura(random.uniform(0.5, 1.5))

       
# Creación de la clase hija RobotOruga,
# contiene el método único ajustar_tension() y los dos métodos heredados mencionados anteriormente mover() y limpiar().
class RobotOruga(RobotBase):
    # En este caso se requiere que desde el main se ingrese nombre, la tensión de la oruga.
    def __init__(self,nombre:str,tension_oruga:float):
        # Entrega los mismos atributos de la clase hija RobotTresRuedas, solo que en este caso se establece el valor de la capacidad de carga en 50.0 .
        super().__init__(nombre,50.0)
        self.tension_oruga = tension_oruga
    # Con todo lo anterior se crea un objeto con un cierto nombre, una cierta capacidad de carga,
    # una cierta tensión de oruga y con sus posiciones iniciales (x,y,yaw).

    # Definimos método único ajustar_tension(), imprime en pantalla las tensiones de las orugas.
    def ajustar_tension(self):
        print(f"[{self.get_nombre()}] Ajustando tension de las orugas al {self.tension_oruga}%.")

    #  Definimos método mover()a través de herencia para usar el método de la clase padre step(0.3,0.8).
    def mover(self):
        reward,llegamos=super().step(0.3, 0.8)
        return reward,llegamos

    # Definimos método limpiar() a través de herencia para usar dos métodos de la clase padre _reducir_bateria(4.5) 
    # y _recolectar_basura(numero random entre 2.0 y 4.0).

    def limpiar(self):
        self._reducir_bateria(4.5)
        self._recolectar_basura(random.uniform(2.0, 4.0))

    
# Creación de la clase hija RobotDron
# contiene el método único despegar() y los dos métodos heredados mencionados anteriormente mover() y limpiar().
class RobotDron(RobotBase):
    # En este caso se requiere que desde el main se ingrese nombre, altura máxima.
    def __init__(self,nombre:str,altura_maxima:float):
        # Entrega los mismos atributos de la clase hija RobotTresRuedas, solo que en este caso se establece el valor de la capacidad de carga en 5.0 .
        super().__init__(nombre,5.0)
        self.altura_maxima =altura_maxima
        # Se establece un atributo que indica si está en vuelo o no y según su estado va a realizar unas funciones o otras, en sus métodos.
        self.en_vuelo=False

    # Definimos método despegar, imprime la altura máxima y cambia el estado de vuelo a true (en_vuelo=True).
    def despegar(self):
        self.en_vuelo=True
        print(f"[{self.get_nombre()}] Despegando hasta {self.altura_maxima} metros de altura.")
    
    #  Definimos método mover() a través de herencia para usar el método de la clase padre step(2.5,1.0) solo llama al método padre si está en vuelo(en_vuelo=True).
    def mover(self):

        if self.en_vuelo:
            reward,llegamos=super().step(2.5, 1.0)
        else:
            reward,llegamos=0.0,False    

        return reward,llegamos
    
    # Definimos método limpiar() a través de herencia para usar dos métodos de la clase padre _reducir_bateria(3.0) 
    # y _recolectar_basura(numero random entre 0.1 y 0.4), solo llama a los métodos del padre si está en vuelo(en_vuelo=True).
    def limpiar(self):
        if self.en_vuelo:
            self._reducir_bateria(3.0)
            self._recolectar_basura(random.uniform(0.1, 0.4))
    

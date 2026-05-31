import random # Es extra solo para darle mas realismo.
#Clase Padre
class Jugador:
    def __init__(self, nombre, edad, altura, dorsal):
        # Atributos
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.dorsal = dorsal

    def correr(self):
        
        return f"{self.nombre} está corriendo por la cancha."

    def mostrar_rol(self):
       
        return f"Soy un jugador de fútbol."

    def entrenar(self):
       
        return f"{self.nombre} está entrenando duro."

    def descansar(self):
        
        return f"{self.nombre} está descansando para el próximo partido."

#Clases hijas usando herencia y polimorfismo
class Portero(Jugador):
    def __init__(self, nombre, edad, altura, dorsal, atajadas, saques_completados):
        super().__init__(nombre,edad,altura,dorsal)
        self.atajadas = atajadas                     
        self.saques_completados = saques_completados

    def mostrar_rol(self):
        return f"{self.nombre} - Portero"

    def atajar(self):
        ataje_exitoso = random.choice([True, False])
        if ataje_exitoso:
            self.atajadas += 1
            return f"{self.nombre} atajó el tiro. (Atajadas: {self.atajadas})"
        else:
            return f"{self.nombre} se le pasó el balón."
        
    def saque_arco(self):
        saque_exitoso = random.choice([True, False])
    
        if saque_exitoso:
            self.saques_completados += 1
            return f"{self.nombre} metió un saque de arco preciso al pecho de su compañero. (Saques completados: {self.saques_completados})"
        else:
            return f"{self.nombre} le pegó mal en el saque de arco y regaló el balón al rival."
        


class Defensa(Jugador):
    def __init__(self, nombre, edad, altura, dorsal, balones_recuperados, balones_despejados, faltas, amarillas, rojas):
        super().__init__(nombre,edad,altura,dorsal)
        self.balones_recuperados = balones_recuperados
        self.balones_despejados = balones_despejados
        self.faltas = faltas
        self.amarillas = amarillas
        self.rojas = rojas


    def mostrar_rol(self):
        return f"{self.nombre} - Defensa"

    def barrido(self): # Método propio 1 (Asociado a recuperar)
        barrido_exitoso = random.choice([True, False])
    
        if barrido_exitoso:
            self.balones_recuperados += 1
            return f"¡{self.nombre} se barrió limpiamente y recuperó el balón ! Balones recuperados: {self.balones_recuperados}"
        else:
            # Vamos implementar un sistema de tarjetas básico con random.
            tarjeta=random.randint(1, 100)
            self.faltas += 1
            if(tarjeta <= 60):
                return f"{self.nombre} entró de forma incorrecta y se llevó una advertencia."
            elif(tarjeta <=90): 
                self.amarillas += 1
                return f"{self.nombre} entró de forma incorrecta y se llevó una tarjeta amarilla."
            else:
                self.rojas += 1
                return f"{self.nombre} entró de forma muy agresiva, se llevó tarjeta roja, ¡expulsión directa!."
            
    def despeje(self): # Método propio 2 (Asociado a despejar)

        # Sumamos 1 al contador para simular la acción en tiempo real

        self.balones_despejados += 1
        return f"¡{self.nombre} reventó la pelota! Balones despejados: {self.balones_despejados}"


class Mediocampista(Jugador):
    def __init__(self, nombre, edad, altura, dorsal, asistencias, pases_completados):
        super().__init__(nombre,edad,altura,dorsal)
        self.asistencias = asistencias
        self.pases_completados = pases_completados

    def mostrar_rol(self):
        return f"{self.nombre} - Mediocampista"
    
    def dar_pase(self):

        probabilidad = random.randint(1, 100)
        
        if probabilidad <= 70:
            self.pases_completados += 1
            return f"¡Hermoso pase filtrado de {self.nombre}! (Pases completados: {self.pases_completados})"
        else:
            return f"{self.nombre} intentó un pase profundo, pero la defensa rival interceptó."

    def centrar(self):

        exito = random.choice([True, False]) # 50/50

        if exito:
            self.asistencias += 1
            return f"¡Centro perfecto de {self.nombre} que termina en gol! (Asistencias: {self.asistencias})"
        else:
            return f"{self.nombre} mandó el centro pasado y el balón se fue por la línea de fondo."
        

class Delantero(Jugador):
    def __init__(self, nombre, edad, altura, dorsal, tiros_al_arco, goles, faltas, amarillas, rojas):
        super().__init__(nombre,edad,altura,dorsal)
        self.tiros_al_arco = tiros_al_arco
        self.goles = goles
        self.faltas = faltas
        self.amarillas = amarillas
        self.rojas = rojas

    def mostrar_rol(self):
        return f"{self.nombre} - Delantero"

    def patear_al_arco(self):
        self.tiros_al_arco += 1
        # 60% de probabilidad de gol
        probabilidad = random.randint(1, 100)
        
        if probabilidad <= 60:
            self.goles += 1
            return f"¡GOOOOOOL! {self.nombre} definió con potencia. (Goles: {self.goles} | Tiros: {self.tiros_al_arco})"
        elif probabilidad <=75:
            return f"¡TAPADÓN! El tiro de {self.nombre} fue al ángulo, pero el portero rival la atajó. (Tiros: {self.tiros_al_arco})"
        else:
            return f"¡Se le fue! El tiro de {self.nombre} llegó a las gradas"

    def presionar_salida(self):
        exito = random.choice([True, False])
        if exito:
            return f"¡Buena presión! {self.nombre} asfixió la salida y forzó el error del defensa."
        else:
            self.faltas += 1
            return f"¡FALTA en ataque! {self.nombre} metió un empujón por la espalda. (Faltas: {self.faltas})"
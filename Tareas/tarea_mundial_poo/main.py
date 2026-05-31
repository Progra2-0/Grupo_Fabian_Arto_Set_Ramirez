import os
import pandas as pd
from jugadores import Portero,Defensa,Mediocampista,Delantero #Clases hijas
pais_elegido = "Portugal"

# 11 jugadores titulares (formación 4-4-2 como indican en la tarea)

jugadores_titulares = [
    # 1 Portero (nombre, edad, altura, dorsal, atajadas, saques_completados)
    Portero("Diogo Costa", 26, 1.86, 22, atajadas=145, saques_completados=320),

    # 4 Defensas (nombre, edad, altura, dorsal, balones_recuperados, balones_despejados, faltas, amarillas, rojas)
    Defensa("Rúben Dias", 29, 1.87, 4, balones_recuperados=285, balones_despejados=310, faltas=45, amarillas=8, rojas=1),
    Defensa("João Cancelo", 32, 1.82, 20, balones_recuperados=210, balones_despejados=150, faltas=38, amarillas=6, rojas=0),
    Defensa("Nuno Mendes", 23, 1.76, 19, balones_recuperados=165, balones_despejados=95, faltas=28, amarillas=4, rojas=0),
    Defensa("Gonçalo Inácio", 24, 1.85, 14, balones_recuperados=190, balones_despejados=215, faltas=32, amarillas=5, rojas=1),

    # 4 Mediocampistas (nombre, edad, altura, dorsal, asistencias, pases_completados)
    # Lógica: Asistencias siempre son una fracción muy pequeña de los pases totales
    Mediocampista("Bruno Fernandes", 31, 1.79, 8, asistencias=62, pases_completados=1850),
    Mediocampista("João Neves", 21, 1.74, 15, asistencias=14, pases_completados=980),
    Mediocampista("Matheus Nunes", 27, 1.83, 16, asistencias=22, pases_completados=1240),
    Mediocampista("Bernardo Silva", 31, 1.73, 10, asistencias=58, pases_completados=2100),

    # 2 Delanteros (nombre, edad, altura, dorsal, tiros_al_arco, goles, faltas, amarillas, rojas)
    # Lógica: Goles < Tiros al arco. Rojas< Faltas, Amarillas < Faltas.
    Delantero("Cristiano Ronaldo", 41, 1.87, 7, tiros_al_arco=415, goles=130, faltas=85, amarillas=12, rojas=1),
    Delantero("Rafael Leão", 26, 1.88, 17, tiros_al_arco=180, goles=42, faltas=45, amarillas=6, rojas=0)
]

print("--- SIMULADOR DE CAMPEÓN DEL MUNDO ---")

# PARTE 3: ACCIONES EN LA CANCHA (MÉTODOS HEREDADOS Y PROPIOS)

print("\n" + "="*50)
print("Acciones en la cancha:")
print("="*50)

for jugador in jugadores_titulares:
    # Llamamos al método heredado de la clase padre
    print(jugador.correr()) 
    
    # Llamamos a un método propio según la clase hija
    if isinstance(jugador, Portero):
        print(jugador.atajar())
    elif isinstance(jugador, Defensa):
        print(jugador.barrido())
    elif isinstance(jugador, Mediocampista):
        print(jugador.dar_pase())
    elif isinstance(jugador, Delantero):
        print(jugador.patear_al_arco())

# PARTE 4: ROLES DEL EQUIPO (POLIMORFISMO PURO)
print("\n" + "="*50)
print("Roles del equipo")
print("="*50)

for jugador in jugadores_titulares:
    # Llama al método mostrar_rol() de cada objeto.
    print(jugador.mostrar_rol())

# --- PARTE 5: USO DE PANDAS Y EXPORTACIÓN ---
datos_equipo = []

for j in jugadores_titulares:
    rol_limpio = j.mostrar_rol().split(" - ")[1] if " - " in j.mostrar_rol() else j.mostrar_rol()
    
    # 1. Creamos la fila base con los datos obligatorios y guiones en los opcionales
    fila = {
        "Pais": pais_elegido,
        "Dorsal": j.dorsal,
        "Nombre": j.nombre,
        "Edad": j.edad,
        "Altura_m": j.altura,
        "Posicion": rol_limpio,
        "Goles": "-",
        "Asistencias": "-",
        "Atajadas": "-",
        "Balones_Recuperados": "-",
        "Pases_Completados": "-",
        "Faltas": "-",
        "Amarillas": "-",
        "Rojas": "-"
    }
    
    # 2. Intentamos sacar los atributos propios. Si el jugador no lo tiene, ignoramos el error y queda el guion.
    try:
        fila["Goles"] = j.goles
    except AttributeError:
        pass

    try:
        fila["Asistencias"] = j.asistencias
    except AttributeError:
        pass

    try:
        fila["Atajadas"] = j.atajadas
    except AttributeError:
        pass

    try:
        fila["Balones_Recuperados"] = j.balones_recuperados
    except AttributeError:
        pass

    try:
        fila["Pases_Completados"] = j.pases_completados
    except AttributeError:
        pass

    try:
        fila["Faltas"] = j.faltas
    except AttributeError:
        pass

    try:
        fila["Amarillas"] = j.amarillas
    except AttributeError:
        pass

    try:
        fila["Rojas"] = j.rojas
    except AttributeError:
        pass

    # 3. Agregamos la fila lista a nuestra lista principal
    datos_equipo.append(fila)

# Construir el DataFrame
df = pd.DataFrame(datos_equipo)

# --- IMPRESIÓN SOLICITADA EN LA PAUTA ---
print("\n" + "="*50)
print("ESTADÍSTICAS DEL EQUIPO (PANDAS)")
print("="*50)

print("\n1. La tabla completa del equipo:")
print(df)

print(f"\n2. La edad promedio del equipo: {df['Edad'].mean():.1f} años")

print(f"\n3. La altura máxima del equipo: {df['Altura_m'].max():.2f} metros")

print("\n4. La cantidad de jugadores por posición:")
print(df.groupby('Posicion')['Nombre'].count().to_string())

print("\n5. El promedio de edad por posición:")
print(df.groupby('Posicion')['Edad'].mean().round(1).to_string())

# Exportar a CSV
os.makedirs("output", exist_ok=True)
ruta_archivo = f"output/titulares_{pais_elegido.lower()}.csv"
df.to_csv(ruta_archivo, index=False, sep=';', encoding="utf-8")
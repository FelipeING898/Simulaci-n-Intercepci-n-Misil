import math

def calcular_velocidad_inicial(g, xmax, x):
    # Convertir ángulo a radianes
    x_radianes = math.radians(x)
    
    # Calcular el valor de la sin(2x)
    seno_doble = math.sin(2 * x_radianes)
    
    # Calcular la velocidad inicial
    V0 = math.sqrt((g * xmax) / seno_doble)
    
    return V0

# Ejemplo de uso
g = 9.81  # Aceleración gravitacional en m/s^2
xmax = 100000  # Distancia máxima en metros
x = 45  # Ángulo en grados

velocidad_inicial = calcular_velocidad_inicial(g, xmax, x)
print(f"La velocidad inicial es: {velocidad_inicial:.2f} m/s")


import math

# Definir variables
Vo = 990.45  # Velocidad inicial en m/s
theta = 45  # Ángulo en grados
t = 126.75  # Tiempo en segundos (ejemplo)

# Convertir el ángulo a radianes
theta_rad = math.radians(theta)

# Calcular la distancia en x usando la fórmula x = Vo * cos(theta) * t
x_distance = Vo * math.cos(theta_rad) * t

print(f"La distancia en x es {x_distance:.2f} metros después de {t} segundos.")

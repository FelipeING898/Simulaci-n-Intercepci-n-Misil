import math

# Definir variables
g = 9.8  # Gravedad en m/s^2
Vo = 990.45  # Velocidad inicial en m/s
x = 45  # Ángulo en grados
h = 10000  # Altura de impacto en metros

# Convertir el ángulo a radianes
x_rad = math.radians(x)

# Coeficientes de la ecuación cuadrática ax^2 + bx + c = 0
a = -0.5 * g
b = Vo * math.sin(x_rad)
c = -h

# Resolver la ecuación cuadrática usando la fórmula general
discriminante = b**2 - 4*a*c

if discriminante >= 0:
    # Hay dos soluciones, pero tomamos la solución positiva para el tiempo
    t1 = (-b + math.sqrt(discriminante)) / (2 * a)
    t2 = (-b - math.sqrt(discriminante)) / (2 * a)
    
    # El tiempo debe ser positivo
    t = max(t1, t2)
    print(f"El tiempo de intercepción es {t:.2f} segundos")
else:
    print("No hay solución real para el tiempo")

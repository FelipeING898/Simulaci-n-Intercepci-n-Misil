import math

class Proyectil:
    def __init__(self, velocidad_inicial, angulo, altura_impacto):
        self.g = 9.8  # Aceleración debido a la gravedad
        self.vo = velocidad_inicial  # Velocidad inicial
        self.angulo = math.radians(angulo)  # Ángulo de lanzamiento en radianes
        self.altura_impacto = altura_impacto

    def calcular_tiempo_intercepcion(self):
        a = -0.5 * self.g
        b = self.vo * math.sin(self.angulo)
        c = -self.altura_impacto

        discriminante = b**2 - 4*a*c

        if discriminante >= 0:
            t1 = (-b + math.sqrt(discriminante)) / (2 * a)
            t2 = (-b - math.sqrt(discriminante)) / (2 * a)
            return max(t1, t2)
        else:
            return None

# Ejemplo de uso:
proyectil1 = Proyectil(990.45, 45, 10000)
tiempo = proyectil1.calcular_tiempo_intercepcion()

if tiempo is not None:
    print(f"El tiempo de intercepción es {tiempo:.2f} segundos")
else:
    print("No hay solución real para el tiempo")
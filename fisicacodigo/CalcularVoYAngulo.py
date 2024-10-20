import matplotlib
matplotlib.use("TkAgg")  # Asegura que se use el backend correcto para tkinter

import math
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import tkinter as tk
from tkinter import messagebox

class Proyectil:
    def __init__(self, velocidad_inicial=0, angulo=0, posicion_inicial=0):
        self.g = 9.81  # Aceleración de la gravedad
        self.vo = velocidad_inicial
        self.theta = math.radians(angulo)  # Ángulo en radianes
        self.xo = posicion_inicial  # Posición inicial horizontal

    def calcular_velocidad_inicial_para_alcance(self, xmax):
        """Calcula la velocidad inicial necesaria para alcanzar una distancia máxima."""
        seno_doble = math.sin(2 * self.theta)
        return math.sqrt((self.g * xmax) / seno_doble)

    def calcular_tiempo_intercepcion(self, altura):
        """Calcula el tiempo que tarda en alcanzar una altura específica."""
        a = -0.5 * self.g
        b = self.vo * math.sin(self.theta)
        c = -altura
        discriminante = b**2 - 4*a*c
        if discriminante >= 0:
            t1 = (-b + math.sqrt(discriminante)) / (2 * a)
            t2 = (-b - math.sqrt(discriminante)) / (2 * a)
            return max(t1, t2)
        else:
            return None

    def calcular_posicion_en_tiempo(self, t):
        """Calcula la posición (x, y) del proyectil en un tiempo t."""
        x = self.xo + self.vo * math.cos(self.theta) * t
        y = self.vo * math.sin(self.theta) * t - 0.5 * self.g * t**2
        return x, y

def sistema_ecuaciones(vars, proyectil_inicial, proyectil_interceptor, t_intercepcion, g):
    Vo, angulo = vars
    x_intercepcion_inicial, y_intercepcion = proyectil_inicial.calcular_posicion_en_tiempo(t_intercepcion)

    eq1 = proyectil_interceptor.xo + Vo * math.cos(angulo) * t_intercepcion - x_intercepcion_inicial
    eq2 = Vo * math.sin(angulo) * t_intercepcion - 0.5 * g * t_intercepcion**2 - y_intercepcion

    return [eq1, eq2]

def calcular_trayectorias():
    try:
        angulo_misil = float(entrada_angulo_misil.get())
        xmax_misil = float(entrada_xmax.get())
        altura_intercepcion = float(entrada_altura.get())
        posicion_inicial_interceptor = float(entrada_posicion.get())

        proyectil_inicial = Proyectil(0, angulo_misil, 0)  # Misil enemigo desde x=0
        velocidad_inicial_enemigo = proyectil_inicial.calcular_velocidad_inicial_para_alcance(xmax_misil)
        proyectil_inicial.vo = velocidad_inicial_enemigo

        proyectil_interceptor = Proyectil(0, 0, posicion_inicial_interceptor)

        t_intercepcion = proyectil_inicial.calcular_tiempo_intercepcion(altura_intercepcion)

        if t_intercepcion is not None:
            x_intercepcion, y_intercepcion = proyectil_inicial.calcular_posicion_en_tiempo(t_intercepcion)

            sol_inicial = [500, math.radians(45)]
            solucion = fsolve(sistema_ecuaciones, sol_inicial, args=(proyectil_inicial, proyectil_interceptor, t_intercepcion, 9.81))

            Vo_interceptor, angulo_interceptor = solucion
            proyectil_interceptor.vo = Vo_interceptor
            proyectil_interceptor.theta = angulo_interceptor

            t_vals = [t for t in range(0, int(t_intercepcion) + 2)]

            x_enemigo = []
            y_enemigo = []
            for t in t_vals:
                x, y = proyectil_inicial.calcular_posicion_en_tiempo(t)
                x_enemigo.append(x)
                y_enemigo.append(y)

            x_interceptor = []
            y_interceptor = []
            for t in t_vals:
                x, y = proyectil_interceptor.calcular_posicion_en_tiempo(t)
                x_interceptor.append(x)
                y_interceptor.append(y)

            plt.plot(x_enemigo, y_enemigo, label="Misil Enemigo", color="red")
            plt.plot(x_interceptor, y_interceptor, label="Misil Interceptor", color="blue")
            plt.scatter(x_intercepcion, y_intercepcion, color="green", label="Punto de Intercepción")
            plt.title("Trayectoria del misil enemigo y el misil interceptor")
            plt.xlabel("Distancia (m)")
            plt.ylabel("Altura (m)")
            plt.legend()
            plt.grid(True)
            plt.show()

        else:
            messagebox.showerror("Error", "No se puede alcanzar la altura de intercepción.")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Simulación de Intercepción de Misiles")

# Etiquetas y entradas
etiqueta_angulo_misil = tk.Label(ventana, text="Ángulo del misil enemigo (grados):")
etiqueta_angulo_misil.grid(row=0, column=0)
entrada_angulo_misil = tk.Entry(ventana)
entrada_angulo_misil.grid(row=0, column=1)

etiqueta_xmax = tk.Label(ventana, text="Distancia máxima del misil enemigo (xmax) en metros:")
etiqueta_xmax.grid(row=1, column=0)
entrada_xmax = tk.Entry(ventana)
entrada_xmax.grid(row=1, column=1)

etiqueta_posicion = tk.Label(ventana, text="Posición inicial del misil antiaéreo (Xo) en metros:")
etiqueta_posicion.grid(row=2, column=0)
entrada_posicion = tk.Entry(ventana)
entrada_posicion.grid(row=2, column=1)

etiqueta_altura = tk.Label(ventana, text="Altura de intercepción en metros:")
etiqueta_altura.grid(row=3, column=0)
entrada_altura = tk.Entry(ventana)
entrada_altura.grid(row=3, column=1)

# Botón para calcular
boton_calcular = tk.Button(ventana, text="Calcular y Graficar", command=calcular_trayectorias)
boton_calcular.grid(row=4, columnspan=2)

# Ejecutar el bucle de la ventana
ventana.mainloop()

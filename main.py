import numpy as np
import matplotlib.pyplot as plt

# Constante de Coulomb
K = 8.99e9  # N·m²/C²

def calcular_fuerza(Q1, Q2, x2, y2):
    r = np.array([x2, y2])
    r_magnitud = np.linalg.norm(r)

    if r_magnitud == 0:
        raise ValueError("Las cargas no pueden estar en la misma posición.")

    fuerza_magnitud = K * Q1 * Q2 / r_magnitud**2
    fuerza_vector = fuerza_magnitud * (r / r_magnitud)

    return fuerza_vector

def graficar(Q1, Q2, x2, y2, fuerza_vector):
    plt.figure(figsize=(6,6))
    plt.quiver(0, 0, x2, y2, angles='xy', scale_units='xy', scale=1, color='blue', label='Vector posición Q2')
    plt.scatter(0, 0, color='red', label='Q1 (en el origen)')
    plt.scatter(x2, y2, color='green', label='Q2')
    plt.quiver(x2, y2, fuerza_vector[0], fuerza_vector[1], angles='xy', scale_units='xy', scale=1, color='purple', label='Fuerza sobre Q2')
    
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid()
    plt.legend()
    plt.title('Fuerza eléctrica entre dos cargas')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

try:
    Q1 = float(input("Ingrese la carga Q1 (en Coulombs): "))
    Q2 = float(input("Ingrese la carga Q2 (en Coulombs): "))
    x2 = float(input("Ingrese la coordenada X de Q2: "))
    y2 = float(input("Ingrese la coordenada Y de Q2: "))

    fuerza = calcular_fuerza(Q1, Q2, x2, y2)
    print(f"El vector de fuerza sobre Q2 es: {fuerza} N")

    graficar(Q1, Q2, x2, y2, fuerza)

except ValueError as e:
    print("Error:", e)

import numpy as np

# Definición de la función y su derivada
fx  = lambda x: np.exp(x**2) * x - 4  # Función f(x) = e^(x^2) * x - 4
dfx = lambda x: np.exp(x**2) * (2*x**2 + 1)  # Derivada f'(x) = e^(x^2) * (2x^2 + 1)

x0 = 2          # Valor inicial
tolera = 0.0000001 # Tolerancia

# PROCEDIMIENTO
tabla = []
tramo = abs(2*tolera)  # Inicialización del tramo
xi = x0
iteraciones = 0

print(f"{'Iteración':<10} {'xi':<15} {'xnuevo':<15} {'tramo':<15}")
while tramo >= tolera:
    xnuevo = xi - fx(xi) / dfx(xi)  # Fórmula de Newton-Raphson
    tramo = abs(xnuevo - xi)        # Cálculo del tramo
    tabla.append([xi, xnuevo, tramo])  # Guardar valores en la tabla
    
    print(f"{iteraciones:<10} {xi:<15.10f} {xnuevo:<15.10f} {tramo:<15.10f}")
    
    xi = xnuevo  # Actualizar xi
    iteraciones += 1

# convierte la lista a un arreglo.
tabla = np.array(tabla)

# SALIDA
print(f"\nLa raíz aproximada es: {xi}")
print(f"Se realizaron {iteraciones} iteraciones.")
print(f"Con un error de: {tramo}")

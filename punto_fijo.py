import numpy as np
import matplotlib.pyplot as plt

# DEFINICIÓN DE LA FUNCIÓN ORIGINAL
# f(x) = x * 2^x - 1
fx = lambda x: x * 2**x - 1

# DEFINICIÓN DE LA FUNCIÓN DE ITERACIÓN (gx)
# gx(x) = 1 / 2^x
gx = lambda x: 1 / (2**x)

# INTERVALO INICIAL
a = 0  # Límite inferior del intervalo
b = 1  # Límite superior del intervalo

# CRITERIO DE PARADA
error = 0.000001 # Tolerancia para el error

# INICIALIZACIÓN DE VARIABLES
xn_1 =  (a + b) / 2 # Valor inicial del punto anterior (punto medio del intervalo (a + b) / 2 o 0)
error_absoluto = np.inf  # Error absoluto inicial (infinito para comenzar)
error_relativo = np.inf  # Error relativo inicial (infinito para comenzar)
iteraciones = 0  # Contador de iteraciones

# Variables de control para los criterios de convergencia
converge_abs = False
converge_rel = False

# CABECERA DE LA TABLA DE RESULTADOS
print(f"{'Iteración':<10} {'xi':<20} {'xnuevo':<20} {'Err. Abs':<20} {'Err. Rel':<20} {'Conv. Abs':<20} {'Conv. Rel':<20}")
print(f"{iteraciones:<10} {xn_1:<20.10f} {'':<20} {'':<20} {'':<20} {'':<20}")

# CICLO DE ITERACIÓN DEL MÉTODO DE PUNTO FIJO
while not (converge_abs and converge_rel):
    xn = gx(xn_1)  # Calcula el nuevo valor usando la función de iteración gx

    # Calcula el error absoluto
    error_absoluto = abs(xn - xn_1)
    
    # Calcula el error relativo, manejando el caso donde xn podría ser cero
    if xn != 0:
        error_relativo = abs((xn - xn_1) / xn)
    else:
        error_relativo = np.inf  # Asignar infinito si xn es cero para evitar división por cero

    # Verifica si el error absoluto y relativo han convergido
    converge_abs = error_absoluto < error
    converge_rel = error_relativo < error

    # Muestra los resultados de la iteración actual con errores y su estado de convergencia
    print(f"{iteraciones:<10} {xn_1:<20.10f} {xn:<20.10f} {error_absoluto:<20.10f} {error_relativo:<20.10f} {'Sí' if converge_abs else 'No':<20} {'Sí' if converge_rel else 'No':<20}")

    # Actualiza el valor anterior para la siguiente iteración
    xn_1 = xn
    iteraciones += 1

# RESULTADOS FINALES
print(f"\nLa raíz aproximada es: {xn:.6f}")
print(f"Se realizaron {iteraciones} iteraciones.")
print(f"Error absoluto final: {error_absoluto:.6f}")
print(f"Error relativo final: {error_relativo:.6f}")

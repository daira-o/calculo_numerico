import numpy as np
import matplotlib.pyplot as plt

# DEFINICIÓN DE LA FUNCIÓN
# fx es la función f(x) = e^(x^2) * x - 4
fx = lambda x: (x-2)*(x+1)*x*((x-1)**3)*(x+2)
# INTERVALO INICIAL
# [a, b] es el intervalo en el que buscamos la raíz
a = -3 # Límite inferior del intervalo
b = -0.5  # Límite superior del intervalo
#convergencia en a),c),d)
# CRITERIO DE PARADA
tolera = 0.00001  # Tolerancia para el error
max_iter = 100  # Número máximo de iteraciones

# INICIALIZACIÓN DE VARIABLES
pn_anterior = (a + b) / 2  # Inicializamos con el punto medio
error_absoluto = b - a  # Tramo inicial (distancia entre a y b)
error_relativo = np.inf  # Error relativo inicial, definido como infinito
iteraciones = 0  # Contador de iteraciones

# Variables de control para los criterios de convergencia
converge_abs = False
converge_rel = False

# Cabecera de la tabla de resultados
print(f"{'Iteración':<10} {'a':<10} {'b':<10} {'pn':<10} {'f(pn)':<10} {'Err. Abs':<10} {'Err. Rel':<10} {'Conv. Abs':<10} {'Conv. Rel':<10}")

# CICLO DE BISECCIÓN
while not (converge_abs and converge_rel) and iteraciones < max_iter:
    # Punto medio del intervalo [a, b]
    pn = (a + b) / 2
    # Calculamos el valor de la función en los extremos y en el punto medio
    fa = fx(a)
    fb = fx(b)
    fpn = fx(pn)

    # Comprobamos el signo de f(a) * f(pn) para ver en qué subintervalo está la raíz
    cambia = np.sign(fa) * np.sign(fpn)

    if cambia < 0:
        # La raíz está en el subintervalo [a, pn], así que actualizamos b
        b = pn
    elif cambia > 0:
        # La raíz está en el subintervalo [pn, b], así que actualizamos a
        a = pn
    else:
        # Si f(pn) es exactamente 0, hemos encontrado la raíz exacta
        break

    # Actualizamos el error absoluto
    error_absoluto = abs(b - a)

    # Actualizamos el error relativo basado en la diferencia entre el valor actual y el anterior de pn
    if pn != 0:  # Para evitar división por cero
        error_relativo = abs((pn - pn_anterior) / pn)
    else:
        error_relativo = np.inf

    # Verificamos si el error absoluto ha convergido
    converge_abs = error_absoluto < tolera
    
    # Verificamos si el error relativo ha convergido
    converge_rel = error_relativo < tolera

    # Mostramos los resultados de la iteración actual con los errores y su estado de convergencia
    print(f"{iteraciones:<10} {a:<10.6f} {b:<10.6f} {pn:<10.6f} {fpn:<10.6f} {error_absoluto:<10.6f} {error_relativo:<10.6f} {'Si' if converge_abs else 'No':<10} {'Si' if converge_rel else 'No':<10}")

    # Actualizamos el valor anterior de pn para la siguiente iteración
    pn_anterior = pn

    # Incrementamos el contador de iteraciones
    iteraciones += 1

# RESULTADOS FINALES
print(f"\nLa raíz aproximada es: {pn}")
print(f"Se realizaron {iteraciones} iteraciones.")
print(f"Error absoluto final: {error_absoluto}")
print(f"Error relativo final: {error_relativo}")

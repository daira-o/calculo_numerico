import matplotlib as plt
# Algoritmo de Bisección
# [a,b] se escogen de la gráfica de la función
# error = tolera
import numpy as np
import matplotlib.pyplot as plt

# INGRESO
fx  = lambda x: np.exp(x**2) * x - 4  # Función f(x) = e^(x^2) * x - 4
a = 1
b = 2
tolera = 0.0001

# PROCEDIMIENTO
# Error absoluto
tramo = b - a
iteraciones = 0

# si es relativo
# tramo = (b - a) / a

print(f"{'Iteración':<10} {'a':<10} {'b':<10} {'pn':<10} {'f(pn)':<10} {'tramo':<10}")
while tramo >= tolera:
    pn = (a + b) / 2
    fa = fx(a)
    fb = fx(b)
    fpn = fx(pn)
    cambia = np.sign(fa) * np.sign(fpn)
    
    print(f"{iteraciones:<10} {a:<10.6f} {b:<10.6f} {pn:<10.6f} {fpn:<10.6f} {tramo:<10.6f}")
    
    if cambia < 0: 
        b = pn
    elif cambia > 0:
        a = pn
    else:
        break  # Si f(pn) es exactamente 0, hemos encontrado la raíz
    
    tramo = b - a
    # tramo = (b - a) / a  # Si es relativo
    iteraciones += 1

print(f"\nLa raíz aproximada es: {pn}")
print(f"Se realizaron {iteraciones} iteraciones.")


# SALIDA
print('       raiz en: ', pn)
print('error en tramo: ', tramo)
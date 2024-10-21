import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# INGRESO: Datos de prueba
xi = [-2,0,1]  # Puntos en el eje x
fi = [0,1,-1]  # Valores correspondientes en el eje y

# PROCEDIMIENTO
xi = np.array(xi, dtype=float)
fi = np.array(fi, dtype=float)

# Inicialización del polinomio de Lagrange
n = len(xi)
x = sym.Symbol('x')
polinomio = 0
divisorL = np.zeros(n, dtype=float)
L = []

# Construcción del polinomio de Lagrange
for i in range(n):
    numerador = 1
    denominador = 1
    for j in range(n):
        if j != i:
            numerador *= (x - xi[j])
            denominador *= (xi[i] - xi[j])
    terminoLi = numerador / denominador
    polinomio += terminoLi * fi[i]
    divisorL[i] = denominador
    L.append(terminoLi)

# Simplificación del polinomio
polisimple = polinomio.expand()

# Función para evaluación numérica del polinomio
px = sym.lambdify(x, polisimple)

# Puntos para la gráfica
muestras = 101
a = np.min(xi)
b = np.max(xi)
pxi = np.linspace(a, b, muestras)
pfi = px(pxi)

# SALIDA
print('Valores de fi:', fi)
print('Divisores en L(i):', divisorL)
print()
print('Polinomios L(i):')
for i in range(n):
    print(f'L{i} = {L[i]}')
print()
print('Polinomio de Lagrange (expresiones):')
print(polinomio)
print()
print('Polinomio de Lagrange (simplificado):')
print(polisimple)

# Gráfica
plt.plot(xi, fi, 'o', label='Puntos')
plt.plot(pxi, pfi, label='Polinomio')
plt.legend()
plt.xlabel('xi')
plt.ylabel('fi')
plt.title('Interpolación Lagrange')
plt.show()

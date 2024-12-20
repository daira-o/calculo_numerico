import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# INGRESO: Datos de entrada
xi = [1, 1.1, 1.3, 1.5, 1.9, 2.1]
yi = [1.84, 1.96, 2.21, 2.45, 2.94, 3.18]

# Convertir listas a arrays de numpy
xi = np.array(xi, dtype=float)
yi = np.array(yi, dtype=float)
n = len(xi)  # Número de datos

# Calcular sumatorias y medias
log_xi = np.log(xi)
log_yi = np.log(yi)
sx = np.sum(log_xi)   # Sumatoria de log(xi)
sy = np.sum(log_yi)   # Sumatoria de log(yi)
sxy = np.sum(log_xi * log_yi)  # Sumatoria de log(xi) * log(yi)
sx2 = np.sum(log_xi ** 2)  # Sumatoria de log(xi)^2

# Calcular coeficientes a y b para la regresión y = a * x^b
b = (n * sxy - sx * sy) / (n * sx2 - sx ** 2)  # Pendiente
a_log = (sy - b * sx) / n  # Intercepto en logaritmos
a = np.exp(a_log)  # Convertir el intercepto a la escala original

# Definir la ecuación de regresión: y = a * x^b
x = sym.Symbol('x')
f = a * x**b

# Convertir la función simbólica a una función numérica
fx = sym.lambdify(x, f)
fi = fx(xi)  # Valores ajustados

# Calcular el coeficiente de correlación en el espacio de logaritmos
numerador = n * sxy - sx * sy
raiz1 = np.sqrt(n * sx2 - sx ** 2)
raiz2 = np.sqrt(n * np.sum(log_yi ** 2) - sy ** 2)
r = numerador / (raiz1 * raiz2)

# Calcular el coeficiente de determinación
r2 = r ** 2
r2_porcentaje = np.around(r2 * 100, 2)

# Calcular el error cuadrático
error_cuad = np.sum((fi - yi) ** 2)
mse = np.mean((yi - fi) ** 2)

# SALIDA: Resultados
print('Ecuación de la curva de regresión: f(x) =', f)
print('Coeficiente de correlación (r) =', r)
print('Coeficiente de determinación (r^2) =', r2)
print('Error cuadrático =', error_cuad)
print('Error cuadrático medio =', mse)
print(f'{r2_porcentaje}% de los datos está descrito por el modelo de potencia')

# GRAFICA: Visualización de los datos y la curva de regresión
plt.plot(xi, yi, 'o', label='Datos (xi, yi)')
plt.plot(xi, fi, color='orange', label=f'Ecuación: {a:.3f} * x^{b:.3f}')

# Líneas de error
for i in range(n):
    y0 = np.min([yi[i], fi[i]])
    y1 = np.max([yi[i], fi[i]])
    plt.vlines(xi[i], y0, y1, color='red', linestyle='dotted')

plt.legend()
plt.xlabel('xi')
plt.title('Mínimos Cuadrados - Regresión de Potencia')
plt.show()

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# INGRESO: Datos de entrada
xi = [1, 2, 3, 4, 5, 6, 7,8,9,10]
yi = [1.3,3.5,4.2,5,7,8.8,10.1,12.5,13,15.6]

# Convertir listas a arrays de numpy
xi = np.array(xi, dtype=float)
yi = np.array(yi, dtype=float)
n = len(xi)  # Número de datos

# Calcular sumatorias y medias
xm = np.mean(xi)  # Media de xi
ym = np.mean(yi)  # Media de yi
sx = np.sum(xi)   # Sumatoria de xi
sy = np.sum(yi)   # Sumatoria de yi
sxy = np.sum(xi * yi)  # Sumatoria de xi * yi
sx2 = np.sum(xi ** 2)  # Sumatoria de xi^2
sy2 = np.sum(yi ** 2)  # Sumatoria de yi^2  

# Calcular coeficientes a y b para la recta de regresión y = a + b*x
b = (n * sxy - sx * sy) / (n * sx2 - sx ** 2)  # Pendiente
a = ym - b * xm  # Intercepto

# Definir el polinomio de grado 1
x = sym.Symbol('x')
f = a + b * x

# Convertir la función simbólica a una función numérica
fx = sym.lambdify(x, f)
fi = fx(xi)  # Valores ajustados

# Calcular el coeficiente de correlación
numerador = n * sxy - sx * sy
raiz1 = np.sqrt(n * sx2 - sx ** 2)
raiz2 = np.sqrt(n * sy2 - sy ** 2)
r = numerador / (raiz1 * raiz2)

# Calcular el coeficiente de determinación
r2 = r ** 2
r2_porcentaje = np.around(r2 * 100, 2)

#Calcular el error cuadrático
mse = np.mean((yi - fi) ** 2)
error_cuad = np.sum((fx(xi)-yi)**2)

# SALIDA: Resultados
print('Ecuación de la recta de regresión: f(x) =', f)
print('Coeficiente de correlación (r) =', r)
print('Coeficiente de determinación (r^2) =', r2)
print('Error cuadrático medio =', error_cuad)
print('Error cuadrático  =', mse)
print(f'{r2_porcentaje}% de los datos está descrito por el modelo lineal')

# GRAFICA: Visualización de los datos y la recta de regresión
plt.plot(xi, yi, 'o', label='Datos (xi, yi)')
plt.plot(xi, fi, color='orange', label=f'Ecuación: {f}')

# Líneas de error
for i in range(n):
    y0 = np.min([yi[i], fi[i]])
    y1 = np.max([yi[i], fi[i]])
    plt.vlines(xi[i], y0, y1, color='red', linestyle='dotted')

plt.legend()
plt.xlabel('xi')
plt.title('Mínimos Cuadrados - Regresión Lineal')
plt.show()

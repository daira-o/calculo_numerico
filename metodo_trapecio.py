# Integración: Regla de los trapecios
# Usando una función fx() definida por el usuario
import numpy as np

# INGRESO DE DATOS
# Definimos la función a integrar, en este caso e^(-x^2)
fx = lambda x: np.e ** (-x**2)

# Intervalo de integración
a = 0      # Límite inferior
b = 1      # Límite superior
tramos = 6 # Número de tramos o divisiones (deben ser equidistantes)

# PROCEDIMIENTO
# Regla del Trapecio usando tramos equidistantes en el intervalo [a, b]

# Calcula el tamaño del paso (h), es decir, la distancia entre puntos en x
h = (b - a) / tramos

# Inicializa las listas de valores xi y f(xi) para la tabla
xi_values = []
fx_values = []

# Inicia en el valor inferior a
xi = a
suma = fx(xi)

# Guarda los primeros valores de xi y f(xi)
xi_values.append(xi)
fx_values.append(fx(xi))

# Itera para cada tramo desde el segundo punto hasta el penúltimo punto
for i in range(0, tramos - 1, 1):
    # Avanza al siguiente punto en el eje x
    xi = xi + h
    # Guarda los valores de xi y f(xi)
    xi_values.append(xi)
    fx_values.append(fx(xi))
    # Suma el doble del valor de la función en este punto (por la regla del trapecio)
    suma = suma + 2 * fx(xi)

# Agrega el valor de fx en el último punto del intervalo (b)
xi_values.append(b)
fx_values.append(fx(b))
suma = suma + fx(b)

# Calcula el área aproximada bajo la curva usando la regla del trapecio
area = h * (suma / 2)

# SALIDA DE RESULTADOS
print('Tramos:', tramos)
print('Tabla de valores:')
print('xi\t\tf(xi)')
for x, fx_val in zip(xi_values, fx_values):
    print(f'{x:.4f}\t{fx_val:.4f}')  # Muestra xi y f(xi) con 4 decimales para claridad

print('Integral aproximada:', area)

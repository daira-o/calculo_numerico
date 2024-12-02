import numpy as np

def divided_diff(x, y):
    '''
    Función para calcular la tabla de diferencias divididas
    '''
    n = len(y)  # Número de puntos
    coef = np.zeros([n, n])  # Inicialización de la matriz de coeficientes con ceros
    coef[:, 0] = y  # La primera columna de coeficientes es igual a los valores de y
    
    # Rellenar la tabla de diferencias divididas
    for j in range(1, n):  # Recorrer columnas a partir de la segunda
        for i in range(n - j):  # Recorrer filas
            # Calcular el coeficiente usando la fórmula de diferencias divididas
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
    
    return coef  # Devolver la tabla de diferencias divididas completa

def newton_poly(coef, x_data, x):
    '''
    Evaluar el polinomio de Newton en el punto x
    '''
    n = len(x_data) - 1  # Índice del último coeficiente
    p = coef[n]  # Inicializar el valor del polinomio con el último coeficiente
    for k in range(1, n + 1):
        # Usar el método de Horner para construir el polinomio de Newton
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p  # Devolver el valor del polinomio en el punto x

# Puntos de datos conocidos
x = np.array([1.5, 2, 3, 3.5])
y = np.array([0.17609, 0.30103, 0.47712, 0.54407])

# Obtener los coeficientes de diferencias divididas
a_s = divided_diff(x, y)

# Imprimir la tabla de diferencias divididas
print("Tabla de Diferencias Divididas:")
print(a_s)

"""
# Evaluación en múltiples puntos nuevos
x_new = np.arange(-5, 2.1, 0.1)
y_new = newton_poly(a_s[0, :], x, x_new)

# Imprimir los nuevos puntos de datos
print("\nNuevos Puntos de Datos:")
for xi, yi in zip(x_new, y_new):
"""

# Evaluar el polinomio en un punto específico nuevo
x_new_point = 2.5
y_new_point = newton_poly(a_s[0, :], x, x_new_point)
print(f"\nEl valor del polinomio de Newton en x = {x_new_point} es y = {y_new_point:.2f}")

# Cálculo del error
# Logaritmo en base 10, ya que log por defecto es base e
y_error = np.log10(2.5)  # Valor real usando log base 10
y_abs_error = abs((y_error - y_new_point) / y_error)  # Error absoluto relativo
print(f"El error absoluto es: {y_abs_error:.4f}")

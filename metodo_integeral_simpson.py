import numpy as np  # Importamos la biblioteca numpy para trabajar con arreglos y funciones matemáticas.

def funcion_a_integrar(x):
    """Función a integrar: en este caso, el seno de x."""
    return np.sin(x)  # Retorna el valor de la función seno para el valor x.

def regla_simpson_13(func, a, b, tramos):
    """
    Calcula la integral definida de una función en el intervalo [a, b] 
    utilizando la regla de Simpson 1/3.

    Parámetros:
    func: función que se va a integrar.
    a: límite inferior de la integración.
    b: límite superior de la integración.
    tramos: número de tramos en los que se divide el intervalo (debe ser par).
    """
    # Verifica si el número de tramos es par, ya que la regla de Simpson 1/3
    # requiere un número par de tramos. Si no es par, lanza un error.
    if tramos % 2 != 0:
        raise ValueError("El número de tramos debe ser par para la regla de Simpson 1/3.")

    # Calcula el tamaño del paso, que es la distancia entre puntos en el eje x.
    h = (b - a) / tramos

    # Genera una lista de puntos equiespaciados en el intervalo [a, b].
    xi = np.linspace(a, b, tramos + 1)

    # Calcula la integral usando la fórmula de Simpson 1/3.
    # Suma las áreas bajo la curva dividiendo en tramos de 3 puntos consecutivos:
    # - El primer y último punto de cada tramo se multiplican por 1.
    # - El punto intermedio de cada tramo se multiplica por 4.
    delta_areas = (h / 3) * np.sum([
        func(xi[i]) + 4 * func(xi[i + 1]) + func(xi[i + 2])
        for i in range(0, tramos, 2)
    ])
    integral_cuarta = 1
    error = -(b-a)/180*h**4*integral_cuarta

    return delta_areas, error  # Retorna el valor aproximado de la integral.

# INGRESO DE DATOS
a = 0              # Límite inferior de integración.
b = np.pi / 2      # Límite superior de integración.
tramos = 6         # Número de tramos (debe ser par).

# CÁLCULO DE LA INTEGRAL
area,error = regla_simpson_13(funcion_a_integrar, a, b, tramos)

# SALIDA DE RESULTADOS
print(f'Número de tramos: {tramos}')
print(f'Integral con regla de Simpson 1/3: {area}')
print(f'Error: {error}')

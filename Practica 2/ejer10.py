import numpy as np
import matplotlib.pyplot as plt

# DEFINICIÓN DE LA FUNCIÓN ORIGINAL
fx = lambda x: (x**2-1)/3

# DEFINICIÓN DE LA FUNCIÓN DE ITERACIÓN (gx)
gx = lambda x: (x**2-1)/3

# INTERVALO INICIAL
a = -1  # Límite inferior del intervalo
b = 1  # Límite superior del intervalo

# CRITERIO DE PARADA
error = 0.0001  # Tolerancia para el error
max_iter = 100  # Máximo número de iteraciones permitidas

# INICIALIZACIÓN DE VARIABLES
xn_1 = 0  # Valor inicial
error_absoluto = np.inf  # Error absoluto inicial
error_relativo = np.inf  # Error relativo inicial
iteraciones = 0  # Contador de iteraciones

# Variables de control para los criterios de convergencia
converge_abs = False
converge_rel = False

# CABECERA DE LA TABLA DE RESULTADOS
print(f"{'Iteración':<10} {'xi':<20} {'xnuevo':<20} {'Err. Abs':<20} {'Err. Rel':<20} {'Conv. Abs':<20} {'Conv. Rel':<20}")
print(f"{iteraciones:<10} {xn_1:<20.10f} {'':<20} {'':<20} {'':<20} {'':<20}")

# CICLO DE ITERACIÓN DEL MÉTODO DE PUNTO FIJO
while not (converge_abs and converge_rel) and iteraciones < max_iter:
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
if iteraciones < max_iter:
    print(f"\nLa raíz aproximada (punto fijo) es: {xn:.6f}")
    print(f"Se realizaron {iteraciones} iteraciones.")
    print(f"Error absoluto final: {error_absoluto:.6f}")
    print(f"Error relativo final: {error_relativo:.6f}")

    # Verificación: evaluamos f(x) para comprobar que f(x) ≈ x
    fx_verificado = fx(xn)
    print(f"\nVerificación: f(x) = {fx_verificado:.6f}, x = {xn:.6f}")
    if np.isclose(fx_verificado, xn, atol=error):
        print("La verificación es correcta: f(x) ≈ x dentro de la tolerancia.")
    else:
        print("La verificación falló: f(x) no es aproximadamente igual a x dentro de la tolerancia.")
else:
    print("\nEl método no converge dentro del número máximo de iteraciones permitido.")
    print(f"Se alcanzaron {max_iter} iteraciones sin cumplir los criterios de parada.")

# GRAFICACIÓN DE f(x) Y EL PUNTO FIJO
x_vals = np.linspace(0, 2 * np.pi, 1000)
y_vals = fx(x_vals)

plt.plot(x_vals, y_vals, label="f(x)")
plt.plot(x_vals, x_vals, label="y = x", linestyle="--")
plt.scatter([xn], [xn], color='red', label=f'Punto fijo (x = {xn:.4f})')
plt.title("Visualización del punto fijo")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()

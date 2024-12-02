import numpy as np

# DEFINICIÓN DE LA FUNCIÓN Y SU DERIVADA
# f(x) = e^(x^2) * x - 4
# Derivada f'(x) = e^(x^2) * (2x^2 + 1)
fx = lambda x: np.cos(x)**2-3*x
dfx = lambda x: -2*np.cos(x)*np.sin(x)-3

# VALOR INICIAL Y TOLERANCIA
x0 = np.pi/6         # Valor inicial para la aproximación de la raíz
tolera = 0.0005  # Tolerancia para el criterio de parada

# INICIALIZACIÓN DE VARIABLES
xi = x0             # Valor inicial de xi
tramo = abs(2 * tolera)  # Inicialización del error (tramo) para entrar al ciclo
error_absoluto = np.inf  # Inicialización del error absoluto
error_relativo = np.inf  # Inicialización del error relativo
iteraciones = 0     # Contador de iteraciones

# LISTA PARA ALMACENAR RESULTADOS
tabla = []

# CABECERA DE LA TABLA DE RESULTADOS
print(f"{'Iteración':<10} {'xi':<20} {'xnuevo':<20} {'Err. Abs':<20} {'Err. Rel':<20} {'Conv. Abs':<20} {'Conv. Rel':<20}")
print(f"{iteraciones:<10} {xi:<20.10f} {'':<20} {'':<20} {'':<20} {'':<20}")

# CICLO DE ITERACIÓN DEL MÉTODO DE NEWTON-RAPHSON
while not (error_absoluto < tolera and error_relativo < tolera):
    # Calcula el nuevo valor usando la fórmula de Newton-Raphson
    xnuevo = xi - fx(xi) / dfx(xi)
    
    # Calcula el error absoluto y relativo
    error_absoluto = abs(xnuevo - xi)
    if xnuevo != 0:
        error_relativo = abs((xnuevo - xi) / xnuevo)
    else:
        error_relativo = np.inf  # Evita división por cero si xnuevo es cero
    
    # Verifica si ambos errores han convergido
    converge_abs = error_absoluto < tolera
    converge_rel = error_relativo < tolera
    
    # Guarda los resultados en la tabla
    tabla.append([xi, xnuevo, error_absoluto, error_relativo, 'Sí' if converge_abs else 'No', 'Sí' if converge_rel else 'No'])
    
    # Muestra los resultados de la iteración actual
    print(f"{iteraciones:<10} {xi:<20.10f} {xnuevo:<20.10f} {error_absoluto:<20.10f} {error_relativo:<20.10f} {'Sí' if converge_abs else 'No':<20} {'Sí' if converge_rel else 'No':<20}")

    # Actualiza el valor de xi para la siguiente iteración
    xi = xnuevo
    iteraciones += 1

# Convierte la lista a un arreglo para futuras manipulaciones si es necesario
tabla = np.array(tabla)

# RESULTADOS FINALES
print(f"\nLa raíz aproximada es: {xi:.10f}")
print(f"Se realizaron {iteraciones} iteraciones.")
print(f"Error absoluto final: {error_absoluto:.10f}")
print(f"Error relativo final: {error_relativo:.10f}")

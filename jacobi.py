import numpy as np
import pandas as pd

# Definir el sistema de ecuaciones Ax = b
A = np.array([[10, -1, 2, 0], [-1, 11, -1, 3], [2, -1, 10, -1], [0, 3, -1, 8]], dtype=float)
b = np.array([6, 25, -11, 15], dtype=float)

# Inicializar el vector solución inicial con ceros, del mismo tamaño que el vector b
x = np.zeros_like(b)

# Definir el número máximo de iteraciones y la tolerancia
max_iter = 100
tolerance = 0.01

# Función que implementa el método de Jacobi
def jacobi(A, b, x0, tolerance, max_iter):
    # Verificar si el determinante de A es distinto de 0
    det_A = np.linalg.det(A)
    if det_A == 0:
        raise ValueError("El sistema no tiene una solución única, el determinante de A es cero.")
    
    # Verificar si el sistema es diagonalmente dominante
    n = len(b)
    diag_dom = True
    for i in range(n):
        # Verificar que la suma de los coeficientes no diagonales sea menor que el coeficiente diagonal
        sum_non_diag = np.sum(np.abs(A[i, :])) - np.abs(A[i, i])
        if np.abs(A[i, i]) <= sum_non_diag:
            diag_dom = False
            break
    if not diag_dom:
        raise ValueError("El sistema no es diagonalmente dominante, lo que podría afectar la convergencia del método de Jacobi.")

    # Inicializar el vector para almacenar la solución nueva en cada iteración
    x_new = np.copy(x0)
    
    # Crear listas para almacenar los datos por iteración
    iteraciones = []
    soluciones_actuales = []
    errores_absolutos = []
    errores_relativos = []
    convergido_absoluto = []
    convergido_relativo = []
    
    # Iniciar el proceso iterativo
    for k in range(max_iter):
        # Copiar el valor actual de x_new para almacenarlo como la solución anterior (x_old)
        x_old = np.copy(x_new)
        
        # Iterar sobre cada ecuación (o fila de la matriz A)
        for i in range(n):
            # Calcular la suma de los productos de los coeficientes y las soluciones
            # anteriores, excluyendo el elemento diagonal A[i, i]
            sum_ = np.dot(A[i, :], x_old) - A[i, i] * x_old[i]
            
            # Actualizar el valor de x_new[i] usando la fórmula de Jacobi
            x_new[i] = (b[i] - sum_) / A[i, i]
        
        # Calcular el error absoluto como la norma infinita de la diferencia absoluta
        error_absoluto = np.linalg.norm(x_new - x_old, ord=np.inf)
        
        # Calcular el error relativo para cada componente, evitando la división por cero
        errores_relativos_componente = np.abs((x_new - x_old) / np.where(x_new != 0, x_new, 1))
        error_relativo = np.max(errores_relativos_componente)
        
        # Almacenar los datos de la iteración
        iteraciones.append(k + 1)
        soluciones_actuales.append([f'{xi:.9f}' for xi in x_new])
        errores_absolutos.append(f'{error_absoluto:.9f}')
        errores_relativos.append(f'{error_relativo:.9f}')
        
        # Determinar si ha convergido
        convergido_absoluto.append('Sí' if error_absoluto < tolerance else 'No')
        convergido_relativo.append('Sí' if error_relativo < tolerance else 'No')
        
        # Verificar si el error absoluto o relativo es menor que la tolerancia
        if error_absoluto < tolerance and error_relativo < tolerance:
            print(f"Convergencia alcanzada después de {k+1} iteraciones.")
            # Retornar la solución junto con los errores registrados
            return np.array(soluciones_actuales[-1]), iteraciones, soluciones_actuales, errores_absolutos, errores_relativos, convergido_absoluto, convergido_relativo
    
    # Si se alcanzan las iteraciones máximas sin convergencia, informarlo
    print("Se alcanzó el número máximo de iteraciones sin convergencia")
    return np.array(soluciones_actuales[-1]), iteraciones, soluciones_actuales, errores_absolutos, errores_relativos, convergido_absoluto, convergido_relativo

# Ejecutar el método de Jacobi
try:
    solucion, iteraciones, soluciones_actuales, errores_absolutos, errores_relativos, convergido_absoluto, convergido_relativo = jacobi(A, b, x, tolerance, max_iter)
    
    # Crear una tabla con toda la información por iteración
    df_resultados = pd.DataFrame({
        'Iteración': iteraciones,
        'Solución Actual': [' '.join(sa) for sa in soluciones_actuales],
        'Error Absoluto': errores_absolutos,
        'Error Relativo': errores_relativos,
        'Convergido Absoluto': convergido_absoluto,
        'Convergido Relativo': convergido_relativo
    })
    
    # Mostrar la tabla de resultados
    print("\nTabla de resultados:")
    print(df_resultados.to_string(index=False))

except ValueError as e:
    print(e)

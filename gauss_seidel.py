import numpy as np
import pandas as pd

def gauss_seidel(A, b, tol=0.01, max_iter=1000):
    """
    Resuelve el sistema de ecuaciones Ax = b usando el método de Gauss-Seidel y retorna un DataFrame con el historial de iteraciones.
    
    Parámetros:
    A -- Matriz de coeficientes (2D numpy array) de tamaño n x n
    b -- Vector de términos independientes (1D numpy array) de tamaño n
    tol -- Tolerancia para el criterio de convergencia (por defecto 1e-10)
    max_iter -- Número máximo de iteraciones (por defecto 1000)
    
    Retorna:
    df -- DataFrame con el historial de iteraciones, errores y convergencia
    """
    n = len(b)  # Número de variables (dimensión del sistema)
    
    x = np.zeros(n)  # Vector de soluciones inicializado en ceros
    history = []  # Lista para almacenar el historial de iteraciones
    
    # Iteraciones del método de Gauss-Seidel
    for k in range(max_iter):
        x_old = np.copy(x)  # Guardar la solución anterior para comparar
        
        # Actualización de cada componente del vector solución
        for i in range(n):
            # Suma de los términos de la izquierda del componente actual
            sum1 = np.dot(A[i, :i], x[:i])
            # Suma de los términos de la derecha del componente actual
            sum2 = np.dot(A[i, i+1:], x_old[i+1:])
            # Cálculo del nuevo valor del componente i
            x[i] = (b[i] - sum1 - sum2) / A[i, i]
        
        # Cálculo de errores
        abs_error = np.linalg.norm(x - x_old, ord=np.inf)  # Error absoluto (norma infinito de la diferencia)
        rel_error = abs_error / np.linalg.norm(x, ord=np.inf) if np.linalg.norm(x, ord=np.inf) != 0 else np.inf  # Error relativo
        
        # Verificar si la solución cumple con el criterio de convergencia
        converged_abs = abs_error < tol  # Verificación del criterio de convergencia basado en error absoluto
        converged_rel = rel_error < tol  # Verificación del criterio de convergencia basado en error relativo
        
        # Almacenar los resultados de la iteración actual en la lista de historial
        history.append([k + 1] + x.tolist() + [abs_error, rel_error, converged_abs, converged_rel])
        
        # Si la solución cumple con ambos criterios de convergencia, finalizar las iteraciones
        if converged_abs and converged_rel:
            print(f"Convergencia alcanzada después de {k+1} iteraciones.")
            break
    
    # Crear DataFrame con el historial de iteraciones para una presentación clara
    columns = ["Iteración"] + [f"x{i+1}" for i in range(n)] + ["Error Absoluto", "Error Relativo", "Convergencia Absoluta", "Convergencia Relativa"]
    df = pd.DataFrame(history, columns=columns)
    
    # Configurar pandas para mostrar números en formato decimal en lugar de notación científica
    pd.set_option('display.float_format', '{:.10f}'.format)
    
    return df

# Ejemplo de uso
A = np.array([[10, -1, 2, 0], [-1, 11, -1, 3], [2, -1, 10, -1], [0, 3, -1, 8]], dtype=float)
b = np.array([6, 25, -11, 15], dtype=float)

# Llamar a la función y almacenar el resultado en un DataFrame
df_resultado = gauss_seidel(A, b)
print(df_resultado)

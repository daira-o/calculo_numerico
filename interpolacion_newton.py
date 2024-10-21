import numpy as np

def divided_diff(x, y):
    '''
    Function to calculate the divided differences table
    '''
    n = len(y)
    coef = np.zeros([n, n])
    # the first column is y
    coef[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
    
    return coef

def newton_poly(coef, x_data, x):
    '''
    Evaluate the newton polynomial at x
    '''
    n = len(x_data) - 1 
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p

# Data points
x = np.array([1.5, 2, 3, 3.5])
y = np.array([0.17609, 0.30103, 0.47712, 0.54407])

# Get the divided difference coefficients
a_s = divided_diff(x, y)

# Print the divided differences table
print("Divided Differences Table:")
print(a_s)

"""
# Evaluate on new data points
x_new = np.arange(-5, 2.1, 0.1)
y_new = newton_poly(a_s[0, :], x, x_new)

# Print the new data points
print("\nNew Data Points:")
for xi, yi in zip(x_new, y_new):
"""
# Evaluate the polynomial at a specific new point
x_new_point = 2.5
y_new_point = newton_poly(a_s[0, :], x, x_new_point)
print(f"\nEl valor del polinomio de Newton en x = {x_new_point} es y = {y_new_point:.2f}")

#Error
#Log en base 10, log solo es en base e
y_error = np.log10(2.5)
y_abs_error = abs((y_error - y_new_point)/y_error)
print(f"El error absoluto es: {y_abs_error:.4f}")
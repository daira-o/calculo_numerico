import numpy as np
import matplotlib.pyplot as plt

fx  = lambda x: x*2**x-1
gx = lambda x: 1/2**x

a = 0
b = 1

error = 0.000001

xn_1 = (a + b) / 2
tramo = abs(2 * error)
iteraciones = 0

print(f"{'Iteración':<10} {'xi':<20} {'xnuevo':<20} {'tramo':<20}")
print(f"{iteraciones:<10} {xn_1:<20.10f} {'':<20} {'':<20}")

while tramo >= error:
    xn = gx(xn_1)
    tramo = abs(xn - xn_1)
    iteraciones += 1
    print(f"{iteraciones:<10} {xn_1:<20.10f} {xn:<20.10f} {tramo:<20.10f}")
    xn_1 = xn

print(f"Total de iteraciones: {iteraciones}")

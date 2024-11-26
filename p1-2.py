import sys
import matplotlib.pyplot as plt
from plot import plot1D, plot2D



if len(sys.argv) < 3:
    print("Uso: python p1-2.py <archivo_salida_1D> <archivo_salida_2D>")
    sys.exit(1)

output_file_1d = sys.argv[1]
output_file_2d = sys.argv[2]


t1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
x1 = [0, 1, -1, 1, -1, 1, -1, 1, -1]

t2 = [0.0, 0.33, 0.66, 0.99, 1.32, 1.65, 1.98, 2.31, 2.64, 2.98, 3.31, 3.64, 3.97, 4.3, 4.63, 4.96, 5.29, 5.62, 5.95, 6.28]
x2 = [1.0, 0.95, 0.79, 0.55, 0.25, -0.08, -0.4, -0.68, -0.88, -0.99, -0.99, -0.88, -0.68, -0.4, -0.08, 0.25, 0.55, 0.79, 0.95, 1.0]
y2 = [0.00e+00, 3.25e-01, 6.14e-01, 8.37e-01, 9.69e-01, 9.97e-01, 9.16e-01, 7.36e-01, 4.76e-01, 1.65e-01, -1.65e-01, -4.76e-01, -7.36e-01, -9.16e-01, -9.97e-01, -9.69e-01, -8.37e-01, -6.14e-01, -3.25e-01, -2.45e-16]

plot1D(t1, x1, "Tiempo (t)", "Posición (x)", output_file_1d)
plot2D(t2, x2, y2, "Tiempo (t)", "Posición (x)", output_file_2d)

# Importar las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Definir los datos de entrada (x) y salida (y)
x = np.array([2, 3, 4, 5, 6, 7, 7, 8, 9, 11, 12]).reshape(-1, 1)
y = np.array([18, 16, 15, 17, 20, 23, 25, 28, 31, 30, 29])

# Crear un objeto de regresión lineal
lin_reg = LinearRegression()

# Ajustar el modelo lineal a los datos
lin_reg.fit(x, y)

# Obtener los coeficientes del modelo lineal
intercept = lin_reg.intercept_
slope = lin_reg.coef_[0]

# Calcular los valores predichos por el modelo lineal
y_pred_lin = intercept + slope * x

# Crear un objeto de transformación polinomial de grado 2
poly_reg = PolynomialFeatures(degree=2)

# Transformar los datos de entrada en características polinomiales
x_poly = poly_reg.fit_transform(x)

# Ajustar el modelo polinomial a los datos transformados
lin_reg.fit(x_poly, y)

# Obtener los coeficientes del modelo polinomial
intercept_poly = lin_reg.intercept_
coeffs_poly = lin_reg.coef_

# Calcular los valores predichos por el modelo polinomial
y_pred_poly = intercept_poly + coeffs_poly[1] * x + coeffs_poly[2] * x**2

# Graficar los datos y los modelos ajustados
plt.scatter(x, y, color='blue', label='Datos')
plt.plot(x, y_pred_lin, color='red', label='Modelo lineal')
plt.plot(x, y_pred_poly, color='green', label='Modelo polinomial')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
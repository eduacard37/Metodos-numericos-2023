import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sympy import *

st.markdown("# Ajuste de curvas e interpolación 💻")
st.sidebar.markdown("# Método Interpolación Lagrange 💻")

# Configuración de la página
st.markdown("## Visualizador de Método Interpolación de Lagrange 📈")
st.image("https://th.bing.com/th/id/R.98d2012329e73062990bb9db05d79817?rik=4yLqZS8Tq8Y1xA&riu=http%3a%2f%2fblog.espol.edu.ec%2fanalisisnumerico%2ffiles%2f2017%2f12%2finterpolalagrange01.png&ehk=Cu0IpXw4Xp6cS4U5QjZdlRxDF0svUWtyFYqL6zt0wNo%3d&risl=&pid=ImgRaw&r=0",width=400)
st.write("Esta aplicación muestra la gráfica de interpolacion de Lagrange")

# Definir el rango de entrada
start_range = st.sidebar.slider("Inicio del rango", -10.0, 10.0, 0.1)
end_range = st.sidebar.slider("Fin del rango", -10.0, 10.0, 2.0)

# Indicar la ubicación de los archivos
data = st.file_uploader("Cargar archivo .CSV ✏️",type='csv')

# Importar los datos
df = pd.read_csv(data)

# Espacio reservado para la figura
fig_placeholder = st.empty()
tablita = st.empty()

x_values = np.array(df["X"])
y_values = np.array(df["Y"])

x = symbols('x')
Px = 0  # Inicializamos el polinomio interpolante

Px_data = []
for i in range(len(x_values)):
    Li = 1
    for j in range(len(x_values)):
        if i != j:
            Li *= (x - x_values[j]) / (x_values[i] - x_values[j])
    Px += y_values[i] * Li

    Px_data.append(simplify(Px))

#Agregamos la nueva columna al dataframe
df['P(x)'] = Px_data

# Simplificamos el polinomio
Px_simplified = simplify(Px)

# Creamos una función numérica a partir del polinomio simplificado
Px_lambda = lambdify(x, Px_simplified, "numpy")

# Crear un rango de valores para x
x_range = np.linspace(min(x_values), max(x_values), 400)

# Calcular los valores correspondientes en y
y_range = Px_lambda(x_range)

# Graficar los datos originales y el polinomio interpolado
fig, ax = plt.subplots()
ax.plot(x_values, y_values, 'ro', label='data')
ax.plot(x_range, y_range, label='Lagrange')
ax.set_title('Interpolación de Lagrange')
ax.grid(True)
ax.legend()

#Mostrar la figura en el espacio reservado
fig_placeholder.pyplot(fig)
tablita.dataframe(df)
    
# Borra la figura para la siguiente iteración
plt.close(fig)
import streamlit as st
import sympy as sp
import numpy as np
import pandas as pd

st.markdown("# Métodos diferenciación e integración 💻")
st.sidebar.markdown("# Método Euler 💻")

# Configuración de la página
st.markdown("## Visualizador de Método Euler 📈")
st.image("https://www.lifeder.com/wp-content/uploads/2019/05/Euler1.jpg",width=400)
st.write("Esta aplicación muestra la gráfica de Euler")

# Definir el rango de entrada
start_range = st.sidebar.slider("Inicio del rango", -10.0, 10.0, -2.0)
end_range = st.sidebar.slider("Fin del rango", -10.0, 10.0, 2.0)

# Ingresar la función
var = st.text_input("Variable ✏️", "t")
t = sp.symbols(var)
dy = st.text_input("Función derivada ✏️", "3*t**2")
dy = sp.sympify(dy)

# Ingresar los límites y tolerancia
y0 = st.number_input("Condición inicial y(0) ✏️", -10, 10, 0, 1)
h = st.number_input("Paso de integración (h) ✏️", 0.1, 10.0, 0.2, 0.1)

#definimos la funcion
y_real = sp.integrate(dy)

# Definimos los vectores donde almacenaremos el resultado.
x = np.arange(start_range, end_range + h, h)
y = np.empty_like(x)
y_r = np.empty_like(x)
y[0] = y0

# Dataframe para almacenar los resultados
columnas = ['it','t','yi','yi+1']
tabla = pd.DataFrame(columns=columnas)

# Espacio reservado para la figura
fig_placeholder = st.empty()
tablita = st.empty()

for i in range(0,len(y)-1):
  y[i+1] = y[i] + h * dy.subs({t:x[i]})
  y_r[i] = y_real.subs({t:x[i]})
  nueva_fila = pd.DataFrame(data={'it':[i+1],'t':[round(x[i],2)],'yi':[round(y[i],2)],"yi+1":[round(y[i+1],2)]})
  tabla = pd.concat([tabla,nueva_fila], ignore_index=True)
tabla.head()
y_r[-1] = y_real.subs({t:x[-1]})

import matplotlib.pyplot as plt
plt.figure()
fig, ax = plt.subplots()
ax.plot(x,y, marker='o', label ="Metodo Euler")
ax.plot(x,y_r, label='Valor real: {}'.format(f"${sp.latex(y_real)}$"))
ax.set_title("Método Euler")
ax.grid()
ax.legend()

# Ejes coordenados
x_min, x_max = ax.get_xlim()
y_min, y_max = ax.get_ylim()

# Graficar las líneas de los ejes
plt.plot([x_min, x_max], [0, 0], color='black')
plt.plot([0, 0], [y_min, y_max], color='black')

# Mostrar la figura en el espacio reservado
fig_placeholder.pyplot(fig)
tablita.dataframe(tabla)
  
# Borra la figura para la siguiente iteración
plt.close(fig)
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import pandas as pd

st.markdown("# Métodos abiertos 💻")
st.sidebar.markdown("# Método Secante modificado 💻")

# Configuración de la página
st.markdown("## Visualizador de Método Secante modificado 📈")
st.image("https://www.geogebra.org/resource/gtuVuStu/BpQjxRW058XnPhpr/material-gtuVuStu-thumb@l.png",width=400)
st.write("Esta aplicación muestra la gráfica de la secante modificada")

# Definir el rango de entrada
start_range = st.sidebar.slider("Inicio del rango", -10.0, 10.0, 0.1)
end_range = st.sidebar.slider("Fin del rango", -10.0, 10.0, 2.0)

# Ingresar la función
var = st.text_input("Variable ✏️", "x")
x = sp.symbols(var)
funcion = st.text_input("Función ✏️", "E**(-x)-x")
y = sp.sympify(funcion)

# Ingresar los límites y tolerancia
xi = st.number_input("Xi ✏️", -10.0, 10.0, 0.0, 0.1)
delta = st.number_input("Delta ✏️", 0.01, 1.0, 0.1, 0.01)
tol = st.number_input("Tolerancia ✏️", 0.1, 10.0, 0.1, 0.1)
max_iter = st.number_input("Máximas iteraciones ✏️", 1, 300, 100, 1)

er = tol+1
it = 1
r = np.linspace(start_range,end_range, 100)

# Dataframe para almacenar los resultados
columnas = ['xi','Xi+d','f(xi)','f(Xi+d)','er(%)']
tabla = pd.DataFrame(columns=columnas)

# Espacio reservado para la figura
fig_placeholder = st.empty()
tablita = st.empty()

while er > tol and it < max_iter:
  fxi=round(y.subs({x:xi}),4)
  fxi_d=round(y.subs({x:xi+delta}),4)

  # Crear la figura
  plt.figure()
  fig, ax = plt.subplots()

  fx = [y.subs({x:x_i}) for x_i in r]
  ax.plot(r,fx,color='blue',label=f"${sp.latex(y)}$")

  ## Plano cartesiano (Ejes)
  ax.vlines(x=0,ymin=min(fx)-0.1,ymax=max(fx)+0.1,color='k')
  ax.hlines(y=0,xmin=min(r)-0.1,xmax=max(r)+0.1,color='k')

  ## Punto inicial
  ax.plot([xi],[fxi], color='red', marker='o', label=f'$(x_{it},f(x_{it}))= ({xi},{fxi})$')

  ## Calculemos el x_i+1 siguiente
  xs = round(xi - ((fxi * delta) / (fxi_d - fxi)),4)
  ax.plot([xs],[0], color='red', marker='x', label=f'$(x_{it+1},0) = ({xs},0)$')

  ## Pintar la recta secante
  #y0 = f(x0)
  #y1 = f(x1)
  #ax.plot([x0, x1], [y0, y1], color='purple',linestyle='--')

  ##titulo de la grafica
  ax.set_title(f"${sp.latex(y)}$")
  ax.grid()
  plt.xlabel("x")
  plt.ylabel("y")
  ax.legend()
  plt.show()

  ## Calculo del error
  er = np.abs((xs-xi)/(xs)) * 100

  ## Actualicemos la tabla de iteraciones
  nueva_fila = {'xi':xi,'Xi+d':round(xi+delta,4),'f(xi)':fxi,"f(Xi+d)":fxi_d,'er(%)':round(er,4)}
  nueva_fila = pd.DataFrame([nueva_fila])
  tabla = pd.concat([tabla, nueva_fila], ignore_index=True)

  #Actualizamos la iteración y el valor de x actual (xi)
  it += 1
  xi = xs


  # Mostrar la figura en el espacio reservado
  fig_placeholder.pyplot(fig)
  tablita.dataframe(tabla)
    
  # Borra la figura para la siguiente iteración
  plt.close(fig)

st.success(f"La raíz está en: ({round(xi,4)}, {round(fxi,4)})")
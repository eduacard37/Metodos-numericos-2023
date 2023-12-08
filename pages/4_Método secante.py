import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import pandas as pd

st.markdown("# Métodos abiertos 💻")
st.sidebar.markdown("# Método Secante 💻")

# Configuración de la página
st.markdown("## Visualizador de Método Secante 📈")
st.image("https://blogsandralcaraz.files.wordpress.com/2017/03/secante.png?w=640",width=400)
st.write("Esta aplicación muestra la gráfica de la Secante")

# Definir el rango de entrada
start_range = st.sidebar.slider("Inicio del rango", -10.0, 10.0, 0.1)
end_range = st.sidebar.slider("Fin del rango", -10.0, 10.0, 2.0)

# Ingresar la función
var = st.text_input("Variable ✏️", "x")
x = sp.symbols(var)
func = st.text_input("Función ✏️", "E**(-x)-x")
y = sp.sympify(func)

# Ingresar los límites y tolerancia
x0 = st.number_input("X0 ✏️", -10.0, 10.0, 0.0, 0.1)
x1 = st.number_input("X1 ✏️", -10.0, 10.0, 1.0, 0.1)
tol = st.number_input("Tolerancia ✏️", 0.1, 10.0, 1.0, 0.1)
max_iter = st.number_input("Máximo de iteraciones ✏️", 1, 300, 100, 1)

# Valores iniciales
er = tol+1
it = 1
r = np.linspace(start_range,end_range, 100)

# Dataframe para almacenar los resultados
columnas = ['xi','Xi-1','f(xi)','f(Xi-1)','er(%)']
tabla = pd.DataFrame(columns=columnas)

# Espacio reservado para la figura
fig_placeholder = st.empty()
tablita = st.empty()

while er > tol and it < max_iter:
  fx0=round(y.subs({x:x0}),4)
  fx1=round(y.subs({x:x1}),4)

  # Crear la figura
  plt.figure()
  fig, ax = plt.subplots()

  fx = [y.subs({x:x_i}) for x_i in r]
  ax.plot(r,fx,color='blue',label=f"${sp.latex(y)}$")

  ## Plano cartesiano (Ejes)
  ax.vlines(x=0,ymin=min(fx)-0.1,ymax=max(fx)+0.1,color='k')
  ax.hlines(y=0,xmin=min(r)-0.1,xmax=max(r)+0.1,color='k')

  ## Punto inicial
  ax.plot([x1],[fx1], color='red', marker='o', label=f'$(x_{it},f(x_{it}))= ({x1},{fx1})$')

  ## Calculemos el x_i+1 (X2) siguiente
  x2 = round(x1 - (fx1 * (x1 - x0) / (fx1 - fx0)),4)
  ax.plot([x2],[0], color='red', marker='x', label=f'$(x_{it+1},0) = ({x2},0)$')

  ## Pintar la recta secante
  y0 = fx0
  y1 = fx1
  ax.plot([x0, x1], [y0, y1], color='purple',linestyle='--')

  ##titulo de la grafica
  ax.set_title(f"${sp.latex(y)}$")
  ax.grid()
  plt.xlabel("x")
  plt.ylabel("y")
  ax.legend()

  ## Calculo del error
  er = np.abs((x2-x1)/(x2)) * 100

  ## Actualicemos la tabla de iteraciones
  nueva_fila = {'xi':x1,'Xi-1':x0,'f(xi)':fx1,"f(Xi-1)":fx0,'er(%)':round(er,4)}
  nueva_fila = pd.DataFrame([nueva_fila])
  tabla = pd.concat([tabla, nueva_fila], ignore_index=True)

  #Actualizamos la iteración y el valor de x actual (xi)
  it += 1
  x0 = x1
  x1 = x2
  
  # Mostrar la figura en el espacio reservado
  fig_placeholder.pyplot(fig)
  tablita.dataframe(tabla)
    
  # Borra la figura para la siguiente iteración
  plt.close(fig)

st.success(f"La raíz está en: ({round(x1,4)}, {round(fx1,4)})")
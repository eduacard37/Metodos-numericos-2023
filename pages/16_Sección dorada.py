import streamlit as st
import sympy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.markdown("# Métodos optimización irrestricta 💻")
st.sidebar.markdown("# Método sección dorada 💻")

# Configuración de la página
st.markdown("## Visualizador de Método sección dorada 📈")
st.image("https://s-media-cache-ak0.pinimg.com/736x/46/b2/08/46b20812fd012c98f75d769fa8699048.jpg",width=400)
st.write("Esta aplicación muestra la gráfica de la sección dorada")

# Definir el rango de entrada
start_range = st.sidebar.slider("Inicio del rango", -10.0, 10.0, -1.0)
end_range = st.sidebar.slider("Fin del rango", -10.0, 10.0, 5.0)

# Ingresar la función
var = st.text_input("Variable ✏️", "x")
x = sp.symbols(var)
funcion = st.text_input("Función ✏️", "2*sin(x) - ((x**2)/10)")
f = sp.sympify(funcion)

# Ingresar los límites y tolerancia
xl = st.number_input("Límite inferior ✏️", -10.0, 10.0, 0.0, 0.1)
xu = st.number_input("Límite superior ✏️", -10.0, 10.0, 4.0, 0.1)
tol = st.number_input("Tolerancia ✏️", 0.1, 10.0, 10.0, 0.1)
x0 = st.number_input("x0 ✏️", 0.01, 1.0, 0.01, 0.01)

# Seleccionar máximo o mínimo
option = st.radio("Seleccione una opción ✏️", options=["Máximo", "Mínimo"])

# Inicializamos el error con un valor mayor que la tolerancia
error = tol + 1 
R = (np.sqrt(5)-1)/2 # Proporción áurea
it = 1 # Número de iteración
x0 = 0.01

t = np.linspace(start_range,end_range,400)
y = [f.subs(x, ti) for ti in t]

# Creacion del dataframe
columnas = ['xl', 'xu', 'x1', 'x2', 'f(x1)', 'f(x2)', 'x0', 'error(%)']
tabla = pd.DataFrame(columns=columnas)

# Espacio reservado para la figura
fig_placeholder = st.empty()
tablita = st.empty()

d = R*(xu-xl)
x1 = xl + d
x2 = xu - d

fx1 = round(f.subs({x:x1}),4)
fx2 = round(f.subs({x:x2}),4)

while error > tol:
  fx1 = f.subs({x:x1})
  fx2 = f.subs({x:x2})
  error = (1-R)*np.abs((xu-xl)/x0)*100

  data = {'xl':[xl], 'xu':[xu], 'x1':[x1], 'x2':[x2], 'f(x1)':[fx1], 'f(x2)':[fx2], 'x0':[x0], 'error(%)':[round(error,2)]}
  fila = pd.DataFrame(data = data)
  tabla = pd.concat([tabla,fila],ignore_index=True)

  # Graficar
  fig, ax = plt.subplots()
  ax.plot(t, y)
  ax.grid()
  ax.set_title("Método de la sección dorada")

  ## Plano cartesiano (Ejes)
  ax.vlines(x=0,ymin=min(y)-0.5,ymax=max(y)+0.5,color='k')
  ax.hlines(y=0,xmin=min(t)-0.5,xmax=max(t)+0.5,color='k')

  ## Límites xl y xu
  ax.vlines(x=xl, ymin=0, ymax=f.subs({x:xl}), color='g', linestyle='--',label=f"$x_l$ = {round(xl,3)}")
  ax.vlines(x=xu, ymin=0, ymax=f.subs({x:xu}), color='b', linestyle='--',label=f"$x_u$ = {round(xu,3)}")
  ax.vlines(x=x1, ymin=0, ymax=fx1, color='r', linestyle='--',label=f"$x_1$ = {round(x1,3)}")
  ax.vlines(x=x2, ymin=0, ymax=fx2, color='purple', linestyle='--',label=f"$x_2$ = {round(x2,3)}")
  ax.legend()

  #Fin de la grafica
  if option == 'Máximo':
    if fx1 > fx2:
        xl = x2
        x2 = x1
        x0 = xl + d
        x1 = xl + d
    elif fx1 < fx2:
        xu = x1
        x1 = x2
        x0 = x2
        x2 = xu - d
  else:
    if fx1 < fx2:
        xl = x2
        x2 = x1
        x0 = xl + d
        x1 = xl + d
    elif fx1 > fx2:
        xu = x1
        x1 = x2
        x0 = x2
        x2 = xu - d
  data['x0'] = [x0]
  d = R * (xu-xl)

  # Mostrar la figura en el espacio reservado
  fig_placeholder.pyplot(fig)
  tablita.dataframe(tabla)

  # Borra la figura para la siguiente iteración
  plt.close(fig)

st.success(f"El óptimo está en: {round(x0,2)}")
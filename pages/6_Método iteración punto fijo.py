from sympy.functions.elementary.integers import RoundFunction

#importamos librerias
import streamlit as st
import matplotlib.pyplot as plt
from math import *
import sympy as sp
import numpy as np
import pandas as pd
sp.init_printing(use_latex=True)

st.markdown("# Métodos abiertos 💻")
st.sidebar.markdown("# Método Iteracion punto fijo 💻")

# Configuración de la página
st.markdown("## Visualizador de Método Iteración punto fijo 📈")
st.image("https://www.researchgate.net/publication/260157940/figure/fig4/AS:668222424616962@1536328049067/Figura-4-Metodo-del-punto-Fijo-en-GeoGebra.png",width=400)
st.write("Esta aplicación muestra la gráfica de iteración del punto fijo")

# Definir el rango de entrada
start_range = st.sidebar.slider("Inicio del rango", -10.0, 10.0, 0.1)
end_range = st.sidebar.slider("Fin del rango", -10.0, 10.0, 2.0)

# Ingresar la función
var = st.text_input("Variable ✏️", "x")
x = sp.symbols(var)
funcion = st.text_input("Función ✏️", "e**(-x)-x")
f = sp.lambdify(x,funcion)


# Ingresar los límites y tolerancia
x0 = st.number_input("X0 ✏️", -10.0, 10.0, 1.0, 0.1)
n_iter = st.number_input("Número de iteraciones ✏️", 1, 100, 20, 1)
tol = st.number_input("Tolerancia ✏️", 0.1, 10.0, 1.0, 0.1)

error = tol+1
it = 1

# Dataframe para almacenar los resultados
columnas = ['x0','x1','er(%)','f(x1)']
tabla = pd.DataFrame(columns=columnas)

# Espacio reservado para la figura
fig_placeholder = st.empty()
tablita = st.empty()

ims = []
r = np.linspace(x0-2,x0+2, 100)

while it < n_iter:

  # Crear la figura
  plt.figure()
  fig, ax = plt.subplots()
  f_x = f(r)
  ax.plot(r,f_x,color='blue',label=(f'${funcion}$'))

  ## Plano cartesiano (Ejes)
  ax.vlines(x=0,ymin=round(min(f(r)),4)-0.5,ymax=round(max(f(r)),4)+0.5,color='k')
  ax.hlines(y=0,xmin=round(min(r),4)-0.5,xmax=round(max(r),4)+0.5,color='k')
  ax.set_title(f'${funcion}$')
  ax.grid()

  #Calculamos la raíz
  g = f(x)+x
  g = sp.lambdify(x,g)
  x1 = g(x0)

  ## Pintamos el punto fijo
  ax.plot(x1,f(x1),color='red',label=f'$Raíz=${x1}',marker='o')
  ax.legend()
  ax.axis('on')
  plt.show()
  
  ## Calculo del error
  error = np.abs((x1-x0)/x1)*100

  ## Actualicemos la tabla de iteraciones
  nueva_fila = {'x0': x0, 'x1': x1, 'er(%)': error, 'f(x1)': f(x1)}
  nueva_fila = pd.DataFrame([nueva_fila])
  tabla = pd.concat([tabla, nueva_fila], ignore_index=True)

  if error < tol:
    print(f"La raiz es: ({x1})")
    break

  #Actualizamos la iteración y el valor de x actual (xi)
  x0 = x1
  it+=1
  
  
  # Mostrar la figura en el espacio reservado
  fig_placeholder.pyplot(fig)
  tablita.dataframe(tabla)
    
  # Borra la figura para la siguiente iteración
  plt.close(fig)

st.success(f"La raíz está en: ({round(x1,4)}, {round(f(x1),4)})")
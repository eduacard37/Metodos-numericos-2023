import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import pandas as pd

st.markdown("# Métodos cerrados 💻")
st.sidebar.markdown("# Método falsa posición 💻")

# Configuración de la página
st.markdown("## Visualizador de Método Falsa posición 📈")
st.image("https://3.bp.blogspot.com/-EsgQFttXJ84/TyNjK9zq9cI/AAAAAAAAALQ/x142PgxC8AE/s1600/metodo+regla+falsa.jpg",width=400)
st.write("Esta aplicación muestra la gráfica de falsa posición")

# Definir el rango de entrada
start_range = st.sidebar.slider("Inicio del rango", -10.0, 10.0, 0.1)
end_range = st.sidebar.slider("Fin del rango", -10.0, 10.0, 2.0)

# Ingresar la función
var = st.text_input("Variable ✏️", "x")
x = sp.symbols(var)
funcion = st.text_input("Función ✏️", "x**3 - x")
y = sp.sympify(funcion)

# Ingresar los límites y tolerancia
xl = st.number_input("Límite inferior ✏️", -10.0, 10.0, 0.2, 0.1)
xu = st.number_input("Límite superior ✏️", -10.0, 10.0, 1.7, 0.1)
tol = st.number_input("Tolerancia ✏️", 0.1, 10.0, 1.0, 0.1)

# Valores iniciales
xr = None
xr_ant = xu
error = tol+1
it = 1

# Dataframe para almacenar los resultados
columnas = ['Xl','Xu','Xr','er(%)','f(Xl)','f(Xu)','f(Xr)']
tabla = pd.DataFrame(columns=columnas)

# Espacio reservado para la figura
fig_placeholder = st.empty()
tablita = st.empty()

r = np.linspace(start_range,end_range, 100)

while error > tol:
  #Evaluamos la función en los puntos del intervalo.
  fxl= round(y.subs({x:xl}),4)
  fxu= round(y.subs({x:xu}),4)

  #Crear la figura
  fig, ax = plt.subplots()

  fx = [y.subs({x:xi}) for xi in r]
  ax.plot(r,fx,color='blue',label=f"${sp.latex(y)}$")
  
  ## Plano cartesiano (Ejes)
  ax.vlines(x=0,ymin=round(min(fx),4)-0.5,ymax=round(max(fx),4)+0.5,color='k')
  ax.hlines(y=0,xmin=round(min(r),4)-0.5,xmax=round(max(r),4)+0.5,color='k')
  ax.set_title(f"${sp.latex(y)}$")
  ax.grid()

  ## Límites xl y xu
  ax.vlines(x=xl, ymin=0, ymax=fxl, color='k', linestyle='--',label=f'$x_l=${xl}')
  ax.vlines(x=xu, ymin=0, ymax=fxu, color='k', linestyle='--',label=f'$x_u=${xu}')

  #Calculamos la raíz
  xr = round(((fxl*xu)-(fxu*xl))/(fxl-fxu),4)
  fxr = round(y.subs({x:xr}),4)

  # Pintamos el punto intermedio
  ax.plot(xr,fxr,color='red',label=f'$Raíz=${xr}',marker='o')

  # Trazo de la linea recta
  ax.plot([xl,xu],[fxl,fxu],color='red')
  ax.legend()

  # Actualizamos el error y la tabla
  error = round(np.abs((xr-xr_ant)/(xr))*100,4)
  nueva_fila = {'Xl': xl, 'Xu': xu, 'Xr': xr, 'er(%)': error, 'f(Xl)': fxl, 'f(Xu)': fxu, 'f(Xr)':fxr}
  nueva_fila = pd.DataFrame([nueva_fila])
  tabla = pd.concat([tabla, nueva_fila], ignore_index=True)

  # Actualizamos los límites
  if (fxl * fxr) < 0:
    xu = xr
  elif (fxl*fxr) > 0:
    xl = xr
  elif (fxl*fxr) == 0:
    print(f"La raiz está en: ({xr},{fxr})")
    break

  xr_ant = xr
  it+=1
  
  # Mostrar la figura en el espacio reservado
  fig_placeholder.pyplot(fig)
  tablita.dataframe(tabla)
  
  # Borra la figura para la siguiente iteración
  plt.close(fig)

st.success(f"La raíz está en: ({round(xr,4)}, {round(fxr,4)})")
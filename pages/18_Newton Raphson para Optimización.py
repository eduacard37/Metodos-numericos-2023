import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import pandas as pd

st.markdown("# Métodos optimización irrestricta 💻")
st.sidebar.markdown("# Método Newton Raphson 💻")

# Configuración de la página
st.markdown("## Visualizador de Método Newton Raphson 📈")
st.image("https://4.bp.blogspot.com/-GayFzveB56k/UKASSVyVV2I/AAAAAAAAAs8/Jxo3eiN51W4/s1600/newton.png",width=400)
st.write("Esta aplicación muestra la gráfica de Newton Raphson")

# Definir el rango de entrada
start_range = st.sidebar.slider("Inicio del rango", -10.0, 10.0, -1.0)
end_range = st.sidebar.slider("Fin del rango", -10.0, 10.0, -0.1)

# Ingresar la función
var = st.text_input("Variable ✏️", "x")
x = sp.symbols(var)
funcion = st.text_input("Función ✏️", "x**3-x")
y = sp.sympify(funcion)

# Ingresar los límites y tolerancia
xi = st.number_input("Punto xi ✏️", -10.0, 10.0, -1.0, 0.1)
tol = st.number_input("Tolerancia ✏️", 0.01, 10.0, 1.0, 0.01)

y1 = sp.diff(y)
print("La función es: ",y)

columnas = ['xi','Xi+1','f(xi)',"f'(Xi)",'er(%)']
tabla = pd.DataFrame(columns=columnas)

# Espacio reservado para la figura
fig_placeholder = st.empty()
tablita = st.empty()

er = tol+1
it = 1
ims = []

while er > tol:
  fxi = round(y1.subs({x: xi}), 4)

  # Grafica
  plt.figure()
  fig, ax = plt.subplots()

  r = np.linspace(start_range,end_range, 100)
  fx = [y.subs({x:x_i}) for x_i in r]

  ax.plot(r,fx,color='blue',label=f"${sp.latex(y)}$")

  ## Plano cartesiano (Ejes)
  ax.vlines(x=0,ymin=min(fx)-0.1,ymax=max(fx)+0.1,color='k')
  ax.hlines(y=0,xmin=min(r)-0.1,xmax=max(r)+0.1,color='k')

  ## Punto inicial
  ax.scatter([xi],[y.subs({x:xi})], color='red', marker='o', label=f'$(x_{it},f(x_{it}))= ({xi},{y.subs({x:xi})})$')

  ## Calculemos la derivada
  dy = y1.diff()

  ## Evaluemos la derivada en x_i
  dfxi = round(dy.subs({x:xi}),4)

  ## Calculemos el x_i+1 (siguiente)
  xs = round(xi - ((fxi)/(dfxi)),4)
  ax.scatter([xs],[y.subs({x:xs})], color='red', marker='x', label=f'$(x_{it+1},{y.subs({x:xs})}) = ({xs},{y.subs({x:xs})})$')

  ## Pintar la recta tangente
  h=0.001
  dfx = (y.subs({x:xi+h})-y.subs({x:xi}))/h
  tan = y.subs({x:xi})+dfx*(r-xi)
  ax.plot(r,tan,color='purple',linestyle='--',label=f"${sp.latex(dy)}$")
  ax.set_title(f"${sp.latex(y)}$")
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  ax.grid()
  ax.legend()

  ## Calculo del error
  er = np.abs((xs-xi)/(xs)) * 100

  ## Actualicemos la tabla de iteraciones
  nueva_fila = {'xi':xi,'Xi+1':xs,'f(xi)':fxi,"f'(Xi)":dfxi,'er(%)':round(er,4)}
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

st.success(f"El óptimo está en: ({round(xs,4)}, {y.subs({x:xs})})")
import streamlit as st
import sympy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.markdown("# Métodos optimización irrestricta 💻")
st.sidebar.markdown("# Método del Gradiente 💻")

# Configuración de la página
st.markdown("## Visualizador de Método Gradiente 📈")
st.image("https://www.codificandobits.com/img/posts/2018-07-02/gradiente-descendente-ejemplo-grafico-1.png",width=400)
st.write("Esta aplicación muestra la gráfica del gradiente")

# Definir el rango de entrada
start_range = st.sidebar.slider("Inicio del rango", -10.0, 10.0, -3.0)
end_range = st.sidebar.slider("Fin del rango", -10.0, 10.0, -1.0)

# Ingresar la función
var = st.text_input("Variable ✏️", "x")
x = sp.symbols(var)
funcion = st.text_input("Función ✏️", "x**2+5*x+6")
f = sp.sympify(funcion)

# Ingresar los límites y tolerancia
xi = st.number_input("Punto xi ✏️", -10.0, 10.0, -0.1, 0.1)
tol = st.number_input("Tolerancia ✏️", 0.01, 10.0, 0.1, 0.1)
alfa = st.number_input("Alfa ✏️", 0.01, 1.0, 0.1, 0.1)

# Hallar la derivada
df=sp.diff(f)
f=sp.lambdify(x, f, "numpy")
df=sp.lambdify(x, df, "numpy")

columnas = ['xi','xs','f(xs)','er(%)']
tabla = pd.DataFrame(columns=columnas)

# Espacio reservado para la figura
fig_placeholder = st.empty()
tablita = st.empty()

error = tol + 1
it = 1 # Número de iteración

t=np.linspace(start_range,end_range,100)
y=f(t)
fig, ax = plt.subplots()
ax.plot(t,y)
ax.set_title("Método del gradiente")
alfa=0.01

while error>tol:
  xs = xi-(alfa*df(xi))
  error = np.abs((xs-xi)/xs)*100
  
  ## Actualicemos la tabla de iteraciones
  nueva_fila = {'xi':xi,'xs':xs,'f(xs)':f(xs),'er(%)':round(error,4)}
  nueva_fila = pd.DataFrame([nueva_fila])
  tabla = pd.concat([tabla, nueva_fila], ignore_index=True)
  
  xi=xs
  plt.scatter(xs,f(xs),c='g')
  
  # Mostrar la figura en el espacio reservado
  fig_placeholder.pyplot(fig)
  tablita.dataframe(tabla)
ax.scatter(xs,f(xs),c='r')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.grid()

#fig_placeholder.pyplot(fig)
tablita.dataframe(tabla)
  
# Borra la figura para la siguiente iteración
plt.close(fig)

st.success(f"El optimo está en: ({round(xs,2)}, {round(f(xs),2)})")
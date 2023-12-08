import streamlit as st
import sympy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.markdown("# Métodos optimización irrestricta 💻")
st.sidebar.markdown("# Método interpolación cuadrática 💻")

# Configuración de la página
st.markdown("## Visualizador de Método interpolación cuadrática 📈")
st.image("https://1.bp.blogspot.com/-Il_LQ3i4fpI/V2OtEP_25KI/AAAAAAAAImI/3NXHKZlpKqg0CMgv7OJHIUBkVit4YEJ8QCLcB/s1600/parab1172016.png",width=400)
st.write("Esta aplicación muestra la gráfica de interpolación cuadrática")

# Definir el rango de entrada
start_range = st.sidebar.slider("Inicio del rango", -10.0, 10.0, -1.5)
end_range = st.sidebar.slider("Fin del rango", -10.0, 10.0, 0.0)

# Ingresar la función
var = st.text_input("Variable ✏️", "x")
x = sp.symbols(var)
funcion = st.text_input("Función ✏️", "x**3-2*x")
f = sp.sympify(funcion)
f=sp.lambdify(x, f, "numpy")

# Ingresar los límites y tolerancia
x0 = st.number_input("Punto x0 ✏️", -10.0, 10.0, -1.0, 0.1)
x1 = st.number_input("Punto x1 ✏️", -10.0, 10.0, -0.4, 0.1)
x2 = st.number_input("Punto x2 ✏️", -10.0, 10.0, -0.2, 0.1)
tol = st.number_input("Tolerancia ✏️", 0.01, 10.0, 0.1, 0.01)

# Criterio de parada y error inicial
error = tol + 1
x3ant=x0
it = 1
# Vector linealmente espaciado
t=np.linspace(start_range,end_range,100)
y=f(t)

columnas = ['x0', 'x1', 'x2', 'f(x0)', 'f(x1)', 'f(x2)', 'error(%)']
tabla = pd.DataFrame(columns=columnas)

# Espacio reservado para la figura
fig_placeholder = st.empty()
tablita = st.empty()

# Gráfica del método
fig, ax = plt.subplots()
ax.plot(t,y)
ax.vlines(x=0,ymin=min(y)-0.1,ymax=max(y)+0.1,color='k')
ax.hlines(y=0,xmin=min(t)-0.1,xmax=max(t)+0.1,color='k')

while error>tol:
  x3=(f(x0)*(x1**2-x2**2)+f(x1)*(x2**2-x0**2)+f(x2)*(x0**2-x1**2))/(2*f(x0)*(x1-x2)+2*f(x1)*(x2-x0)+2*f(x2)*(x0-x1))
  if(x3>=x1):
    if(f(x3)>f(x1)):
      x0=x1
      x1=x3
    else:
      x2=x3
  else:
    if(f(x3)<f(x1)):
      x0=x3
    else:
      x2=x1
      x1=x3
  error=np.abs((x3-x3ant)/x3)*100
  x3ant=x3

  data = {'x0':[x0], 'x1':[x1], 'x2':[x2], 'f(x0)':[f(x0)], 'f(x1)':[f(x1)], 'f(x2)':[f(x2)], 'error(%)':[round(error,2)]}
  fila = pd.DataFrame(data = data)
  tabla = pd.concat([tabla,fila],ignore_index=True)

ax.scatter(x3,f(x3),c='r')
ax.text(x3+0.1,f(x3),(round(x3,2),round(f(x3),2)))
ax.set_title('Interpolacion cuadrática')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid()

# Mostrar la figura en el espacio reservado
fig_placeholder.pyplot(fig)
tablita.dataframe(tabla)

# Borra la figura para la siguiente iteración
plt.close(fig)

st.success(f"El óptimo está en: ({round(x3,2)}, {round(f(x3),2)})")
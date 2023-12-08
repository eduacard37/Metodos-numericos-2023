import streamlit as st
import sympy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.markdown("# Métodos diferenciación e integración 💻")
st.sidebar.markdown("# Método Trapecio múltiple 💻")

# Configuración de la página
st.markdown("## Visualizador de Método Trapecio múltiple 📈")
st.image("https://i.ytimg.com/vi/rREhW5wjkUI/maxresdefault.jpg",width=400)
st.write("Esta aplicación muestra la gráfica del Trapecio múltiple")

# Definir el rango de entrada
start_range = st.sidebar.slider("Inicio del rango", -10.0, 10.0, 0.0)
end_range = st.sidebar.slider("Fin del rango", -10.0, 10.0, 6.0)

# Ingresar la función
var = st.text_input("Variable ✏️", "x")
x = sp.symbols(var)
Funcion = st.text_input("Función ✏️", "3*x**2")
fx = sp.sympify(Funcion)

# Ingresar puntos para hallar el trapecio y cantidad de intervalos
a = st.number_input("Punto a ✏️", -10, 10, 1, 1)
b = st.number_input("Punto b ✏️", -10, 10, 4, 1)
n = st.number_input("Número de segmentos (n) ✏️", 1, 10, 3, 1)

h = (b - a) / n
print (f"f(x)= {fx}, a = {a}, b = {b}, n = {n}, h = {h}")

t = np.arange(a,b+h,h)
y = [float(round(fx.subs({x:ti}),3)) for ti in t]

print("xi = ",t)
print("f(xi)= ",y)

sum = 0
for i in range (1,len(y)-1):
  sum = y[i]+sum

I = h/2 * (y[0] + 2 * (sum) + y[-1])

# Espacio reservado para la figura
fig_placeholder = st.empty()

# Ahora usemos la funcion de integracion simbólica de sympy
I_real = sp.integrate(fx,(x,a,b))
st.info(f"La integral por sympy es: {I_real}")
st.info(f"La integral numerica es: {I}")

error = np.abs((I_real - I)/(I_real))*100
st.error(f"La integración tiene un error de {error:.2f}%")

plt.figure()
t = np.linspace(a-1,b+1, 100)
y = [fx.subs({x:i})for i in t]

fig, ax = plt.subplots()
ax.plot(t,y,color='blue',label=(f"${sp.latex(fx)}$"))
ax.set_title("Método trapezoidal múltiple")
ax.grid()

fa = fx.subs({x:a})
fb = fx.subs({x:b})

## Plano cartesiano (Ejes)
ax.vlines(x=0,ymin=min(y),ymax=max(y),color='k')
ax.hlines(y=0,xmin=min(t),xmax=max(t),color='k')

## límites xl y xu
ax.vlines(x=a, ymin=0, ymax=fa, color='r', linestyle='--')
ax.vlines(x=b, ymin=0, ymax=fb, color='r', linestyle='--')

while a <= b-h:
  fa = fx.subs({x:a})
  fb = fx.subs({x:a+h})
  ax.vlines(x=a+h, ymin=0, ymax=fb, color='r', linestyle='--')
  ax.fill([a,a,a+h,a+h],[0,fa,fb,0], 'r', alpha=0.2)
  ax.plot([a,a+h],[fa,fb], color='r', linestyle='--')
  a = a+h

plt.grid(True)
plt.legend()

# Mostrar gráfica
fig_placeholder.pyplot(fig)
plt.close(fig)

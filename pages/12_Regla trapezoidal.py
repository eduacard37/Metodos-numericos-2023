import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
sp.init_printing(use_latex=True)

st.markdown("# Métodos diferenciación e integración 💻")
st.sidebar.markdown("# Método Trapecio 💻")

# Configuración de la página
st.markdown("## Visualizador de Método Trapecio 📈")
st.image("https://i.ytimg.com/vi/dUY784-uRk0/maxresdefault.jpg",width=400)
st.write("Esta aplicación muestra la gráfica del Trapecio")

# Definir el rango de entrada
start_range = st.sidebar.slider("Inicio del rango", -10.0, 10.0, 0.0)
end_range = st.sidebar.slider("Fin del rango", -10.0, 10.0, 6.0)

# Ingresar la función
var = st.text_input("Variable ✏️", "x")
x = sp.symbols(var)
Funcion = st.text_input("Función ✏️", "3*x**2")
fx = sp.sympify(Funcion)

# Ingresar punto para hallar el trapecio
a = st.number_input("Punto a ✏️", -10, 10, 1, 1)
b = st.number_input("Punto b ✏️", -10, 10, 4, 1)
fa = fx.subs({x:a})
fb = fx.subs({x:b})

print(f"f(a) = {fa} \nf(b) = {fb}")

# Aplicamos la regla trapezoidal
I = (b-a) * ((fa+fb)/2)
print("I = ",I, "U^2")

# Integral real
real = sp.integrate (fx, (x,a,b))

# Calculemos el error
e = np.abs((real - I)/(real)) * 100

plt.figure()
xi = np.linspace(start_range,end_range, 100)
y = [fx.subs({x:i})for i in xi]

# Espacio reservado para la figura
fig_placeholder = st.empty()

fig, ax = plt.subplots()
ax.plot(xi,y,color='blue',label=f"${sp.latex(fx)}$")
ax.set_title("Regla trapezoidal")
plt.xlabel('X')
plt.ylabel('Y')
ax.grid()

## Plano cartesiano (Ejes)
ax.vlines(x=0,ymin=min(y),ymax=max(y),color='k')
ax.hlines(y=0,xmin=min(xi),xmax=max(xi),color='k')

## límites xl y xu
ax.vlines(x=a, ymin=0, ymax=fa, color='r', linestyle='--')
ax.vlines(x=b, ymin=0, ymax=fb, color='r', linestyle='--')
ax.plot([a,b],[fa,fb], color='r', linestyle='--')

ax.fill([a,a,b,b],[0,fa,fb,0], 'r', alpha=0.2)

plt.grid(True)
plt.legend()

# Mostrar gráfica
fig_placeholder.pyplot(fig)
plt.close(fig)

st.info(f"El error es de {round(e,2)} %")
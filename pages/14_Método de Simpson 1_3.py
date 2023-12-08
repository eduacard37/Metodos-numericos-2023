import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.markdown("# Métodos diferenciación e integración 💻")
st.sidebar.markdown("# Método Simpson 1/3 💻")

# Configuración de la página
st.markdown("## Visualizador de Método Simpson 1/3 📈")
st.image("https://multimedia.uned.ac.cr/pem/metodos_numericos_ensenanza/modulo4/img/des/Simpson1.jpg",width=400)
st.write("Esta aplicación muestra la gráfica de Simpson 1/3")

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
b = st.number_input("Punto b ✏️", -10, 10, 2, 1)

m = (a+b)/2

fa = fx.subs({x:a})
fb = fx.subs({x:b})
fm = fx.subs({x:m})
print(f"f(a) = {fa} \nf(b) = {fb} \nf(m) = {fm:.2f}")

# Aplicamos la regla de simpson 1/3
I = (b-a) * ((fa + 4*fm + fb)/6)

# Espacio reservado para la figura
fig_placeholder = st.empty()

print("I = ",I, "U^2")

# Ahora usemos la funcion de integracion simbólica de sympy
I_real = sp.integrate(fx,(x,a,b))
st.info(f"La integral por sympy es: {I_real}")

# Ahora calculamos el error
error = np.abs((I_real - I)/(I_real))*100
st.error(f"La integración tiene un error de {error:.2f}%")

import numpy as np
import matplotlib.pyplot as plt
plt.figure()

t = np.linspace(a-1,b+1, 100)
y = [fx.subs({x:i})for i in t]

fig, ax = plt.subplots()
ax.plot(t,y,color='blue',label=f"${sp.latex(fx)}$")
ax.set_title("Método Simpson 1/3")
ax.grid()

## Plano cartesiano (Ejes)
ax.vlines(x=0,ymin=min(y),ymax=max(y),color='k')
ax.hlines(y=0,xmin=min(t),xmax=max(t),color='k')

## límites xl y xu
ax.vlines(x=a, ymin=0, ymax=fa, color='r', linestyle='--')
ax.vlines(x=b, ymin=0, ymax=fb, color='r', linestyle='--')

ax.fill([a,a,m,b,b],[0,fa,fm,fb,0], 'r', alpha=0.2)
plt.grid(True)
plt.legend()

# Mostrar gráfica
fig_placeholder.pyplot(fig)
plt.close(fig)
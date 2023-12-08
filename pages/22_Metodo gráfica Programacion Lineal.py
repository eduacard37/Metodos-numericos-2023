import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

st.markdown("# Programación lineal 💻")
st.sidebar.markdown("# Método gráfico 💻")

# Configuración de la página
st.markdown("## Visualizador de Método Gráfico 📈")
st.image("https://i0.wp.com/www.celeberrima.com/wp-content/uploads/2019/09/ejemplo-metodo-grafico-programacion-lineal6.png?w=843&ssl=1",width=400)
st.write("Esta aplicación muestra la gráfica del método gráfico")

# Definir el rango de entrada
start_range = st.sidebar.slider("Inicio del rango", -10.0, 30.0, 0.0)
end_range = st.sidebar.slider("Fin del rango", -10.0, 30.0, 30.0)

# Ingresar las restricciones
var = st.text_input("Variable ✏️", "x y")
x, y = sp.symbols(var)
R_1 = st.text_input("Restricción 1 ✏️", "x + 2*y - 20")
Restriccion_1 = sp.sympify(R_1)
R_2 = st.text_input("Restricción 2 ✏️", "3*x + 4*y - 12")
Restriccion_2 = sp.sympify(R_2)

# Ingresar los vertices
Vertice_1 = st.text_input("Vertice 1 ✏️", "0,3")
Vertice_2 = st.text_input("Vertice 2 ✏️", "4,0")
Vertice_3 = st.text_input("Vertice 3 ✏️", "0,10")
Vertice_4 = st.text_input("Vertice 4 ✏️", "20,0")

# Configurar el rango para las variables
x_vals = np.linspace(start_range, end_range, 100)

# Espacio reservado para la figura
fig_placeholder = st.empty()

# Convertir restricciones a funciones para y
y_restriccion1 = sp.solve(Restriccion_1, y)[0]
y_restriccion2 = sp.solve(Restriccion_2, y)[0]

# Convertir a funciones numéricas
func_restriccion1 = sp.lambdify(x, y_restriccion1, modules=['numpy'])
func_restriccion2 = sp.lambdify(x, y_restriccion2, modules=['numpy'])

# Crear la figura
fig, ax = plt.subplots()

# Graficar las restricciones
ax.plot(x_vals, func_restriccion1(x_vals), label=f"${sp.latex(Restriccion_1)}$")
ax.plot(x_vals, func_restriccion2(x_vals), label=f"${sp.latex(Restriccion_2)}$")
ax.set_xlim(0, 30)
ax.set_ylim(0, 30)
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.grid()
plt.axhline(0, color='black', lw=2)
plt.axvline(0, color='black', lw=2)
plt.fill_between(x_vals, func_restriccion1(x_vals), func_restriccion2(x_vals), where=(x_vals <= 30), color='gray', alpha=0.3,label="Región Factible")

# Convertir cadena a tupla (Coordenadas)
V_1 = Vertice_1.split(',')
V_2 = Vertice_2.split(',')
V_3 = Vertice_3.split(',')
V_4 = Vertice_4.split(',')
V_1 = (float(V_1[0]),float(V_1[1]))
V_2 = (float(V_2[0]),float(V_2[1]))
V_3 = (float(V_3[0]),float(V_3[1]))
V_4 = (float(V_4[0]),float(V_4[1]))

vertices = [
  V_1,
  V_2,
  V_3,
  V_4
]

optimo = max(vertices, key=lambda punto: 3*punto[0] + 2*punto[1])
ax.plot(optimo[0], optimo[1], 'ro', label="solución")
ax.set_title("Metodo gráfico")
ax.set_xlabel("x")
ax.set_ylabel("y")

plt.legend()

 # Mostrar la figura en el espacio reservado
fig_placeholder.pyplot(fig)
import streamlit as st
from sympy import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
init_printing(use_latex=True)

st.markdown("# Métodos Ecuaciones diferenciales ordinarias 💻")
st.sidebar.markdown("# Método Runge Kutta orden 2 💻")

# Configuración de la página
st.markdown("## Visualizador de Método Runge Kutta orden 2 📈")
st.image("https://th.bing.com/th/id/R.8cc53265bda6bdeba151bb36ca58094a?rik=v2dXl29Wmcq%2bnw&riu=http%3a%2f%2fblog.espol.edu.ec%2fanalisisnumerico%2ffiles%2f2018%2f01%2fRungeKutta2doOrden_01.png&ehk=%2bTs2TaNJ5gHt%2fs19P2RLlzQsObvJlaay%2bJEPo6AvjNA%3d&risl=&pid=ImgRaw&r=0",width=400)
st.write("Esta aplicación muestra la gráfica de Runge Kutta orden 2")

# Definir el rango de entrada
start_range = st.sidebar.slider("Inicio del rango", -10.0, 10.0, 0.0)
end_range = st.sidebar.slider("Fin del rango", -10.0, 15.0, 10.0)

# Ingresar las funciones y costantes
var = st.text_input("Variables ✏️", "t vi L R C")
t, vi, L, R, C = symbols(var)
const = st.text_input("Constantes ✏️", "C1 C2")
C1, C2 = symbols(const)

i = Function("i")(t)
v = Function("v")(t)

# Ecuaciones diferenciales
ecua_1 = st.text_input("Ecuación 1 ✏️", (1/L)*vi-(R/L)*i-(1/L)*v)
ecua_2 = st.text_input("Ecuación 2 ✏️", (1/C)*i)
ecua_1 = sympify(ecua_1)
ecua_2 = sympify(ecua_2)

# Condiciones iniciales para i y v
dt = st.number_input("Paso de integración ✏️", 0.01, 10.0, 0.1, 0.01)
initial_i = st.number_input("i inicial ✏️", 0.01, 10.0, 0.1, 0.1)
initial_v = st.number_input("v inicial ✏️", 0.01, 1.0, 0.1, 0.1)
initial_conditions = [initial_i, initial_v]

# Rango de tiempo de integración
time_range = (start_range, end_range)

# Hallamos las derivadas
didt=i.diff(t)
dvdt=v.diff(t)

# Asumimos valores de R,L y C = 1
expr1 = Eq(didt, (1/L)*vi-(R/L)*i-(1/L)*v)
expr1=expr1.subs(L, 1).subs(R,1).subs(C,1).subs(vi,1)

# Asumimos valores de R,L y C = 1
expr2 = Eq(dvdt, (1/C)*i)
expr2=expr2.subs(L,1).subs(R,1).subs(C,1).subs(vi,1)
s=dsolve([expr1,expr2])

# Vamos a hallar los valores de las ctes C1 y C2
eq1 = Eq(s[0].rhs.subs({t:0}).evalf(), 0.1)
eq2 = Eq(s[1].rhs.subs({t:0}).evalf(), 0.1)
sol = solve([eq1,eq2], [C1,C2])

# Generamos 2 funciones para reemplazar valores de t para graficar las soluciones
e1 = lambdify(t,s[0].rhs.subs(sol),'numpy')
e2 = lambdify(t,s[1].rhs.subs(sol),'numpy')
e1_simplex = s[0].rhs.subs(sol)
e2_simplex = s[1].rhs.subs(sol)

t_vals = np.linspace(start_range,end_range,100)

# Definición de las funciones para el sistema de ecuaciones diferenciales
def func_i(v, i, t):
    return 1 - i - v

def func_v(i, v, t):
    return i

# Definición de las funciones para el sistema de ecuaciones diferenciales
def runge_kutta_2_system(funcs, y0, t_range, dt):
    t_values = np.arange(t_range[0], t_range[1], dt)
    y_values = [np.array(y0)]

    for t in t_values[:-1]:
        y_current = y_values[-1]

        k1 = np.array([f(*y_current, t) for f in funcs])
        k2 = np.array([f(*(y_current + k1 * dt), t + dt) for f in funcs])

        y_next = y_current + dt * (0.5 * k1 + 0.5 * k2)
        y_values.append(y_next)
    return t_values, np.array(y_values).T

# Espacio reservado para la figura
fig_placeholder = st.empty()

st.success(f"La solución de (i) es: ${latex(e1_simplex)}$")
st.success(f"La solución de (v) es: ${latex(e2_simplex)}$")

# Solución aproximada para i(t) y v(t) usando el Método de Runge-Kutta de orden 2
t_values_rk2, [i_values_rk2_system, v_values_rk2_system] = runge_kutta_2_system(
    [func_i, func_v], initial_conditions, time_range, dt)

# Graficando soluciones analíticas y aproximadas
plt.figure()
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Grafica de la corriente
ax[0].plot(t_vals, e1(t_vals), label='Analítico i(t)')
ax[0].plot(t_values_rk2, i_values_rk2_system, label='RK2 Aproximado i(t)', linestyle='--')
ax[0].set_xlabel('Tiempo')
ax[0].set_ylabel('Corriente (i(t))')
ax[0].set_title('Corriente en función del tiempo')
ax[0].grid(True)
ax[0].legend()

# Grafica del voltaje
ax[1].plot(t_vals, e2(t_vals), label='Analítico v(t)', color='orange')
ax[1].plot(t_values_rk2, v_values_rk2_system, label='RK2 Aproximado v(t)', linestyle='--', color='green')
ax[1].set_xlabel('Tiempo')
ax[1].set_ylabel('Voltaje (v(t))')
ax[1].set_title('Voltaje en función del tiempo')
ax[1].grid(True)
ax[1].legend()

plt.tight_layout()
plt.show()

# Mostrar la figura en el espacio reservado
fig_placeholder.pyplot(fig)
  
# Borra la figura para la siguiente iteración
plt.close(fig)
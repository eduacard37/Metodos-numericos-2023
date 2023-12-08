import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
sp.init_printing(use_latex=True)

st.markdown("# Métodos optimización irrestricta 💻")
st.sidebar.markdown("# Método analítico 💻")

# Configuración de la página
st.markdown("## Visualizador de Método analítico 📈")
st.image("https://www.fisimat.com.mx/wp-content/uploads/2018/11/maximos_minimos.png",width=400)
st.write("Esta aplicación muestra la gráfica de la forma analítica")

# Definir el rango de entrada
start_range = st.sidebar.slider("Inicio del rango", -10.0, 10.0, 0.0)
end_range = st.sidebar.slider("Fin del rango", -10.0, 10.0, 6.0)

# Ingresar la función
var = st.text_input("Variable ✏️", "x")
x = sp.symbols(var)
Funcion = st.text_input("Función ✏️", "x**3 - 6*x**2 + 4*x + 12")
f = sp.sympify(Funcion)

# Espacio reservado para la figura
fig_placeholder = st.empty()

# Calculamos la primera derivada
f_prime = sp.diff(f, x)
st.info(f"La primera derivada es: ${sp.latex(f_prime)}$")

# Calculamos la segunda derivada
f_double_prime = sp.diff(f_prime, x)
st.info(f"La segunda derivada es: ${sp.latex(f_double_prime)}$")

# Encuentra los puntos críticos resolviendo f'(x) = 0
critical_points = sp.solve(f_prime, x)
st.success(f"Los puntos criticos son: ${sp.latex(critical_points)}$")

# Determinamos la naturaleza de los puntos críticos
nature_of_critical_points = []
for point in critical_points:
    if f_double_prime.subs(x, point) > 0:
        nature = "mínimo"
    elif f_double_prime.subs(x, point) < 0:
        nature = "máximo"
    else:
        nature = "inconclusivo"
    nature_of_critical_points.append(nature)
    
#print(critical_points)
#print(nature_of_critical_points)

# Graficamos la función y los puntos críticos
f_lambda = sp.lambdify(x, f, "numpy")
x_vals = np.linspace(float(min(critical_points)) - 2, float(max(critical_points)) + 2, 400)
y_vals = f_lambda(x_vals)

fig, ax = plt.subplots()
ax.plot(x_vals, y_vals, label=f"${sp.latex(f)}$", color='blue')
for point, nature in zip(critical_points, nature_of_critical_points):
    plt.scatter(point, f.subs(x, point), color='red')
    plt.text(point+0.2, f.subs(x, point), f'${sp.latex(point)}$: ${sp.latex(nature)}$')

ax.set_title("Función y sus puntos críticos")
plt.xlabel("x")
plt.ylabel("f(x)")
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()

 # Mostrar gráfica
fig_placeholder.pyplot(fig)
plt.close(fig)
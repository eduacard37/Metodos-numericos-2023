import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#from sklearn.metrics import r2_score, mean_squared_error

st.markdown("# Ajuste de curvas e interpolación 💻")
st.sidebar.markdown("# Método Regresión minimos cuadrados 💻")

# Configuración de la página
st.markdown("## Visualizador de Método Regresión minimos cuadrados 📈")
st.image("https://sourceexample.com/img/0be60616d5ff506a5fe8ac10f6b4d70c/6rdcvz5miv.png",width=400)
st.write("Esta aplicación muestra la gráfica de regresion por minimos cuadrados")

# Definir el rango de entrada
start_range = st.sidebar.slider("Inicio del rango", -10.0, 10.0, 0.1)
end_range = st.sidebar.slider("Fin del rango", -10.0, 10.0, 2.0)

# Indicar la ubicación de los archivos
filepath = st.file_uploader("Cargar archivo .CSV ✏️",type='csv')

# Importar los datos
df = pd.read_csv(filepath)

# Espacio reservado para la figura
fig_placeholder = st.empty()
tablita = st.empty()

fig, ax = plt.subplots()
ax.scatter(df["X"].to_list(),df["Y"].to_list(),color='blue',label="datos")
ax.set_title("Regresion")
ax.grid()
ax.legend()

# Calculamos las sumatorias y la pendiente y el intercepto de la recta.
x = np.array(df["X"])
y = np.array(df["Y"])

sx = np.sum(x)
sy = np.sum(y)

sx2 = np.sum(x**2)
sxy = np.sum(x*y)

n = len(x)

m = ((n*sxy) - (sx*sy))/((n*sx2)-(sx**2))
b = (sy -(m*sx))/n

print("Pendiente: ",m,"; intercepto: ",b,"\n")

fig, ax = plt.subplots()

# vamos a verificar como se realizó la interpolación
recta = m*x + b

ax.scatter(df["X"].to_list(),df["Y"].to_list(),color='blue',label="datos")
ax.plot(x,recta,color='red',label="y=mx+b")

ax.set_title("Regresion lineal")
ax.grid()
ax.legend()

## vamos a calcular las métricas de error.
#from sklearn.metrics import r2_score, mean_squared_error

# Calcular ECM
#mse = mean_squared_error(y, recta)
#print(f"\nEl error cuadrático medio ECM es: {mse}")

# Calcular R^2
#r2 = r2_score(y, recta)
#print(f"El coeficiente de determinacion R^2 es: {r2}")

#Mostrar la figura en el espacio reservado
fig_placeholder.pyplot(fig)
tablita.dataframe(df)
    
# Borra la figura para la siguiente iteración
plt.close(fig)

#st.success(f"La raíz está en: ({round(x1,4)}, {round(f(x1),4)})")
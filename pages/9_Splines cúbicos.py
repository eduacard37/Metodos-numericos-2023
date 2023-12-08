import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.markdown("# Ajuste de curvas e interpolación 💻")
st.sidebar.markdown("# Método Splines cúbicos 💻")

# Configuración de la página
st.markdown("## Visualizador de Método Splines cúbicos 📈")
st.image("https://i.stack.imgur.com/Hfx8t.png",width=400)
st.write("Esta aplicación muestra la gráfica de los splines cúbicos")

# Definir el rango de entrada
start_range = st.sidebar.slider("Inicio del rango", -10.0, 10.0, 0.1)
end_range = st.sidebar.slider("Fin del rango", -10.0, 10.0, 2.0)

def read_csv(file):
    return np.genfromtxt(file, delimiter=',', skip_header=1)

def cubic_spline_approximation(x, y):
    degree = 3
    coefs = np.polyfit(x, y, degree)
    polynomial = np.poly1d(coefs)
    return polynomial

def main():
    st.title('Interpolación de splines cubicos')

    file = st.file_uploader('Cargar archivo .csv', type='csv')
    if file is not None:
        data = read_csv(file)
        x = data[:, 0]
        y = data[:, 1]

        splines = cubic_spline_approximation(x, y)

        x_range = np.linspace(x.min(), x.max(), 1000)
        y_range = splines(x_range)

        st.subheader('Gráfica')
        plt.figure()
        plt.plot(x, y, 'o', label='Datos originales')
        plt.plot(x_range, y_range, '-', label='Función splines cúbicos')
        plt.legend()
        st.pyplot(plt)
        
        st.subheader('Datos originales')
        st.write(data)

        st.subheader('Función splines cúbicos')
        st.write(splines)

if __name__ == '__main__':
    main()
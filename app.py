import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('/Users/BELEN/Documents/Sprint 5/Proyecto-Sprint-5/vehicles_us.csv') # leer los datos

st.header('Proyecto :blue[SPRINT 5]')

#Creación checkbox histograma
build_histogram = st.checkbox('Construir un histograma') 

if build_histogram: # si la casilla de verificación está seleccionada
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig_h = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_h, use_container_width=True)


#Creación checkbox gráficos de disperción
build_scatter = st.checkbox('Construir gráfico de dispersión') 

if build_scatter: # si la casilla de verificación está seleccionada
   # escribir un mensaje
    st.write('Creación de un gráfico de disperción para el conjunto de datos de anuncios de venta de coches')

    # crear un gráfico de dispersión
    fig_s = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_s, use_container_width=True)
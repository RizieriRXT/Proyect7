import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("vehicles_us.csv") 
carros= car_data["model"].count()
marcas_model= car_data["model"].str.split()
marcas=[]
for i in marcas_model:
    marcas.append(i[0])
car_data["marca"]=marcas
marcas=car_data["marca"].nunique()
st.header('Carros listados para su venta ')
st.write(f"Se tiene un regiistro de {carros} anuncios de venta de coches, majeando {marcas} marcas distintas distintas")


seleccion_marca = st.selectbox("Selecciona una marca:", car_data["marca"].unique())
datos_filtrados = car_data[car_data["marca"] == seleccion_marca]
seleccion_model = st.selectbox("Selecciona un modelo:", datos_filtrados["model"].unique())
datos_filtrados = datos_filtrados[datos_filtrados["model"] == seleccion_model]
seleccion_condition = st.selectbox("Seleccione su estado:", datos_filtrados["condition"].unique())
datos_filtrados = datos_filtrados[datos_filtrados["condition"] == seleccion_condition]
seleccion_button = st.button(f"Mostrar autos {seleccion_model} con un estado: {seleccion_condition}")
if seleccion_button:

    st.write(f"Se encontraron {datos_filtrados["model"].count()} resultados para el modelo {seleccion_model}:")
    st.write(datos_filtrados)

st.header(f'Resuemen de la marca {seleccion_marca}')
build_histogram = st.checkbox('Histograma')
build_dispercion = st.checkbox('Grafica de disrpercion (precio/kilometraje)')
build_barra = st.checkbox('grafica de barras ( anuncios por color)')
resumen_button = st.button(f'Mostrar resumen de {seleccion_marca}') # crear un 
if resumen_button:
    if build_histogram:
        fig1 = px.histogram(car_data[car_data["marca"] == seleccion_marca], x="odometer")
        fig1.update_layout(
        title="Anuncios de autos segun su kilometraje",
        xaxis_title="Kilometros",  
        yaxis_title="Anuncios",
        title_x=0.3 ) 
        st.plotly_chart(fig1, use_container_width=True)
    if build_dispercion:
        fig3 = px.scatter(car_data[car_data["marca"] == seleccion_marca], x="odometer", y="price") 
        fig3.update_layout(
        title="Relacion del precio y el kilometraje",
        xaxis_title="Kilometros",  
        yaxis_title="Precio",
        title_x=0.3 ) 
        st.plotly_chart(fig3, use_container_width=True) 
    if build_barra:
        fig2 = px.bar(car_data[car_data["marca"] == seleccion_marca], x="paint_color")
        fig2.update_layout(
        title="Autos anuinciados segun su color",
        xaxis_title="Colores",  
        yaxis_title="Anuncios",
        title_x=0.3  ) 
        st.plotly_chart(fig2, use_container_width=True)

st.header("Anuncios de cada marca")
fig4 = px.bar(car_data, x="marca")
fig4.update_layout(
title="Anuncios por marca",
xaxis_title="Marca",  
yaxis_title="Anuncios",
title_x=0.3) 
st.plotly_chart(fig4, use_container_width=True)
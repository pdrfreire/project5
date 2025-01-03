import streamlit as st
import pandas as pd
import plotly.express as px

path = r"C:\Users\X\project5\project5\vehicles.csv"
car_data = pd.read_csv(path)

hist_button = st.button('Criar histograma')  # criar um botão
if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Criar gráfico de dispersão')
if disp_button:
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import pandas as pd
import plotly.express as px

path = "vehicles.csv"
car_data = pd.read_csv(path)

st.header('Análise exploratoria de dados - Vendas dos Veículos')

hist_button = st.button('Criar histograma')  # criar um botão
if hist_button:  # Se o botão for clicado
    # Mensagem inicial
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # Criar um histograma com melhorias
    fig = px.histogram(
        car_data,
        x="odometer",
        nbins=30,  # Ajustar o número de bins
        color_discrete_sequence=['#636EFA'],  # Cor personalizada
        title="Distribuição de Quilometragem dos Veículos",
        labels={"odometer": "Quilometragem (milhas)"},  # Rótulo do eixo X
    )

    # Personalizar layout
    fig.update_layout(
        title_font_size=20,
        xaxis_title_font_size=16,
        yaxis_title_font_size=16,
        xaxis=dict(title="Quilometragem (milhas)", tickformat=','),
        yaxis=dict(title="Frequência"),
        template="plotly_white",  # Tema do gráfico
    )

    # Exibir o gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.checkbox('Criar gráfico de dispersão')

if disp_button:
    # Mensagem inicial
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    # Criar um gráfico de dispersão com melhorias
    fig = px.scatter(
        car_data,
        x="odometer",  # Quilometragem (milhas)
        y="price",     # Preço (USD)
        color="condition",  # Diferenciar pontos pela condição do veículo
        hover_data=["model_year", "model", "fuel",
                    "type"],  # Informações extras no hover
        title="Relação entre Quilometragem e Preço dos Veículos",
        labels={
            "odometer": "Quilometragem (milhas)",
            "price": "Preço (USD)",
            "condition": "Condição",
            "cylinders": "Cilindros",
        },
    )

    # Personalizar layout
    fig.update_layout(
        title_font_size=20,
        xaxis_title_font_size=16,
        yaxis_title_font_size=16,
        xaxis=dict(title="Quilometragem (milhas)", tickformat=','),
        yaxis=dict(title="Preço (USD)", tickformat='$,.0f'),
        template="plotly_white",  # Tema do gráfico
    )

    # Exibir o gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

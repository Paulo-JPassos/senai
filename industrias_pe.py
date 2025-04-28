# Importação das bibliotecas necessárias
import streamlit as st
import pandas as pd
import plotly.express as px
import os
import datetime as dt

# Título do dashboard
st.title("Indústrias de Pernambuco")

# Caminho do arquivo CSV na mesma pasta
csv_file = "industrias_Pe.csv"

# Verifica se o arquivo CSV existe na mesma pasta
if os.path.exists(csv_file):
    # Lê o arquivo CSV em um DataFrame
    df = pd.read_csv(csv_file, encoding='windows-1252', sep=';')

    st.markdown("### Visão geral")

    # Exibe os dados carregados
    st.markdown("### Dados das indústrias de PE")
    st.dataframe(df.head(1000))

    # Filtros de seleção
    st.sidebar.header("Filtros")

    # Filtro multiselect para "Porte da Empresa"
    selected_porte = st.sidebar.multiselect(
        "Selecione o Porte da Empresa", 
        options=df['Porte da Empresa'].unique(),  # Exclui valores nulos se houver
        default=df['Porte da Empresa'].unique()
    )

    # Filtro multiselect para "Situação Cadastral"
    selected_situacao = st.sidebar.multiselect(
        "Situação Cadastral", 
        options=df['Situação Cadastral'].dropna().unique(),
        default=df['Situação Cadastral'].dropna().unique()
    )

    # Filtro selectbox para "Nome Fantasia" (você pode mudar a coluna conforme necessário)
    selected_nome_fantasia = st.sidebar.selectbox(
        "Selecione o Nome Fantasia", 
        options=df['Nome Fantasia'].dropna().unique(),  # Exclui valores nulos
        index=0  # Define o primeiro item como padrão
    )

    # Aplicando os filtros no DataFrame
    df_filtered = df[
        (df['Porte da Empresa'].isin(selected_porte)) &  # Filtra pelo porte da empresa
        (df['Situação Cadastral'].isin(selected_situacao)) &  # Filtra pela situação cadastral
        (df['Nome Fantasia'] == selected_nome_fantasia)  # Filtra pelo nome fantasia
    ]

    # Exibindo o DataFrame filtrado
    st.write("DataFrame filtrado:", df_filtered)
    st.dataframe(df_filtered)  # Exibindo o DataFrame filtrado com formatação de tabela
else:
    # Caso o arquivo CSV não seja encontrado, exibe uma mensagem de erro
    st.error(f"O arquivo {csv_file} não foi encontrado.")

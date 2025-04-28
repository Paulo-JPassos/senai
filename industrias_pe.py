# Importação das bibliotecas necessárias
import streamlit as st
import pandas as pd
import plotly.express as px
import os
import datetime as dt

# Título do dashboard
st.title("Indústrias de Pernambuco")

# Caminho do arquivo CSV na mesma pasta
csv_file = "Industrias_Pernambuco.csv"

# Verifica se o arquivo CSV existe na mesma pasta
if os.path.exists(csv_file):
    # Lê o arquivo CSV em um DataFrame
    df = pd.read_csv(csv_file, encoding='windows-1252', sep=';')

    st.markdown("### Visão geral")

     # Exibe os dados carregados
    st.markdown("### Dados das indústrias de PE")
    st.dataframe(df.head(10))
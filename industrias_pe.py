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
    st.dataframe(df.head(1000))

     # Filtros de seleção

    st.write(df.head(1000))

    st.sidebar.header("Filtros")

### Multiselect
#selected_porte = st.sidebar.multiselect(
 #   "Selecione o Porte da Empresa", 
  #  options=df['Porte da Empresa'].dropna().unique(),  # Exclui valores nulos se houver
   # default=df['Porte da Empresa'].dropna().unique()
#)

#selected_situacao = st.sidebar.multiselect(
 #   "Situação Cadastral", 
  #  options=df['Situação Cadastral'].dropna().unique(),
   # default=df['Situação Cadastral'].dropna().unique()
#)

### Selectbox

# Remover espaços extras nos nomes das colunas
#df.columns = df.columns.str.strip()

# Verificar se as colunas necessárias existem
if 'Porte da Empresa' in df.columns and 'Situação Cadastral' in df.columns:
    # Seleção do "Porte da Empresa"
    selected_porte = st.sidebar.selectbox(
        "Selecione o Porte da Empresa", 
        options=sorted(df['Porte da Empresa'].dropna().unique())  # Ordena alfabeticamente
    )

    # Seleção da "Situação Cadastral"
    selected_situacao = st.sidebar.selectbox(
        "Situação Cadastral", 
        options=sorted(df['Situação Cadastral'].dropna().unique())  # Ordena alfabeticamente
    )

    # Aplicando os filtros no DataFrame
    df_filtered = df[
        (df['Porte da Empresa'] == selected_porte) &
        (df['Situação Cadastral'] == selected_situacao)
    ]
    
    # Exibindo o DataFrame filtrado
    st.write("DataFrame filtrado:", df_filtered)
    
    # Exibindo o DataFrame filtrado com uma formatação de tabela
    st.dataframe(df_filtered)
    
else:
    # Caso alguma coluna necessária não seja encontrada, exibe uma mensagem de erro
    st.error("As colunas 'Porte da Empresa' e/ou 'Situação Cadastral' não foram encontradas no DataFrame!")

st.dataframe(df_filtered)

    #selected_store = st.sidebar.multiselect("Selecione o Porte da Empresa", options=df['Porte da Empresa'].unique(), default=df['Porte da Empresa'].unique())
    #selected_model = st.sidebar.multiselect("Situação Cadastral", options=df['Situação Cadastral'].unique(), default=df['Situação Cadastral'].unique())
    #selected_date_range = st.sidebar.date_input("Selecione o Nome", [df['Nome Fantasia'].min(), df['Nome Fantasia'].max()])


#python -m streamlit run industrias_pe.py
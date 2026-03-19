import polars as pl
import streamlit as st

df = pl.read_csv("Dados/vendas_ficticias.csv") 

total_vendido = df["quantidade"].sum()

st.set_page_config(
    layout="wide", # Faz o site usar a tela toda
)

st.title("Mostrando total de produtos vendidos! 🫶🏾🤡")

col1, = st.columns(1) #cria uma coluna, e precisa da "," no final do col1

with col1:
    st.metric(label="Quantidade Total de produtos vendidos: ", value= total_vendido)


st.divider() # Uma linha sutil para separar as seções
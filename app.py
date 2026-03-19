import pandas as pd
import streamlit as st

# carregar dados
df = pd.read_csv("vendas_ficticias.csv")

# calcular média
media_valor_venda = df["valor"].mean()

# mostrar resultado
st.title("Dashboard de Vendas")
st.metric("Média de valor por venda", f"R$ {media_valor_venda:.2f}")

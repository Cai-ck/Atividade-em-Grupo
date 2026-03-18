import polars as pl
import streamlit as st

df = pl.read_csv("Dados/vendas_ficticias.csv") 

total_vendido = df["quantidade"].sum()

st.write(f"O total de produtos vendidos é: {total_vendido}")   
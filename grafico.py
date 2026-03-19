import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Análise de Vendas", layout="wide")

st.title("Painel de Vendas – Visualização")

# --- CARREGAR DADOS ---
@st.cache_data
def load_data():
    return pd.read_csv("vendas_ficticias.csv")

df = load_data()

st.subheader("📄 Prévia dos Dados")
st.dataframe(df)

# Escolha da coluna para agrupar
colunas_categorias = df.select_dtypes(include=["object"]).columns.tolist()

st.subheader("⚙️ Configurações")
categoria = st.selectbox("Escolha a categoria para agrupar:", colunas_categorias)

# Agrupamento
agrupado = df.groupby(categoria).sum(numeric_only=True).reset_index()

# --- GRÁFICO DE PIZZA ---
st.subheader("🥧 Gráfico de Pizza")
fig_pizza = px.pie(
    agrupado,
    names=categoria,
    values=agrupado.columns[1],  
    hole=0.3,
)
st.plotly_chart(fig_pizza, use_container_width=True)

# --- GRÁFICO DE BARRAS ---
st.subheader("Gráfico de Barras")
fig_bar = px.bar(
    agrupado,
    x=categoria,
    y=agrupado.columns[1],
    text_auto=True,
)
st.plotly_chart(fig_bar, use_container_width=True)
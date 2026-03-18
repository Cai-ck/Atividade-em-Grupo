import polars as pl


df = pl.read_csv("Dados/vendas_ficticias.csv") 

total_vendido = df["quantidade"].sum()

print(f"O total de produtos vendidos é: {total_vendido}")
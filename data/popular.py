import pandas as pd
import os
import sqlite3

conn = sqlite3.connect("db.sqlite3")

caminho_atual = os.getcwd()
caminho_final = caminho_atual.replace("\\","/")

df = pd.read_csv(caminho_atual+"/data/ferramentas.csv")

df.columns = ["tituloProduto","preco","descricao"
               ,"imgProduto","catProduto",
               "classProduto","exibirNome"]

df.to_sql("api_produto", conn, if_exists="append", index=False)

conn.close()

print("Dados inseridos com sucessos")
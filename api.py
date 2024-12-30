# Criando uma API com Python, usando flask

from flask import Flask
import pandas as pd
import openpyxl

tabela = pd.read_excel("Vendas - Dez.xlsx")
print(tabela)

app = Flask(__name__) #cria o site

@app.route("/") # Decorador -> diz em qual link a função vai rodar
def home():
  return 'Bem Vindo a minha API de vendas!'


@app.route("/faturamento") # Decorador -> diz em qual link a função vai rodar
def fat():
    faturamento = float(tabela["Valor Final"].sum())
    return {'faturamento': faturamento}

@app.route("/vendas/produtos") 
def vendas_produtos():
    tabela_vendas_produtos = tabela[["Produto", "Valor Final"]].groupby("Produto").sum()
    dic_vendas_produtos = tabela_vendas_produtos.to_dict()
    return dic_vendas_produtos

@app.route("/vendas/produtos/umprodutoespecifico/<produto>") 
def fat_produto(produto):
    tabela_vendas_produtos = tabela[["Produto", "Valor Final"]].groupby("Produto").sum()

    if produto in tabela_vendas_produtos.index:
        vendas_produto = tabela_vendas_produtos.loc[produto]
        dic_vendas_produto = vendas_produto.to_dict()
        return dic_vendas_produto
    else:
        return {produto: 'Not Found'}
    
    

app.run() #coloca o site no ar
# no replet use host="0.0.0.0"
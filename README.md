# API-vendas

API de Vendas com Python
Bem-vindo à API de Vendas, desenvolvida com Python usando o Flask. Esta API permite acessar dados de vendas a partir de um arquivo Excel. Abaixo, você encontrará as instruções de como configurar e usar a API.

Funcionalidades
Home: Uma mensagem de boas-vindas.

Faturamento Total: Retorna o faturamento total das vendas.

Vendas por Produto: Retorna o faturamento agrupado por produto.

Vendas de um Produto Específico: Retorna o faturamento de um produto específico.

Como Usar
1. Pré-requisitos
Python 3.x instalado

Bibliotecas necessárias: Flask, pandas, openpyxl

4. Executar a API
Coloque o arquivo Vendas - Dez.xlsx no mesmo diretório do código ou coloque o caminho quando for utilizar o comando pd.read do pandas.

5. Endpoints
Home: GET /

Exemplo de resposta: Bem Vindo a minha API de vendas!

Faturamento Total: GET /faturamento

Exemplo de resposta: {"faturamento": 12345.67}

Vendas por Produto: GET /vendas/produtos

exemplo da respostas: { "Produto A": 250, "Produto B": 450} 
# Previsão de preço do Petróleo Brent a partir dos dados do IPEA
*Pós Tech FIAP - Data Analytics - Tech Challenge 04*

Grupo 42:
 - Vinicius Mathias Lacrimanti Pignataro
 - Gabriel Krieguer Zarichen
 - Georgia Oliveira Paixão Duarte
 - Mauricio Alexandre De Souza Junior
 - Renan Da Silva Leão

### Objetivos Principais:

- Criar um dashboard interativo com uma ferramente à escolha, contendo um storytelling com no mínimo 4 insights relevantes sobre a variação do preço do petróleo, levando em consideração situações geopolíticas, crises econômicas, etc;
- Criar um modelo de Machine Learning que faça a previsão do preço diariamente, contemplando também o código trabalhado;
- Criar um plano para fazer o deploy em produção do modelo, com as ferramentas necessárias;
- Fazer um MVP (Mininum Viable Product) do modelo em produção utilizando o Streamlit.

### 

**Dados do preço do Petróleo**

Os dados utilizados podem ser obtidos diretamente no site do IPEA, [clicando aqui](http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view).

**main/**

- `Base de dados`: Pasta contendo o CSV com os dados utilizados no projeto;
- `assets`: Pasta contendo as imagens e CSS utilizados no projeto;
- `pages`: Pasta contendo as páginas do aplicativo do Streamlit;
- `util`: Pasta contendo a definição de layout utilizada no projeto;
- `Table_extract.ipynb`: Notebook extraindo os dados do site do IPEA e salvando-os em um arquivo CSV;
- `Tech_Challenge_04.ipynb`: Notebook contendo a análise exploratória dos dados e a previsão;
- `Tech_Challenge_04.pbix`: Dashboard utilizado para uma melhor análise dos dados.
- `main.py`: Arquivo principal do aplicativo do Streamlit;
- `requirements.txt`: Arquivo com todas as dependências necessárias para o projeto.

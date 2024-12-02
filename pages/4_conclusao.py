import streamlit as st


def main():
    st.subheader(':red[Conclusão]')

    st.subheader(':gray[Resultados e Eficiência do Prophet na Previsão]', divider='red')

    st.markdown('''
                Dos resultados obtidos, observamos um WMAPE de aproximadamente 7% \\ao analisarmos os últimos 10 anos, havendo variação conforme aumento ou diminuição do tempo analisado no modelo, o que indica que o mesmo está apresentando uma precisão de aproximadamente 93% nas previsões realizadas. Esse valor é considerado satisfatório, pois está relativamente baixo, sugerindo que o modelo é eficaz em capturar a maior parte da variabilidade nos dados e em prever com precisão o preço do petróleo. \n 

                Em suma, os resultados obtidos demonstram a robustez e a precisão do Prophet na tarefa de prever o preço do petróleo, considerando as características dos dados temporais e sazonais.
                ''')
    
    st.subheader(':gray[Melhorias futuras]', divider='red')

    st.markdown('''
                Apesar de o modelo Prophet ter apresentado resultados satisfatórios, ainda há espaço para melhorias e otimizações futuras. Algumas sugestões de aprimoramento incluem: \n

                :one: **Ajuste de Hiperparâmetros**: O Prophet possui diversos hiperparâmetros que podem ser ajustados para melhorar a precisão das previsões. Realizar uma busca sistemática de hiperparâmetros pode ajudar a encontrar a combinação ideal para o conjunto de dados analisado. \n
                ''')

main()  
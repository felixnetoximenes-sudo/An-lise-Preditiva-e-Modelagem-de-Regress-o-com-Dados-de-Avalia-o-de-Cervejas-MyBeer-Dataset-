# 🍺 Análise Preditiva e Regressão Linear com Dados de Cerveja (MyBeer Dataset)

Este projeto apresenta um pipeline completo de Ciência de Dados e Machine Learning de ponta a ponta. O objetivo principal foi desenvolver um modelo estatístico capaz de prever a nota ponderada de mercado de uma cerveja (`global_weighted_rating_score`) utilizando como base apenas a sua nota global simplificada (`global_rating_score`).

No contexto de negócios, este modelo comprova como métricas simplificadas de feedback do cliente podem automatizar processos de avaliação de catálogo e reduzir custos com pesquisas de mercado complexas.

## 🚀 Tecnologias e Bibliotecas Utilizadas
* **Python** (Linguagem base)
* **Pandas**: Limpeza de dados, tratamento de valores nulos e remoção de duplicadas.
* **NumPy**: Manipulação de matrizes e formatação de arrays bidimensionais para o modelo.
* **Scikit-Learn**: Divisão do conjunto de dados (`train_test_split`), treinamento do algoritmo (`LinearRegression`) e validação de métricas de erro.
* **Matplotlib**: Visualização de dados e plotagem da linha de tendência gerada pela IA.

## 📊 Performance e Resultados da IA
Após o treinamento e a separação dos dados de teste (3% do conjunto de dados), o modelo apresentou resultados de altíssima confiabilidade:

* **Coeficiente de Determinação (R²):** **84,06%**  
  * *Significado prático:* A nota global simplificada é capaz de explicar mais de 84% de toda a variação da nota ponderada final da cerveja.
* **Erro Médio Absoluto (MAE):** **0,0620 pontos**  
  * *Significado prático:* Quando a Inteligência Artificial tenta prever o sucesso de uma cerveja, ela comete um erro médio de apenas 0,06 pontos para mais ou para menos em uma escala de notas.

## 🛠️ Como o Código Funciona (Pipeline)
1. **Tratamento de Dados:** Leitura do arquivo CSV, preenchimento de lacunas (`fillna`), remoção de registros repetidos (`drop_duplicates`) e renomeação de colunas estratégicas.
2. **Engenharia de Recursos:** Conversão das séries do Pandas para arrays NumPy e aplicação do ajuste de forma (`.reshape(-1, 1)`) exigido pelo Scikit-Learn.
3. **Treinamento:** Divisão rigorosa em dados de treino e teste com reprodutibilidade garantida (`random_state=42`).
4. **Visualização:** Geração de um gráfico de dispersão (*scatter plot*) comparando os dados reais do mercado com a linha de predição gerada pela Regressão Linear.

---
*Projeto desenvolvido para fins de portfólio de Ciência de Dados e Inteligência Artificial.*

# Roteiro do Video - Previsao de Rendimento de Safra com ML
# Duracao total: ate 5 minutos

---

## [0:00 - 0:30] Abertura

> [Mostrar o README do GitHub na tela]

"Ola! Somos o grupo composto por Joao Rafael, Leticia, Matheus, Rivando e Tales,
alunos do curso de IA da FIAP. Neste video vamos apresentar nosso projeto da
Fase 5: a previsao de rendimento de safra utilizando Machine Learning, desenvolvido
para a FarmTech Solutions."

"O objetivo do projeto e analisar dados climaticos de uma fazenda de medio porte,
com 200 hectares, e prever o rendimento das culturas usando modelos de regressao
supervisionada, alem de explorar tendencias de produtividade com clusterizacao."

---

## [0:30 - 1:30] Dataset e Analise Exploratoria

> [Mostrar as celulas: df.head(), df.info()]

"Nosso dataset possui 156 registros de 4 culturas: Cocoa, Rice, Rubber e Oil Palm,
com 39 registros para cada uma. As variaveis climaticas sao: precipitacao,
umidade especifica, umidade relativa e temperatura, todas medidas a 2 metros do
solo. A variavel alvo e o Yield, ou seja, o rendimento em toneladas por hectare."

> [Mostrar: df.describe() e checagem de nulos]

"Na analise exploratoria, verificamos que o dataset nao possui nenhum valor nulo
e nenhuma linha duplicada, o que e otimo para a qualidade da nossa analise."

> [Mostrar: grafico de barras das culturas]

"A distribuicao das culturas e perfeitamente balanceada, com 39 registros cada."

> [Mostrar: histogramas das variaveis]

"Nos histogramas, podemos observar a distribuicao de cada variavel numerica.
A precipitacao varia bastante, enquanto temperatura e umidade ficam em faixas
mais concentradas."

> [Mostrar: heatmap de correlacao]

"No heatmap de correlacao, um ponto interessante: as variaveis climaticas
individualmente tem correlacao muito baixa com o rendimento. A precipitacao
tem correlacao de apenas 0,02, e as demais praticamente zero. Isso indica que
o tipo de cultura e o fator mais determinante para o rendimento."

> [Mostrar: boxplots de Yield por cultura]

"Nos boxplots, fica claro que o Oil Palm tem rendimento muito superior as demais,
com media de 175 mil toneladas por hectare, enquanto Cocoa e Rubber ficam abaixo
de 10 mil. O Rice fica em uma faixa intermediaria, em torno de 32 mil."

---

## [1:30 - 2:30] Clusterizacao (Aprendizado Nao Supervisionado)

> [Mostrar: grafico do cotovelo]

"Para identificar tendencias nos dados, aplicamos o algoritmo KMeans. Usamos o
metodo do cotovelo para encontrar o numero ideal de clusters. Observamos que a
partir de k igual a 4, a reducao da inercia diminui significativamente, entao
escolhemos 4 clusters."

> [Mostrar: graficos PCA - clusters vs culturas reais]

"Usando PCA para reduzir a dimensionalidade, conseguimos visualizar os clusters
em 2D. Os dois componentes principais explicam 74,76 porcento da variancia total
dos dados."

> [Mostrar: tabela de medias por cluster]

"Analisando as caracteristicas de cada cluster, o Cluster 0 concentrou 26 dos 26
registros de Oil Palm, com rendimento medio de 178 mil. Isso mostra que o Oil Palm
tem um perfil climatico bem distinto das demais culturas. Ja os clusters 1, 2 e 3
misturaram as culturas Cocoa, Rice e Rubber, indicando que essas tres compartilham
condicoes climaticas semelhantes."

> [Mostrar: grafico de outliers]

"Na deteccao de outliers, pelo metodo IQR encontramos 12 outliers na temperatura
e 35 no rendimento. Porem, pelo Z-Score com limiar de 3, nenhum outlier foi
detectado. Isso sugere que os valores extremos nao sao tao discrepantes assim,
e sim uma variacao natural entre culturas com faixas de rendimento muito
diferentes."

---

## [2:30 - 3:30] Modelos Preditivos

> [Mostrar: celulas de pre-processamento]

"Para a etapa de regressao supervisionada, preparamos os dados com One-Hot Encoding
para a variavel categorica Crop, dividimos em 80 porcento treino e 20 porcento
teste, e padronizamos as features com StandardScaler. Ficamos com 124 registros
para treino e 32 para teste."

"Treinamos cinco modelos diferentes:"

> [Mostrar cada modelo enquanto fala]

"Primeiro, a Regressao Linear, nosso modelo base, simples e interpretavel.
Segundo, o Ridge Regression, que adiciona regularizacao L2 para evitar
overfitting. Terceiro, o Lasso Regression, com regularizacao L1 que pode
zerar coeficientes menos relevantes. Quarto, o Random Forest, um ensemble
de arvores de decisao. E quinto, o Gradient Boosting, que constroi arvores
sequencialmente, corrigindo erros das anteriores."

---

## [3:30 - 4:30] Comparacao de Resultados

> [Mostrar: tabela comparativa dos modelos]

"Avaliamos cada modelo com as metricas R-quadrado, MAE, MSE, RMSE e validacao
cruzada com 5 folds. Os resultados foram excelentes para todos os modelos."

"O melhor modelo foi a Regressao Linear, com R-quadrado de 0,9950 e RMSE de
4.394. O Lasso ficou muito proximo, com R-quadrado de 0,9950 e RMSE de 4.425.
O modelo com pior desempenho relativo foi o Gradient Boosting, com R-quadrado
de 0,9905 e RMSE de 6.061. Mas mesmo assim, todos os modelos tiveram
R-quadrado acima de 0,99, o que e muito bom."

"Na validacao cruzada, todos os modelos mantiveram R-quadrado medio acima de
0,98, confirmando que nao ha overfitting significativo."

> [Mostrar: graficos de barras comparando R2 e RMSE]

> [Mostrar: grafico de feature importance / coeficientes]

"Analisando os coeficientes da Regressao Linear, a variavel mais relevante e
Crop Oil Palm, com coeficiente de 52.260, o que faz sentido ja que o Oil Palm
tem o maior rendimento. Em seguida, a umidade especifica e a temperatura
tambem exercem influencia consideravel."

> [Mostrar: grafico Real vs Previsto]

"No grafico de valores reais versus previstos, os pontos estao muito proximos
da linha diagonal, confirmando a alta precisao do modelo."

---

## [4:30 - 5:00] Conclusao

"Em conclusao, conseguimos construir modelos com excelente capacidade de previsao
do rendimento das safras. A Regressao Linear se destacou como o melhor modelo,
com R-quadrado de 0,995, o que significa que explica 99,5 porcento da variacao
dos dados."

"Como pontos fortes, destacamos: a analise completa desde a exploracao dos dados
ate a comparacao de cinco algoritmos diferentes, a clusterizacao que revelou
padroes interessantes entre as culturas, e a alta acuracia de todos os modelos."

"Como limitacao, o dataset e relativamente pequeno, com 156 registros, e o fato
de a Regressao Linear ter superado os modelos mais complexos sugere que a relacao
entre as variaveis e o rendimento e predominantemente linear neste cenario."

"O codigo completo e a documentacao estao disponiveis no nosso repositorio
do GitHub. Obrigado pela atencao!"

> [Mostrar: link do repositorio na tela]

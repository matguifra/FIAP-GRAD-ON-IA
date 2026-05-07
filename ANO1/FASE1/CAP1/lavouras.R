#Vetor com os dados vindos do python
vetor_dados <- c(1.0, 0.0, 60.06, 148.2, 8000.0, 250.0, 1.56, 411.84, 168.48, 411.84, 12480.0, 312.0, 21.0, 0.0, 1261.26, 3112.2, 168000.0, 5250.0)

#Conversão do vetor em matriz, cada linha uma lavoura
matriz_dados <- matrix(vetor_dados, ncol = 6, byrow = TRUE)

#Conversão da matriz em um dataframe
lavouras <- as.data.frame(matriz_dados)

#Nomeando as colunas do dataframe
colnames(lavouras) <- c("area", "nitrogenio", "fosforo", "potassio", "agua_total", "irrigacao")

print(lavouras)
cat("\n") #pular uma linha para melhor visualização

estatisticas <- data.frame(
  area       = c(mean(lavouras$area)      , median(lavouras$area)      , sd(lavouras$area)),
  nitrogenio = c(mean(lavouras$nitrogenio), median(lavouras$nitrogenio), sd(lavouras$nitrogenio)),
  fosforo    = c(mean(lavouras$fosforo)   , median(lavouras$fosforo)   , sd(lavouras$fosforo)),
  potassio   = c(mean(lavouras$potassio)  , median(lavouras$potassio)  , sd(lavouras$potassio)),
  agua_total = c(mean(lavouras$agua_total), median(lavouras$agua_total), sd(lavouras$agua_total)),
  irrigacao  = c(mean(lavouras$irrigacao) , median(lavouras$irrigacao) , sd(lavouras$irrigacao))
)

rownames(estatisticas) <- c("Média", "Mediana", "Desvio padrão")

print(estatisticas)
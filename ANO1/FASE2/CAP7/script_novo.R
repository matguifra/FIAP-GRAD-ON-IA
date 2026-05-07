# JoaoRafaelGoncalvesRamos_RM567908_fase2_cap7
# LeticiaAngelimGuerra_RM567501_fase2_cap7
# MatheusGuimaraesFranca_RM567144_fase2_cap7
# RivandoBezerraCavalcantiNeto_RM568235_fase2_cap7
# TalesFerrazDeArrudaDomienikan_RM567483_fase2_cap7

# CARREGAR BIBLIOTECAS
library(readxl)
library(ggplot2)
library(dplyr)

# --- CARREGAMENTO DOS DADOS ---

# O arquivo de dados é carregado usando um caminho relativo.
# Isso garante que o script funcione em qualquer computador, 
# desde que o arquivo "tabela_formatada.xlsx" esteja na mesma pasta.
dados <- read_excel("tabela_formatada.xlsx")


# Abaixo, a linha original com caminho absoluto (foi desativada para garantir a portabilidade do código).
# dados <- read_excel("C:/Users/rivan/Estudos/FIAP/ATV2_7/tabela_formatada.xlsx"

# VISUALIZAR OS DADOS
head(dados)
str(dados)
summary(dados)

# ANÁLISE DA VARIÁVEL QUANTITATIVA CONTÍNUA: Área_Total_ha
area_total <- dados$Área_Total_ha

cat("=== ANÁLISE EXPLORATÓRIA - ÁREA TOTAL (HECTARES) ===\n")

# 1. MEDIDAS DE TENDÊNCIA CENTRAL
cat("\n1. MEDIDAS DE TENDÊNCIA CENTRAL:\n")
media <- mean(area_total)
mediana <- median(area_total)

cat("Média:", round(media, 2), "hectares\n")
cat("Mediana:", mediana, "hectares\n")

# 2. MEDIDAS DE DISPERSÃO
cat("\n2. MEDIDAS DE DISPERSÃO:\n")
variancia <- var(area_total)
desvio_padrao <- sd(area_total)
coef_variacao <- (desvio_padrao / media) * 100
amplitude <- max(area_total) - min(area_total)

cat("Variância:", round(variancia, 2), "\n")
cat("Desvio Padrão:", round(desvio_padrao, 2), "hectares\n")
cat("Coeficiente de Variação:", round(coef_variacao, 2), "%\n")
cat("Amplitude:", amplitude, "hectares\n")

# 3. MEDIDAS SEPARATRIZES
cat("\n3. MEDIDAS SEPARATRIZES:\n")
quartis <- quantile(area_total, probs = c(0.25, 0.5, 0.75))
decis <- quantile(area_total, probs = seq(0.1, 0.9, by = 0.1))

cat("Quartis:\n")
print(quartis)
cat("\nDecis (10% a 90%):\n")
print(decis)

# ==================================================
# ANÁLISE GRÁFICA DA VARIÁVEL QUANTITATIVA - GRÁFICOS BÁSICOS
# ==================================================

cat("\n4. ANÁLISE GRÁFICA - VARIÁVEL QUANTITATIVA\n")

# Histograma básico
hist(area_total, 
     main = "Distribuição da Área Total Plantada por Região",
     xlab = "Área (hectares)",
     ylab = "Frequência",
     col = "lightgreen",
     border = "darkgreen",
     breaks = 10)

# Boxplot básico
boxplot(area_total,
        main = "Boxplot - Área Total Plantada",
        ylab = "Área (hectares)",
        col = "lightblue",
        horizontal = TRUE)

# Gráfico de Densidade básico
plot(density(area_total),
     main = "Densidade da Área Total Plantada",
     xlab = "Área (hectares)",
     ylab = "Densidade",
     lwd = 2)
polygon(density(area_total), col = "lightcoral", border = "black")

# ==================================================
# GRÁFICOS APRIMORADOS COM ggplot2 - VARIÁVEL QUANTITATIVA
# ==================================================

cat("\n5. GRÁFICOS APRIMORADOS COM ggplot2\n")

# Histograma com ggplot2
ggplot(dados, aes(x = Área_Total_ha)) +
  geom_histogram(binwidth = 1000000, fill = "lightgreen", color = "darkgreen", alpha = 0.7) +
  geom_vline(aes(xintercept = mean(Área_Total_ha)), color = "red", linetype = "dashed", size = 1) +
  geom_vline(aes(xintercept = median(Área_Total_ha)), color = "blue", linetype = "dashed", size = 1) +
  labs(title = "Distribuição da Área Total Plantada - ggplot2",
       subtitle = "Linhas vermelha (média) e azul (mediana)",
       x = "Área (hectares)",
       y = "Frequência") +
  theme_minimal()

# Boxplot com ggplot2
ggplot(dados, aes(x = "", y = Área_Total_ha)) +
  geom_boxplot(fill = "lightblue", alpha = 0.7, outlier.color = "red", outlier.size = 3) +
  stat_summary(fun = mean, geom = "point", shape = 18, size = 3, color = "red") +
  labs(title = "Boxplot - Área Total Plantada - ggplot2",
       subtitle = "Ponto vermelho = Média | Pontos vermelhos = Outliers",
       y = "Área (hectares)") +
  theme_minimal()

# Densidade com ggplot2
ggplot(dados, aes(x = Área_Total_ha)) +
  geom_density(fill = "lightcoral", alpha = 0.7) +
  geom_vline(aes(xintercept = mean(Área_Total_ha)), color = "red", linetype = "dashed") +
  labs(title = "Densidade da Área Total Plantada - ggplot2",
       x = "Área (hectares)",
       y = "Densidade") +
  theme_minimal()

# Gráfico Q-Q para normalidade
ggplot(dados, aes(sample = Área_Total_ha)) +
  stat_qq(color = "blue") +
  stat_qq_line(color = "red") +
  labs(title = "Gráfico Q-Q - Verificação de Normalidade",
       x = "Quantis Teóricos",
       y = "Quantis Amostrais") +
  theme_minimal()

# ==================================================
# ANÁLISE DE OUTLIERS - VARIÁVEL QUANTITATIVA
# ==================================================

cat("\n=== ANÁLISE DE OUTLIERS - ÁREA TOTAL ===\n")

# Identificar outliers usando o método IQR
Q1 <- quantile(dados$Área_Total_ha, 0.25)
Q3 <- quantile(dados$Área_Total_ha, 0.75)
IQR <- Q3 - Q1
limite_inferior <- Q1 - 1.5 * IQR
limite_superior <- Q3 + 1.5 * IQR

outliers <- dados$Área_Total_ha[dados$Área_Total_ha < limite_inferior | dados$Área_Total_ha > limite_superior]
estados_outliers <- dados$`Região/Estado`[dados$Área_Total_ha %in% outliers]

cat("Limite inferior para outliers:", round(limite_inferior, 2), "\n")
cat("Limite superior para outliers:", round(limite_superior, 2), "\n")
cat("Número de outliers identificados:", length(outliers), "\n")

if(length(outliers) > 0) {
  cat("Outliers encontrados:\n")
  for(i in 1:length(outliers)) {
    cat(" -", estados_outliers[i], ":", round(outliers[i], 2), "hectares\n")
  }
} else {
  cat("Nenhum outlier identificado.\n")
}

# ==================================================
# ANÁLISE DA VARIÁVEL QUALITATIVA: Cultura_Principal
# ==================================================

cat("\n=== ANÁLISE DA VARIÁVEL QUALITATIVA - CULTURA PRINCIPAL ===\n")

cultura <- dados$Cultura_Principal

# Tabela de Frequências
freq_absoluta <- table(cultura)
freq_relativa <- prop.table(freq_absoluta) * 100

cat("Frequência Absoluta:\n")
print(freq_absoluta)
cat("\nFrequência Relativa (%):\n")
print(round(freq_relativa, 2))

# ==================================================
# GRÁFICOS BÁSICOS DA VARIÁVEL QUALITATIVA
# ==================================================

# Gráfico de Barras (vertical)
barplot(freq_absoluta,
        main = "Distribuição das Culturas Principais por Estado",
        xlab = "Cultura",
        ylab = "Número de Estados",
        col = "steelblue",
        ylim = c(0, max(freq_absoluta) + 2),
        las = 2)

# Gráfico de Pizza
pie(freq_relativa,
    main = "Distribuição Percentual das Culturas Principais",
    col = heat.colors(length(freq_relativa)),
    radius = 1,
    labels = paste0(names(freq_relativa), "\n", round(freq_relativa, 1), "%"))

# ==================================================
# GRÁFICOS APRIMORADOS COM ggplot2 - VARIÁVEL QUALITATIVA
# ==================================================

# Preparar dados para ggplot2
dados_cultura <- dados %>%
  count(Cultura_Principal) %>%
  arrange(desc(n)) %>%
  mutate(percentual = round(n/sum(n) * 100, 1))

# Gráfico de barras ordenado com ggplot2
ggplot(dados_cultura, aes(x = reorder(Cultura_Principal, n), y = n)) +
  geom_bar(stat = "identity", fill = "steelblue", alpha = 0.8) +
  geom_text(aes(label = paste0(n, " (", percentual, "%)")), 
            hjust = -0.1, size = 3.5, color = "black") +
  labs(title = "Distribuição das Culturas Principais - ggplot2",
       x = "Cultura",
       y = "Número de Estados") +
  coord_flip() +
  theme_minimal() +
  theme(axis.text.y = element_text(size = 10))

# Gráfico de pizza melhorado com ggplot2
ggplot(dados_cultura, aes(x = "", y = n, fill = Cultura_Principal)) +
  geom_bar(stat = "identity", width = 1) +
  coord_polar("y", start = 0) +
  geom_text(aes(label = paste0(Cultura_Principal, "\n", n, " (", percentual, "%)")), 
            position = position_stack(vjust = 0.5), size = 3.5) +
  labs(title = "Distribuição Percentual das Culturas Principais - ggplot2") +
  theme_void() +
  theme(legend.position = "none")

# Gráfico de waffle (alternativa ao pizza)
ggplot(dados_cultura, aes(fill = Cultura_Principal, values = n)) +
  geom_waffle(color = "white", size = 0.5, n_rows = 5) +
  labs(title = "Distribuição das Culturas - Gráfico de Waffle") +
  theme_void() +
  theme(legend.position = "bottom")

# ==================================================
# ANÁLISE DA VARIÁVEL QUALITATIVA ORDINAL: Porte_Produção
# ==================================================

cat("\n=== ANÁLISE DA VARIÁVEL QUALITATIVA ORDINAL - PORTE DE PRODUÇÃO ===\n")

porte <- dados$Porte_Produção
freq_porte <- table(porte)
freq_porte_rel <- prop.table(freq_porte) * 100

cat("Frequência do Porte de Produção:\n")
print(freq_porte)
cat("\nFrequência Relativa (%):\n")
print(round(freq_porte_rel, 2))

# Gráfico do Porte de Produção
porte_ordenado <- factor(porte, levels = c("Pequeno", "Médio", "Alto", "Muito Alto"))

ggplot(dados, aes(x = porte_ordenado)) +
  geom_bar(fill = "orange", alpha = 0.7) +
  geom_text(stat = 'count', aes(label = ..count..), vjust = -0.5) +
  labs(title = "Distribuição do Porte de Produção",
       x = "Porte de Produção",
       y = "Número de Estados") +
  theme_minimal()

# ==================================================
# ANÁLISES ADICIONAIS E CORRELAÇÕES
# ==================================================

cat("\n=== CORRELAÇÃO ENTRE ÁREA E NÚMERO DE PROPRIEDADES ===\n")
correlacao <- cor(dados$Propriedades, dados$Área_Total_ha)
cat("Coeficiente de Correlação:", round(correlacao, 3), "\n")

# Gráfico de dispersão com ggplot2
ggplot(dados, aes(x = Propriedades, y = Área_Total_ha)) +
  geom_point(size = 3, color = "blue", alpha = 0.7) +
  geom_smooth(method = "lm", color = "red", se = FALSE) +
  geom_text(aes(label = `Região/Estado`), vjust = -0.5, hjust = 0.5, size = 3) +
  labs(title = "Relação: Nº de Propriedades vs Área Total",
       subtitle = paste("Correlação:", round(correlacao, 3)),
       x = "Número de Propriedades",
       y = "Área Total (hectares)") +
  theme_minimal()

# ==================================================
# RESUMO ESTATÍSTICO COMPLETO E RELATÓRIO FINAL
# ==================================================

cat("\n=== RESUMO ESTATÍSTICO COMPLETO ===\n")
print(summary(dados))

cat("\n=== RELATÓRIO FINAL ===\n")
cat("• A variável quantitativa (Área Total) apresenta média de", round(media, 2), "hectares.\n")
cat("• O coeficiente de variação de", round(coef_variacao, 2), "% indica", 
    ifelse(coef_variacao > 30, "alta dispersão", "dispersão moderada"), "nos dados.\n")
cat("• Foram identificados", length(outliers), "outliers na variável área total.\n")
cat("• A cultura predominante é", names(which.max(freq_absoluta)), 
    "com", max(freq_absoluta), "estados.\n")
cat("• A correlação entre propriedades e área é", round(correlacao, 3), 
    ifelse(correlacao > 0.5, "(forte positiva)", "(moderada positiva)"), "\n")

# Salvar gráficos em alta qualidade
# ggsave("histograma_area.png", width = 10, height = 6, dpi = 300)
# ggsave("boxplot_area.png", width = 10, height = 6, dpi = 300)
# ggsave("barras_culturas.png", width = 10, height = 6, dpi = 300)

cat("\n=== ANÁLISE CONCLUÍDA ===\n")
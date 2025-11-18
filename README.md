GLOBAL SOLUTION – Sustentabilidade e Futuro do Trabalho
Grupo

Pedro Paulo Ferreira Agnelo D’Angelo – 567564

Gabriel Guimarães Oliveira – 567835

José Renato – 567225

- Objetivo do Projeto:

Este repositório apresenta uma solução voltada para eficiência energética em ambientes de trabalho (home office), alinhada ao tema Futuro do Trabalho e ao uso de práticas sustentáveis.

O foco é:
analisar o consumo energético do ambiente, identificar desperdícios, propor ajustes, demonstrar os ganhos ambientais e financeiros.

1. Coleta e Análise de Dados

Os dados contêm o consumo médio estimado de:
Monitor (20–30W)
Computador (250–450W)
Notebook (40–150W)
Roteador (8–12W)
Lâmpada (10–18W)
LED (5–10W)
Abajur (5–10W)

Arquivo: data/consumo_energetico.csv

A análise foi feita usando Python para:
calcular consumo total, identificar picos, detectar desperdícios, estimar custos mensais.


2. Conexão com o Futuro do Trabalho

O projeto propõe integrar uma assistente virtual (Alexa) configurada para: 
monitorar o consumo diário, desligar equipamentos automaticamente, sugerir rotinas otimizadas, apoiar decisões inteligentes sobre energia.
Essa automação reduz custos, aumenta sustentabilidade e integra tecnologia ao ambiente produtivo.


3. Desenvolvimento da Solução – Opção A (Análise de Dados)

A partir dos dados analisados, identificamos:
Desperdícios
Iluminação desnecessária
Carregadores sempre conectados
Roteador ligado 24h
Monitor em standby

Ajustes Propostos:
Usar apenas uma fonte de luz por vez
Remover carregadores ou usar régua com botão
Programar o roteador para desligar à noite
Configurar timers inteligentes via Alexa

Ganhos Ambientais:
Menor emissão de CO₂
Preservação de recursos não renováveis
Menor impacto sobre ecossistemas
Melhoria da qualidade do ar

Ganhos Econômicos:
Redução da conta de luz
Menor desgaste dos equipamentos
Estabilidade elétrica
Possibilidade de reinvestir a economia


4. Execução da Análise
python src/analise_consumo.py

import pandas as pd

# ======================================
# Leitura do arquivo CSV
# ======================================

df = pd.read_csv("data/consumo_energetico.csv")

print("\n===== ANÁLISE DE CONSUMO ENERGÉTICO =====\n")

# ======================================
# Consumo total estimado
# ======================================

consumo_total = df["Potencia_W"].sum()
print(f"Consumo total dos equipamentos: {consumo_total} W")

# ======================================
# Estimativa de custo mensal
# Fórmula:
# (potência W / 1000) * horas/dia * 30 * tarifa
# ======================================

TARIFA = 0.95  # valor médio em R$/kWh – pode ajustar se quiser

df["Custo_mensal_R$"] = (df["Potencia_W"] / 1000) * df["Horas_dia"] * 30 * TARIFA

print("\n--- Custo mensal estimado por equipamento (R$) ---")
print(df[["Equipamento", "Custo_mensal_R$"]])

print("\nCusto mensal TOTAL estimado (R$): {:.2f}".format(df["Custo_mensal_R$"].sum()))

# ======================================
# Identificação de desperdícios
# ======================================

print("\n===== Desperdícios Identificados =====")

if df["Horas_dia"].max() > 12:
    print("- Algum equipamento parece ficar ligado mais de 12h/dia → pode haver desperdício.")

if (df["Equipamento"].str.contains("Roteador", case=False)).any():
    print("- Roteador ligado 24h → desligar à noite reduz custo.")

if (df["Equipamento"].str.contains("Lâmpada|LED|Abajur", case=False)).any():
    print("- Iluminação pode estar ligada sem necessidade.")

# ======================================
# Recomendações automáticas
# ======================================

print("\n===== Recomendações de Economia =====")
print("- Desligar o roteador durante a madrugada.")
print("- Usar apenas uma fonte de luz por vez (teto, abajur ou LED).")
print("- Remover carregadores da tomada quando não estiverem em uso.")
print("- Programar Alexa ou automação para desligar equipamentos em horários fixos.")
print("- Evitar deixar monitor em standby por longos períodos.")

print("\n===== FIM DA ANÁLISE =====\n")

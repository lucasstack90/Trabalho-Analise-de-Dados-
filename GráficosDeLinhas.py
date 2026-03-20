import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregando o seu arquivo
df = pd.read_csv('precos_carros_brasil.csv')

# 2. Filtrando os dados
# Vamos focar na marca 'Fiat' para a linha não ficar confusa com todas as marcas juntas
df_fiat = df[df['brand'] == 'Fiat']

# 3. Preparando os dados para a linha
# Agrupamos pelo ano do modelo e calculamos a média de preço para cada ano
evolucao_fiat = df_fiat.groupby('year_model')['avg_price_brl'].mean().sort_index()

# 4. Criando o gráfico de linhas
plt.figure(figsize=(10, 6))
evolucao_fiat.plot(kind='line', marker='o', color='red', linewidth=2)

# 5. Customização
plt.title('Tendência de Preços Médios - FIAT (Por Ano do Modelo)', fontsize=14)
plt.xlabel('Ano do Modelo')
plt.ylabel('Preço Médio (R$)')
plt.grid(True, linestyle='--', alpha=0.7) # Adiciona uma grade suave
plt.show()
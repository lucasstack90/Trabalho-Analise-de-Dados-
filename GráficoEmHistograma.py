import matplotlib.pyplot as plt
import pandas as pd

# Nota: o arquivo precos_carros_brasil.csv deve existir no diretório
precos_carros_brasil = pd.read_csv('precos_carros_brasil.csv')

# Use uma coluna numérica do seu DataFrame para o histograma
# Por exemplo, 'year_of_reference'. Certifique-se de remover valores NA para plotagem.
# Você pode substituir 'year_of_reference' por qualquer outra coluna numérica do seu CSV.
data_from_csv = precos_carros_brasil['year_of_reference'].dropna()

# Crie a figura e um único subplot
fig, ax = plt.subplots(1, 1, figsize=(8, 6), tight_layout=True)

# Plote o histograma
ax.hist(data_from_csv, bins=20)
ax.set_title('Histograma de Ano_de_referência') # Título adicionado para clareza
ax.set_xlabel('Ano de Referência')
ax.set_ylabel('Frequência')

# Mostre o resultado
plt.show()
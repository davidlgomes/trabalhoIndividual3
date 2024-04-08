import pandas as pd
import matplotlib.pyplot as plt
# URL do arquivo Excel hospedado no GitHub
file_path = 'https://raw.githubusercontent.com/davidlgomes/trabalhoIndividual3/main/planilhaTrab3.xlsx'

# Carregar o arquivo Excel para um DataFrame
df = pd.read_excel(file_path, engine='openpyxl', header=None, names=['Dia', 'Horas Trabalhadas', 'Bugs Corrigidos', 'Tarefas Concluídas'], skiprows=1)

# 1. Visualização das primeiras linhas do DataFrame
print("Primeiras linhas do DataFrame:")
print(df.head())

# 2. Resumo estatístico das variáveis numéricas
print("\nResumo estatístico das variáveis numéricas:")
print(df.describe())

# 3. Verificação de valores nulos
print("\nValores nulos no DataFrame:")
print(df.isnull().sum())

# Calcular métricas solicitadas
total_horas_trabalhadas = df['Horas Trabalhadas'].sum()
media_horas_trabalhadas = df['Horas Trabalhadas'].mean()
total_bugs_corrigidos = df['Bugs Corrigidos'].sum()
media_bugs_corrigidos = df['Bugs Corrigidos'].mean()
total_tarefas_concluidas = df['Tarefas Concluídas'].sum()
media_tarefas_concluidas = df['Tarefas Concluídas'].mean()

resolucoes_por_dia = df.groupby('Dia')['Bugs Corrigidos'].sum()
print(resolucoes_por_dia)
# Calcular produtividade diária (tarefas concluídas por hora)
df['Produtividade Diária'] = df['Tarefas Concluídas'] / df['Horas Trabalhadas']

# Calcular média de produtividade diária
media_produtividade_diaria = df['Produtividade Diária'].mean()

tarefas_por_dia_semana = df.groupby('Dia')['Tarefas Concluídas'].sum()

print(f'Total de Horas Trabalhadas: {total_horas_trabalhadas}')
print(f'Média Diária de Horas Trabalhadas: {media_horas_trabalhadas}')
print(f'Total de Bugs Corrigidos: {total_bugs_corrigidos}')
print(f'Média Diária de Bugs Corrigidos: {media_bugs_corrigidos}')
print(f'Total de Tarefas Concluídas: {total_tarefas_concluidas}')
print(f'Média Diária de Tarefas Concluídas: {media_tarefas_concluidas}')

plt.figure(figsize=(14, 10))

# Cores para os gráficos de pizza
cores_pizza = plt.cm.tab10.colors

# Criar os gráficos
# Gráfico de barras para mostrar o total e média diária de horas trabalhadas, bugs corrigidos e tarefas concluídas
cores_medias=['lightblue', 'lightgreen', 'lightsalmon']
cores_totais=['blue', 'green', 'red']
plt.subplot(2, 2, 1)
df[['Horas Trabalhadas', 'Bugs Corrigidos', 'Tarefas Concluídas']].sum().plot(kind='bar', color=cores_totais)
plt.bar(0, media_horas_trabalhadas, color=cores_medias[0], label=f'Média Horas Trabalhadas: {media_horas_trabalhadas:.2f}')
plt.bar(1, media_bugs_corrigidos, color=cores_medias[1], label=f'Média Bugs Corrigidos: {media_bugs_corrigidos:.2f}')
plt.bar(2, media_tarefas_concluidas, color=cores_medias[2], label=f'Média Tarefas Concluídas: {media_tarefas_concluidas:.2f}')
plt.title('Total e Média Diária')
plt.ylabel('Quantidade')
plt.xticks(ticks=[0, 1, 2], labels=['Horas Trabalhadas', 'Bugs Corrigidos', 'Tarefas Concluídas'])
plt.legend(loc='upper right')  # Mover a legenda para uma posição que não se sobreponha aos dados

# Gráfico de pizza para mostrar a distribuição das tarefas concluídas por dia da semana
plt.subplot(2, 2, 2)
plt.pie(tarefas_por_dia_semana, labels=tarefas_por_dia_semana.index, autopct='%1.1f%%', colors=cores_pizza)
plt.title('Distribuição das Tarefas Concluídas por Dia da Semana')

# Gráfico de linha para mostrar a evolução diária de horas trabalhadas, bugs corrigidos e tarefas concluídas
plt.figure(figsize=(25, 10))
plt.subplot(2, 2, 3)
plt.plot(df['Dia'], df['Horas Trabalhadas'], marker='o', color='blue', label='Horas Trabalhadas')
plt.plot(df['Dia'], df['Bugs Corrigidos'], marker='o', color='green', label='Bugs Corrigidos')
plt.plot(df['Dia'], df['Tarefas Concluídas'], marker='o', color='red', label='Tarefas Concluídas')
plt.plot(df['Dia'], df['Produtividade Diária'], marker='o', color='purple', label='Produtividade Diária')
plt.title('Evolução Diária')
plt.xlabel('Dia')
plt.ylabel('Quantidade')
plt.legend(loc='upper right')  # Mover a legenda para uma posição que não se sobreponha aos dados

plt.tight_layout()
plt.show() 


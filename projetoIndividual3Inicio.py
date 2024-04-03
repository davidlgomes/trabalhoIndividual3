import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados do arquivo Excel
df = pd.read_excel('planilhaTrab3.xlsx', header=None, names=['Dia', 'Horas Trabalhadas', 'Bugs Corrigidos', 'Tarefas Concluídas'], skiprows=1)

# Calcular métricas solicitadas
total_horas_trabalhadas = df['Horas Trabalhadas'].sum()
media_horas_trabalhadas = df['Horas Trabalhadas'].mean()
total_bugs_corrigidos = df['Bugs Corrigidos'].sum()
media_bugs_corrigidos = df['Bugs Corrigidos'].mean()
total_tarefas_concluidas = df['Tarefas Concluídas'].sum()
media_tarefas_concluidas = df['Tarefas Concluídas'].mean()
produtividade_diaria = df['Tarefas Concluídas'] / df['Horas Trabalhadas']

# Adicionar métricas ao dataframe
df['Produtividade Diária'] = produtividade_diaria

# Imprimir métricas
print(f'Total de Horas Trabalhadas: {total_horas_trabalhadas}')
print(f'Média Diária de Horas Trabalhadas: {media_horas_trabalhadas}')
print(f'Total de Bugs Corrigidos: {total_bugs_corrigidos}')
print(f'Média Diária de Bugs Corrigidos: {media_bugs_corrigidos}')
print(f'Total de Tarefas Concluídas: {total_tarefas_concluidas}')
print(f'Média Diária de Tarefas Concluídas: {media_tarefas_concluidas}')

# Visualização dos resultados
plt.figure(figsize=(14, 10))

# Gráfico de barras para mostrar o total de horas trabalhadas, bugs corrigidos e tarefas concluídas
plt.subplot(2, 2, 1)
df[['Horas Trabalhadas', 'Bugs Corrigidos', 'Tarefas Concluídas']].sum().plot(kind='bar', color=['blue', 'green', 'red'])
plt.title('Total por Métrica')
plt.ylabel('Quantidade')

# Gráfico de pizza para mostrar a distribuição de horas trabalhadas, bugs corrigidos e tarefas concluídas
plt.subplot(2, 2, 2)
df[['Horas Trabalhadas', 'Bugs Corrigidos', 'Tarefas Concluídas']].sum().plot(kind='pie', autopct='%1.1f%%', colors=['blue', 'green', 'red'])
plt.title('Distribuição por Métrica')

# Gráfico de linha para mostrar a evolução diária de horas trabalhadas, bugs corrigidos e tarefas concluídas
plt.subplot(2, 1, 2)
plt.plot(df['Dia'], df['Horas Trabalhadas'], marker='o', color='blue', label='Horas Trabalhadas')
plt.plot(df['Dia'], df['Bugs Corrigidos'], marker='o', color='green', label='Bugs Corrigidos')
plt.plot(df['Dia'], df['Tarefas Concluídas'], marker='o', color='red', label='Tarefas Concluídas')
plt.title('Progresso Diário')
plt.xlabel('Dia')
plt.ylabel('Quantidade')
plt.legend()

plt.tight_layout()
plt.show()

# trabalhoIndividual3
Trabalho consta no link aberto <a href="https://colab.research.google.com/drive/1FJEXZnYbG8PDcAIWinouqRKvnP5qGRet?usp=sharing"/>  

# Instruções para Executar a Análise de Dados

O notebook que você acessou está disponível no Google Colab e pode ser executado facilmente. Siga estas instruções para executá-lo:

1. **Abrir o Notebook**: Clique no link fornecido para acessar o notebook no Google Colab.

2. **Copiar para o Google Drive (Opcional)**: Se desejar, você pode copiar o notebook para o seu Google Drive clicando em "Arquivo" > "Salvar uma cópia no Google Drive". Isso permite que você faça edições e mantenha uma cópia pessoal do notebook.

3. **Executar as Células**: Após abrir o notebook, você verá o código dividido em células. Cada célula pode ser executada separadamente. Clique na célula que deseja executar e pressione Shift + Enter ou clique no botão "Executar" ao lado da célula.

4. **Executar Todas as Células (Opcional)**: Se preferir, você pode executar todas as células de uma vez clicando em "Ambiente de Execução" > "Executar tudo", ou aperte Ctrl+F9.

5. **Visualizar Resultados**: À medida que você executa as células, você verá os resultados das operações, como gráficos, tabelas ou saídas de texto, diretamente abaixo das células correspondentes.

6. **Interagir com o Notebook**: Após a execução, você pode interagir com o notebook conforme desejar. Você pode editar o código, adicionar novas células, fazer anotações e muito mais.

7. **Salvar Suas Alterações (Opcional)**: Se você fez alterações no notebook e deseja salvá-las, vá para "Arquivo" > "Salvar" ou "Salvar uma cópia no Google Drive".


# Importações necessárias para análise de dados e visualização

Neste notebook, vamos utilizar algumas bibliotecas populares para análise de dados e visualização. Abaixo estão as importações necessárias:


# Pandas
O Pandas é uma biblioteca de código aberto amplamente utilizada para análise de dados em Python.
Ele fornece estruturas de dados poderosas e flexíveis para facilitar a manipulação e análise de dados.

```import pandas as pd ```

# Matplotlib
Matplotlib é uma biblioteca de visualização de dados em Python, que produz gráficos de alta qualidade em diversos formatos.
Ele permite a criação de gráficos estáticos, interativos e animados.
```import matplotlib.pyplot as plt```

#Google Colab (drive)
Google Colab é uma plataforma de pesquisa de código aberto do Google para aprendizado de máquina.
Vem com diversas bibliotecas pré-instaladas e integração com o Google Drive para armazenamento e acesso a arquivos.
```from google.colab import drive```

# URL do arquivo Excel hospedado no GitHub
```
file_path = 'https://raw.githubusercontent.com/davidlgomes/trabalhoIndividual3/main/planilhaTrab3.xlsx'
``` 

# Carregar o arquivo Excel para um DataFrame
```
df = pd.read_excel(file_path, engine='openpyxl', header=None, names=['Dia', 'Horas Trabalhadas', 'Bugs Corrigidos', 'Tarefas Concluídas'], skiprows=1)
```
# Análise Exploratória
### 1. Visualização das primeiras linhas do DataFrame
```
print("Primeiras linhas do DataFrame:")
print(df.head())
```
### 2. Resumo estatístico das variáveis numéricas
```
print("\nResumo estatístico das variáveis numéricas:")
print(df.describe())
```
### 3. Verificação de valores nulos
```
print("\nValores nulos no DataFrame:")
print(df.isnull().sum())
```

##A análise exploratória de dados (AED) é uma etapa fundamental no processo de análise de dados, na qual os dados são explorados para entender sua estrutura, padrões, distribuições e possíveis problemas. Ela envolve a aplicação de diversas técnicas e métodos para resumir e visualizar os dados, ajudando a extrair insights valiosos e a tomar decisões informadas.

As três etapas de análise exploratória mencionadas são as seguintes:

1. Visualização das primeiras linhas do DataFrame: Esta etapa permite obter uma rápida visão geral dos dados, incluindo os nomes das colunas e os primeiros registros. Ajuda a entender a estrutura dos dados e verificar se foram carregados corretamente.

2. Resumo estatístico das variáveis numéricas: Nesta etapa, são calculadas estatísticas descritivas básicas, como média, mediana, desvio padrão, mínimo e máximo, para cada variável numérica. Isso fornece insights sobre a distribuição e a variabilidade dos dados, identificando valores atípicos e anomalias.

3. Verificação de valores nulos: Esta etapa é importante para identificar se há valores ausentes ou nulos nos dados. Valores ausentes podem afetar a análise e podem precisar ser tratados, seja removendo as linhas correspondentes, preenchendo-os com valores substitutos ou aplicando técnicas mais avançadas de imputação de dados.

# Fazer análise exploratória é crucial para compreender os dados que estamos lidando, identificar problemas nos dados e guiar o processo de pré-processamento e modelagem. Ela nos ajuda a formular hipóteses, a direcionar a investigação e a tomar decisões sobre os próximos passos na análise de dados. Além disso, contribui para a comunicação eficaz dos resultados e insights obtidos.

## Métricas Calculadas

- **Total de Horas Trabalhadas:** {total_horas_trabalhadas}
- **Média Diária de Horas Trabalhadas:** {media_horas_trabalhadas:.2f}
- **Total de Bugs Corrigidos:** {total_bugs_corrigidos}
- **Média Diária de Bugs Corrigidos:** {media_bugs_corrigidos:.2f}
- **Total de Tarefas Concluídas:** {total_tarefas_concluidas}
- **Média Diária de Tarefas Concluídas:** {media_tarefas_concluidas:.2f}
- **Média de Produtividade Diária:** {media_produtividade_diaria:.2f}

## Distribuição das Tarefas Concluídas por Dia da Semana

```
print(tarefas_por_dia_semana)
```

# Imprimir métricas calculadas

Para imprimir as métricas calculadas, você pode utilizar o seguinte código:

# Imprimir métricas calculadas
```
print(f'Total de Horas Trabalhadas: {total_horas_trabalhadas}')
print(f'Média Diária de Horas Trabalhadas: {media_horas_trabalhadas}')
print(f'Total de Bugs Corrigidos: {total_bugs_corrigidos}')
print(f'Média Diária de Bugs Corrigidos: {media_bugs_corrigidos}')
print(f'Total de Tarefas Concluídas: {total_tarefas_concluidas}')
print(f'Média Diária de Tarefas Concluídas: {media_tarefas_concluidas}')
```

## Visualização de Dados

### Total e Média Diária

O gráfico de barras apresenta o total e a média diária das horas trabalhadas, bugs corrigidos e tarefas concluídas.


### Distribuição das Tarefas Concluídas por Dia da Semana

O gráfico de pizza mostra a distribuição das tarefas concluídas por dia da semana.


### Evolução Diária

O gráfico de linha apresenta a evolução diária das horas trabalhadas, bugs corrigidos, tarefas concluídas e produtividade diária.





![image](https://github.com/davidlgomes/trabalhoIndividual3/assets/47571290/b202ddfd-6409-42a6-9c10-bed6a09a2aee)
![image](https://github.com/davidlgomes/trabalhoIndividual3/assets/47571290/486e1df7-31ae-43ef-bf05-477e895133e6)
![image](https://github.com/davidlgomes/trabalhoIndividual3/assets/47571290/624a8479-cfca-4f83-88d6-a22985ffc3c1)
![image](https://github.com/davidlgomes/trabalhoIndividual3/assets/47571290/43ccc3e4-ee65-4b21-8bb8-84eee6079439)
![image](https://github.com/davidlgomes/trabalhoIndividual3/assets/47571290/a9a97ecd-9c54-41fb-8523-28b309c7faa8)
![image](https://github.com/davidlgomes/trabalhoIndividual3/assets/47571290/e80fffd2-2bb4-4b5c-baa0-43c703f3eec1)
![image](https://github.com/davidlgomes/trabalhoIndividual3/assets/47571290/59fe3746-5872-4902-bc1c-14bdeed63190)
![image](https://github.com/davidlgomes/trabalhoIndividual3/assets/47571290/324943ed-1a4c-462c-adb3-46d6b4152f65)
![image](https://github.com/davidlgomes/trabalhoIndividual3/assets/47571290/99cab74c-3945-4d9b-ab5d-a9792734e12c)
![image](https://github.com/davidlgomes/trabalhoIndividual3/assets/47571290/ce133012-e267-4b9a-a708-f6050fdc7ed8)

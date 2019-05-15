# -*- coding: utf-8 -*-
"""
Universidade Federal do Amazonas
Instituto de Computacao
Leandro Galvao

Analise dos dados do questionario socio-economico e demografico (QSED) aplicado aos calouros 2018
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats

#----------------------
# Leitura de arquivos
#----------------------

# Planilha de dados cadastrais do SIE
df = pd.read_csv('historico2012a2017_wei.csv', sep=';', encoding = "ISO-8859-1")


#----------------------
# Estatisticas basicas sobre sexo dos participantes
#----------------------

# Filtra apenas alunos que sairam do curso: 'Formados' ou 'Desistentes'
df_evadidos = df.loc[df['FORMA_EVASAO2'].isin(['Formado', 'Desistente'])]

# Conta valores de cada situacao
masc = np.count_nonzero(df_evadidos.SEXO == 'M')
fem  = np.count_nonzero(df_evadidos.SEXO == 'F')

# Homens evadidos (formados + desistentes)
print("No. de homens (calouros 2018): ", masc)
masc_pc = round(masc/(masc + fem) * 100, 1)
print("% de homens (calouros 2018): ", masc_pc)

# Mulheres evadidas (formadas + desistentes)
print("No. de mulheres (calouros 2018): ", fem)
fem_pc = round(fem/(masc + fem) * 100, 1)
print("% de mulheres (calouros 2018): ", fem_pc)

# Homens formados
masc_form = np.count_nonzero(df_evadidos.loc[df['FORMA_EVASAO2'].isin(['Formado'])].SEXO == 'M')

# Homens desistentes
masc_des = np.count_nonzero(df_evadidos.loc[df['FORMA_EVASAO2'].isin(['Desistente'])].SEXO == 'M')

# Mulheres formadas
fem_form = np.count_nonzero(df_evadidos.loc[df['FORMA_EVASAO2'].isin(['Formado'])].SEXO == 'F')

# Mulheres desistentes
fem_des = np.count_nonzero(df_evadidos.loc[df['FORMA_EVASAO2'].isin(['Desistente'])].SEXO == 'F')


#----------------------
# Plotagem
#----------------------

# Prepara grafico de barras
names = ['Homens', 'Mulheres']    # nome das colunas
values = [masc, fem]       # contagem absoluta das colunas
y_pos = np.arange(len(names))

# Frequencia relativa
values = values / np.sum(values)

# Plota grafico de barras
plt.bar(y_pos, values)
plt.xticks(y_pos, names)
plt.ylabel('Proporção do grupo (%)')
plt.title('Distribuição por sexo (calouros 2018)')
#plt.ylim(0, 0.7)

# Primeiro salva-se a figura, para depois exibi-la
plt.savefig('calouros2018_sexo.png', transparent=True)
plt.show()




#----------------------
# Plotagem - modificacao sugerida pela Elaine
#----------------------

# data to plot
n_groups = 2

font = {'family' : 'sans-serif',
        'weight' : 'medium',
        'size'   : 12}

plt.rc('font', **font)


sexo_names = ['Homens', 'Mulheres']    # nome das colunas
values_form = np.array([masc_form, fem_form])       # contagem absoluta das colunas
values_des  = np.array([masc_des, fem_des])       # contagem absoluta das colunas

total = np.sum(values_form + values_des)

# Frequencia relativa
values_form = values_form / total
values_des = values_des / total

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 1

rects1 = plt.bar(index, values_form*100, bar_width,
                    alpha=opacity,
                    color='springgreen',
                    label='Formados',
                    zorder=5)

rects2 = plt.bar(index + bar_width, values_des*100, bar_width,
            alpha=opacity,
            color='lightcoral',
            label='Desistentes',
            zorder=5)

#ax.grid(zorder=0)

#plt.xlabel('Sexo')
plt.ylabel('Proporção do grupo (%)')
plt.title('Proporção de formados e desistentes por sexo')
plt.xticks(index + bar_width/2, ('Homens', 'Mulheres'))
plt.ylim(top=80)

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
#                '%d' % int(round(height, 3)*100) + '.',
                str(round(height, 1))[:4] + '%' if height >= 10 else str(round(height, 1))[:3] + '%',
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.legend()

plt.tight_layout()
plt.show()


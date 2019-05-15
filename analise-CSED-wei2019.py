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
df = pd.read_csv('resultados2018_CSED_wei2019_anonimo.csv', sep=';', encoding = "ISO-8859-1")


#----------------------
# Estatisticas basicas sobre SEXO dos participantes
#----------------------

# Conta valores de cada situacao
masc = np.count_nonzero(df.SEXO == 'M')
fem  = np.count_nonzero(df.SEXO == 'F')

print("No. de homens (calouros 2018): ", masc)
masc_pc = round(masc / (masc + fem) * 100, 1)
print("% de homens (calouros 2018): ", masc_pc)

print("No. de mulheres (calouros 2018): ", fem)
fem_pc = round(fem / (masc + fem) * 100, 1)
print("% de mulheres (calouros 2018): ", fem_pc)



#----------------------
# Plotagem
#----------------------

# Prepara grafico de barras
names = ['M', 'F']    # nome das colunas
values = [masc, fem]       # contagem absoluta das colunas
y_pos = np.arange(len(names))

# Frequencia relativa
values = values / np.sum(values)

# Plota grafico de barras
plt.bar(y_pos, values)
plt.xticks(y_pos, names)
plt.title('Distribuição por sexo (calouros 2018)')
#plt.ylim(0, 0.7)

# Primeiro salva-se a figura, para depois exibi-la
plt.savefig('calouros2018_sexo.png', transparent=True)
plt.show()


#----------------------
# Plotagem - modificacao sugerida pela Elaine
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
plt.title('Distribuição por sexo (calouros 2018)')
#plt.ylim(0, 0.7)

# Primeiro salva-se a figura, para depois exibi-la
plt.savefig('calouros2018_sexo.png', transparent=True)
plt.show()


#----------------------
# Estatisticas basicas sobre COTA dos participantes
#----------------------

# Conta valores de cada situacao
cotaAC = np.count_nonzero(df.COTA == 'AC')
cotaRE = np.count_nonzero(df.COTA == 'Renda')
cotaNR = np.count_nonzero(df.COTA == 'NRenda')

print("No. de Cota AC (calouros 2018): ", cotaAC)
cotaAC_pc = round(cotaAC / (cotaAC + cotaRE + cotaNR) * 100, 1)
print("% de Cota AC (calouros 2018): ", cotaAC_pc)

print("No. de Cota Renda (calouros 2018): ", cotaRE)
cotaRE_pc = round(cotaRE / (cotaAC + cotaRE + cotaNR) * 100, 1)
print("% de Cota Renda (calouros 2018): ", cotaRE_pc)

print("No. de Cota NRenda (calouros 2018): ", cotaNR)
cotaNR_pc = round(cotaNR / (cotaAC + cotaRE + cotaNR) * 100, 1)
print("% de Cota NRenda (calouros 2018): ", cotaNR_pc)


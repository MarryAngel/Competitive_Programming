# Problema: [1064] Positivos e Média
# Dificuldade: Iniciante - Nível 2
# Autor: Maria Angélica Krüger Miranda

val1 = float(input())
val2 = float(input())
val3 = float(input())
val4 = float(input())
val5 = float(input())
val6 = float(input())

qtd_positivos = 0
soma = 0

if val1 >0:
    qtd_positivos += 1
    soma += val1
if val2 >0:
    qtd_positivos += 1
    soma += val2
if val3 >0:
    qtd_positivos += 1
    soma += val3
if val4 >0:
    qtd_positivos += 1
    soma += val4
if val5 >0:
    qtd_positivos += 1
    soma += val5
if val6 >0:
    qtd_positivos += 1
    soma += val6
    
print(f"{qtd_positivos} valores positivos")
print(f"{(soma/qtd_positivos):.1f}")
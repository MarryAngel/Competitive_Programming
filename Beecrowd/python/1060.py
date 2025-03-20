# Problema: [1060] Números Positivos
# Dificuldade: Iniciante - Nível 1
# Autor: Maria Angélica Krüger Miranda

val1 = float(input())
val2 = float(input())
val3 = float(input())
val4 = float(input())
val5 = float(input())
val6 = float(input())

qtd_positivos = 0

if val1 >0:
    qtd_positivos += 1
if val2 >0:
    qtd_positivos += 1
if val3 >0:
    qtd_positivos += 1
if val4 >0:
    qtd_positivos += 1
if val5 >0:
    qtd_positivos += 1
if val6 >0:
    qtd_positivos += 1
    
print(f"{qtd_positivos} valores positivos")
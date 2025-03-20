# Problema: [1065] Pares entre Cinco Números
# Dificuldade: Iniciante - Nível 1
# Autor: Maria Angélica Krüger Miranda

val1 = float(input())
val2 = float(input())
val3 = float(input())
val4 = float(input())
val5 = float(input())


qtd_pares = 0

if val1 % 2 == 0:
    qtd_pares += 1
if val2 % 2 == 0:
    qtd_pares += 1
if val3 % 2 == 0:
    qtd_pares += 1
if val4 % 2 == 0:
    qtd_pares += 1
if val5 % 2 == 0:
    qtd_pares += 1
    
print(f"{qtd_pares} valores pares")

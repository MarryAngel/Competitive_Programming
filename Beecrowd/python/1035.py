# Problema: [1035] Teste de Seleção 1
# Dificuldade: Iniciante - Nível 2
# Autor: Maria Angélica Krüger Miranda

A, B, C, D = map(int, input().split())

if (B > C) and (D > A) and (C + D > A + B) and (C > 0 and D > 0 ) and (A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")


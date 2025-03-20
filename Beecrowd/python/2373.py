# Problema: [2373] Garçom
# Dificuldade: AD-HOC - Nível 1
# Autor: Maria Angélica Krüger Miranda

qtd_bandejas = int(input())

copos_quebrados = 0

for i in range(qtd_bandejas):
    latas, copos = map(int, input().split())

    if latas > copos:
        copos_quebrados += copos
        
print(copos_quebrados)
# Problema: [1153] Fatorial Simples
# Dificuldade: Iniciante - Nível 1
# Autor: Maria Angélica Krüger Miranda

valor = int(input())

fatorial = valor

for i in range(1, valor):
    fatorial *= (valor-i)
    
print(fatorial)
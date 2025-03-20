# Problema: [1044] Múltiplos
# Dificuldade: Iniciante - Nível 2
# Autor: Maria Angélica Krüger Miranda

a, b = map(int, input().split())

if b % a == 0 or a % b == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')

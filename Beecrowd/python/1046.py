# Problema: [1046] Tempo de Jogo
# Dificuldade: Iniciante - Nível 2
# Autor: Maria Angélica Krüger Miranda

inicio, fim = map(int, input().split())

if (fim - inicio) == 0:
    print("O JOGO DUROU 24 HORA(S)")
elif (fim - inicio) < 0:
    print(f"O JOGO DUROU {(fim-inicio)+24} HORA(S)")
else:
    print(f"O JOGO DUROU {fim-inicio} HORA(S)")
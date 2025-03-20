# Problema: [1329] Cara ou Coroa
# Dificuldade: AD-HOC - Nível 2
# Autor: Maria Angélica Krüger Miranda

while True:
    qtd_partidas = int(input())
    if qtd_partidas == 0:
        break
    
    resultados = input().split()
    win_maria = 0
    win_joao = 0
    
    for i in range(qtd_partidas):
        if int(resultados[i]) == 0:
            win_maria += 1
        else:
            win_joao += 1
            
    print("Mary won {} times and John won {} times".format(win_maria, win_joao))
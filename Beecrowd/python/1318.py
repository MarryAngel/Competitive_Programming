# Problema: [1318] Bilhetes Falsos
# Dificuldade: AD-HOC - Nível 3
# Autor: Maria Angélica Krüger Miranda

while True:
    qtd_originais, qtd_pessoas = input().split()
    qtd_originais, qtd_pessoas = int(qtd_originais), int(qtd_pessoas)
    
    if qtd_originais == 0 and qtd_pessoas == 0:
        break
    
    bilhetes = input().split()
    originais = []
    falsos = 0
    clones = []
    
    for bilhete in bilhetes:
        if bilhete not in originais:
            originais.append(bilhete)
        elif bilhete not in clones:
            clones.append(bilhete)
            falsos += 1
            
    print(falsos)
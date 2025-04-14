# Problema: [1101] Sequência de Números e Soma
# Dificuldade: Iniciante - Nível 4
# Autor: Maria Angélica Krüger Miranda

while True:
    m, n = input().split()
    m, n = int(m), int(n)
    
    if m <= 0 or n <= 0:
        break

    if m > n:
        maior = m
        menor = n
    else: 
        maior = n
        menor = m
        
    soma = 0
    saida = ""
    
    for i in range(menor, maior + 1):
        saida += f"{i} "
        soma += i
    
    print(f"{saida}Sum={soma}")
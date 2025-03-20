# # Problema: [2718] ALuzes de Natal
# # Dificuldade: Iniciante - Nível 5
# # Autor: Maria Angélica Krüger Miranda

qtd_grupos = int(input())

for i in range(qtd_grupos):
    decimal = int(input())
    sequencia = 0
    max_sequencia = 0
    
    while decimal > 0:
        resto = decimal % 2
        decimal = decimal // 2
        if resto == 0:
            sequencia = 0 
        else:
            sequencia += 1
            if sequencia > max_sequencia:
                max_sequencia = sequencia
    
    print(max_sequencia)
    
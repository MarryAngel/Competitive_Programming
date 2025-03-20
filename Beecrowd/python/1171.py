# Problema: [1171] Frequência de Números
# Dificuldade: AD-HOC - Nível 3
# Autor: Maria Angélica Krüger Miranda

qtd_valores = int(input())

repeticoes = [0]*2001

for i in range(qtd_valores):
    valor = int(input())
    repeticoes[valor] += 1  
  
for i in range(2001):
    if repeticoes[i] != 0:
        print("{} aparece {} vez(es)".format(i, repeticoes[i]))

        
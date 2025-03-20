# Problema: [1010] Cálculo Simples
# Dificuldade: Iniciante - Nível 3
# Autor: Maria Angélica Krüger Miranda

id1, qtd1, valor1 = map(float, input().split()) 
id2, qtd2, valor2 = map(float, input().split())
total=(qtd1*valor1)+(qtd2*valor2)
print(f"VALOR A PAGAR: R$ {total:.2f}")
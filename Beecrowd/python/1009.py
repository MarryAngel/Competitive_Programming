# Problema: [1009] Salário com Bônus
# Dificuldade: Iniciante - Nível 2
# Autor: Maria Angélica Krüger Miranda

nome, salario, vendas = input(), float(input()), float(input())
total=(vendas*0.15)+salario
print(f"TOTAL = R$ {total:.2f}")
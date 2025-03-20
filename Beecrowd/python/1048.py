# Problema: [1048] Aumento de Salário
# Dificuldade: Iniciante - Nível 2
# Autor: Maria Angélica Krüger Miranda

salario = float(input())
reajuste = 0

if salario <= 400.00:
    reajuste = 0.15
elif salario <= 800.00:
    reajuste = 0.12
elif salario <= 1200.00:
    reajuste = 0.10
elif salario <= 2000.00:
    reajuste = 0.07
else:
    reajuste = 0.04
 
reajuste_ganho = salario * reajuste
novo_salario = salario + reajuste_ganho
    
print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste_ganho:.2f}")
print(f"Em percentual: {int(reajuste*100)} %")
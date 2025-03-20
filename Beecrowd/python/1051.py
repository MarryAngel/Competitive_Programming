# Problema: [1051] Imposto de Renda
# Dificuldade: Iniciante - Nível 2
# Autor: Maria Angélica Krüger Miranda

salario = float(input())

if salario <= 2000.00:
    print("Isento")
elif salario <= 3000.00:
    print(f"R$ {((salario - 2000.00)*0.08):.2f}")
elif salario <= 4500.00:
    print(f"R$ {((salario - 3000.00)*0.18 + 1000.00*0.08):.2f}")
else:
    print(f"R$ {((salario-4500.00)*0.28 + 1500.00*0.18 + 1000.00*0.08):.2f}")
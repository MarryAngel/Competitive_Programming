# Problema: [2434] Saldo do Vovô
# Dificuldade: AD-HOC - Nível 1
# Autor: Maria Angélica Krüger Miranda

n_dias, saldo_inicial = input().split()

menor_saldo = int(saldo_inicial)
saldo_atual = int(saldo_inicial)

for i in range(int(n_dias)):
    movimentacao = int(input())
    saldo_atual += movimentacao
    if saldo_atual < menor_saldo:
        menor_saldo = saldo_atual

print(f"{menor_saldo}")
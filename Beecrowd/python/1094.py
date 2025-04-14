# Problema: [1094] Experiências
# Dificuldade: Iniciante - Nível 3
# Autor: Maria Angélica Krüger Miranda

qtd_testes = int(input())

coelhos, ratos, sapos = 0, 0, 0
qtd_cobaias = 0

for i in range(qtd_testes):
    quantia, tipo = input().split()
    quantia = int(quantia)
    qtd_cobaias += quantia
    if tipo == 'C':
        coelhos += quantia
    elif tipo == 'R':
        ratos += quantia
    elif tipo == 'S':
        sapos += quantia
        
print(f"Total: {qtd_cobaias} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {coelhos * 100 / qtd_cobaias:.2f} %")
print(f"Percentual de ratos: {ratos * 100 / qtd_cobaias:.2f} %")
print(f"Percentual de sapos: {sapos * 100 / qtd_cobaias:.2f} %")
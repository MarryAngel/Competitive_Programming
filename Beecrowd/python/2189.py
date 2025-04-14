# Problema: [2189] Quermesse
# Dificuldade: Ad-Hoc - Nível 1
# Autor: Maria Angélica Krüger Miranda

def sorteio(ordem: list[str]) -> int:
    for i in range(len(ordem)):
        if int(ordem[i]) == i+1:
            return int(ordem[i])

teste = 1

while True:
    qtd_participantes = int(input())
    if qtd_participantes == 0:
        break
    ordem_entrada = input().split()
    vencedor = sorteio(ordem_entrada)
    print(f"Teste {teste}")
    print(f"{vencedor}\n")
    teste += 1
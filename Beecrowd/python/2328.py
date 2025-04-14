# Problema: [2328] Qual Triângulo
# Dificuldade: AD-HOC - Nível 1
# Autor: Maria Angélica Krüger Miranda

def processar_estoque(n_divisoes: int, divisoes: list) -> int:
    estoque = 0
    for i in range(n_divisoes):
        estoque += int(divisoes[i])
    estoque = estoque - n_divisoes
    return estoque

def resolver_estoque():
    n_divisoes = int(input())
    divisoes = input().split()
    estoque = processar_estoque(n_divisoes, divisoes)
    print(estoque)

if __name__ == "__main__":
    resolver_estoque()
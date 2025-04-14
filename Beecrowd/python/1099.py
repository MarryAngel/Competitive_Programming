# Problema: [1099] Soma de Ímpares Consecutivos II
# Dificuldade: Iniciante - Nível 1
# Autor: Maria Angélica Krüger Miranda

def somar_impares(x: int, y: int) -> int:
    soma = 0
    if x > y:
        maior, menor = x, y
    else:
        maior, menor = y, x
    for i in range(menor+1, maior):
        if i % 2 != 0:
            soma += i
    return soma

def resolver():
    qtd_casos = int(input())
    for i in range(qtd_casos):
        x, y = map(int, input().split())
        soma = somar_impares(x, y)
        print(soma)
    
if __name__ == "__main__":
    resolver()

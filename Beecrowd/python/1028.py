# Problema: [1028] - Figurinhas
# Dificuldade: Matemática - Nível 3
# Autor: Maria Angélica Krüger Miranda

def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a%b)

def main():
    qtd_casos = int(input())
    for caso in range(qtd_casos):
        a, b = map(int, input().split())
        max_pilha = mdc(a, b)
        print(max_pilha)

if __name__ == '__main__':
    main()
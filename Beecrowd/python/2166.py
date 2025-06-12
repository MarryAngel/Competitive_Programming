# Problema: [2166] Raiz Quadrada de 2
# Dificuldade: Iniciante - Nível 1
# Autor: Maria Angélica Krüger Miranda

def fracao_periodica_continuada(n_repeticoes):
    if n_repeticoes == 0:
        return 0
    else:
        return 1/(2 + fracao_periodica_continuada(n_repeticoes - 1))

def main():
    n_repeticoes = int(input())
    raiz = 1.0 + fracao_periodica_continuada(n_repeticoes)
    print(f"{raiz:.10f}")

if __name__ == '__main__':
    main()
# Problmea: [1222] Concurso de Contos
# Dificuldade: Strings - Nível 6
# Autor: Maria Angélica Krüger Miranda

def resolver(qtd_palavras, max_linhas, max_caracteres, conto):
    palavras = conto.split()
    qtd_paginas = 1
    qtd_linhas = 1
    qtd_caracteres = 0
    
    for palavra in palavras:
        tamanho = len(palavra)
        if qtd_caracteres == 0:
            qtd_caracteres += tamanho
        elif qtd_caracteres + tamanho + 1 <= max_caracteres:
            qtd_caracteres += tamanho + 1
        else:
            qtd_linhas += 1
            qtd_caracteres = tamanho
            if qtd_linhas > max_linhas:
                qtd_paginas += 1
                qtd_linhas = 1    
                
    return qtd_paginas

def main():
    try:
        while True:
            qtd_palavras, max_linhas, max_caracteres = map(int, input().split())
            conto = input()
            min_paginas = resolver(qtd_palavras, max_linhas, max_caracteres, conto)
            print(min_paginas)
    except EOFError:
        return

if __name__ == "__main__":
    main()
# Problmea: [1260] Espécies de Madeira
# Dificuldade: Estruturas e Bibliotecas - Nível 5
# Autor: Maria Angélica Krüger Miranda

def resolver(dic_arvores, total):
    for arvore in sorted(dic_arvores.keys()):
        print(f"{arvore} {100 * dic_arvores[arvore] / total:.4f}")
    
def main():
    qtd_casos = int(input())
    input()
   
    for caso in range(qtd_casos):
        lista_arvores = {}
        total_arvores = 0
        while True:
            try:
                arvore = input()
            except EOFError:
                break
            if arvore == "":
                break
            total_arvores += 1
            if arvore not in lista_arvores:
                lista_arvores[arvore] = 1
            else:
                lista_arvores[arvore] += 1
        resolver(lista_arvores, total_arvores)
        if caso < qtd_casos - 1:
            print()

if __name__ == "__main__":
    main()
# Problmea: [2729] Lista de Compras
# Dificuldade: Estruturas e Bibliotecas - Nível 4
# Autor: Maria Angélica Krüger Miranda

def main():
    qtd_casos = int(input())
    for caso in range(qtd_casos):
        lista_compras = input().split()
        lista_reduzida = set()
        for item in lista_compras:
            lista_reduzida.add(item)
        lista_reduzida = sorted(lista_reduzida)
        print(" ".join(lista_reduzida))

if __name__ == "__main__":
    main()
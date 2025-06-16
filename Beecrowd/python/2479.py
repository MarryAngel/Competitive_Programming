# Problema: [2479] Ordenando a Lista de Crianças do Papai Noel
# Dificuldade: AD-HOC - Nível 1
# Autor: Maria Angélica Krüger Miranda


def selection_sort_string(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

def main():
    qtd_criancas = int(input())
    nomes = []
    boas = 0
    mas = 0
    for i in range(qtd_criancas):
        comportamento, nome = input().split()
        if comportamento == '+':
            boas += 1
        else:
            mas += 1
        nomes.append(nome)
    nomes_ordenados = selection_sort_string(nomes)
    print(*nomes_ordenados, sep = '\n')
    print(f"Se comportaram: {boas} | Nao se comportaram: {mas}")

if __name__ == '__main__':
    main()
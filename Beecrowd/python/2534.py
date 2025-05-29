# Problema: [2534] Exame Geral
# Dificuldade: Iniciante - Nível 2
# Autor: Maria Angélica Krüger Miranda


def selection_sort(arr: list) -> list:
    n_elements = len(arr)
    for i in range(n_elements-1):
        min_index = i
        for j in range(i+1, n_elements):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def main():
    while True:
        try:
            n_habitantes, n_casos = map(int, input().split())
        except EOFError:
            break
        notas = []
        for i in range(n_habitantes):
            nota = int(input())
            notas.append(nota)
        notas_ordenadas = selection_sort(notas.copy())
        notas_ordenadas = notas_ordenadas[::-1]
        for i in range(n_casos):
            index = int(input())
            print(notas_ordenadas[index-1])
       


if __name__ == '__main__':
    main()
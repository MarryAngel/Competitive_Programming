# Problema: [1042] Sort Simples
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
    entrance = list(map(int, input().split()))
    ordered_list = selection_sort(entrance.copy())
    print(*ordered_list, sep='\n')
    print()
    print(*entrance, sep='\n')

if __name__ == '__main__':
    main()
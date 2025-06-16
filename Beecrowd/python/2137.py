# Problema: [2137] A Biblioteca do Senhor Severino
# Dificuldade: Strings - Nível 1
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
            n_livros = int(input())
        except EOFError:
            break
        code_livros = []
        for i in range(n_livros):
            codigo = int(input())
            code_livros.append(codigo)
       
        code_livros_ordenados = selection_sort(code_livros.copy())
        # transformar para string de tamanho 4 e completando com zeros a esquerda
        code_livros_ordenados = [str(codigo).zfill(4) for codigo in code_livros_ordenados]
        print(*code_livros_ordenados, sep='\n')

if __name__ == '__main__':
    main()
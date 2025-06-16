# Problema: [2381] Lista de Chamada
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
    qtd_alunos, index = map(int, input().split())
    alunos = []
    for i in range(qtd_alunos):
        aluno = input()
        alunos.append(aluno)
    alunos_ordenados = selection_sort_string(alunos)
    print(alunos_ordenados[index - 1])


if __name__ == '__main__':
    main()
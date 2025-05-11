# Problema: [2450] Matriz Escada
# Dificuldade: AD HOC - Nível 4
# Autor: Maria Angélica Krüger Miranda

def criar_matriz(i, j):
    matriz = []
    for linha in range(i):
        matriz.append([])
        for coluna in range(j):
            matriz[linha].append(0)
    return matriz

def contar_zeros_inicio(linha):
    """Conta quantos zeros existem no começo da linha."""
    contagem = 0
    for elemento in linha:
        if elemento == 0:
            contagem += 1
        else:
            break
    return contagem

def resolver(matriz, linhas, colunas):
    ok = True
    quantidade_zeros_anterior = -1  # Começa com -1 para garantir que a primeira linha sempre passe

    for i in range(linhas):
        zeros_inicio = contar_zeros_inicio(matriz[i])

        if i == 0:
            quantidade_zeros_anterior = zeros_inicio
        else:
            if zeros_inicio > quantidade_zeros_anterior or (zeros_inicio == colunas and quantidade_zeros_anterior == colunas):
                quantidade_zeros_anterior = zeros_inicio
            else:
                ok = False
                break

    if ok:
        print("S")
    else:
        print("N")

def main():
    linhas, colunas = map(int, input().split())
    matriz = []

    # Leitura da entrada
    for i in range(linhas):
        linha = list(map(int, input().split()))
        matriz.append(linha)

    resolver(matriz, linhas, colunas)

if __name__ == "__main__":
    main()

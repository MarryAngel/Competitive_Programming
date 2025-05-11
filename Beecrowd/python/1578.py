# Problmea: [1578] Matriz de Quadrados
# Dificuldade: Iniciante - Nível 1
# Autor: Maria Angélica Krüger Miranda

def criar_matriz(i,j):
    matriz  = []
    for linha in range(i):
        matriz.append([])
        for coluna in range(j):
            matriz[linha].append(0)
    return matriz

def mostrar_matriz(matriz, ordem):
    # Passo 1: calcular a largura máxima de cada coluna
    larguras = []
    for j in range(ordem):
        maior = 0
        for i in range(ordem):
            tamanho = len(str(matriz[i][j]))
            if tamanho > maior:
                maior = tamanho
        larguras.append(maior)

    # Passo 2: imprimir a matriz com alinhamento
    for i in range(ordem):
        for j in range(ordem):
            # Se for o primeiro elemento da linha, só imprime o número alinhado
            if j == 0:
                print(f"{matriz[i][j]:>{larguras[j]}}", end="")
            else:
                # Nos próximos, imprime um espaço antes
                print(f" {matriz[i][j]:>{larguras[j]}}", end="")
        print()  

def main():
    qtd_casos = int(input())
    for caso in range(qtd_casos):
        ordem = int(input())
        matriz = []
        
        # Preencher a matriz
        for linha in range(ordem):
            linha = input().split()
            linha = [int(x) for x in linha]
            matriz.append(linha)
            
        # Calcular os quadrados
        for i in range(ordem):
            for j in range(ordem):
                matriz[i][j] = matriz[i][j] ** 2
        
        # Mostrar a matriz
        print(f"Quadrado da matriz #{4+caso}:")
        mostrar_matriz(matriz, ordem)
        if caso < qtd_casos - 1:
            print()
            
if __name__ == "__main__":
    main()
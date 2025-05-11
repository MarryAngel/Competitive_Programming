# Problmea: [1827] Matriz IV
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
    for i in range(ordem):
        linha = matriz[i]
        for j in range(ordem):
            print(f"{linha[j]:1}", end="")
        print()
    

def main():
    
    while True:
        try:
            ordem = int(input())
        except EOFError:
            return
    
        matriz = criar_matriz(ordem, ordem)
        
        for i in range(ordem):
            for j in range(ordem):
                # diagonal principal
                if i == j:
                    matriz[i][j] = 2
                # diagonal secundária
                elif i + j == ordem - 1:
                    matriz[i][j] = 3
        
        # Preencher parte interna com 1
        for i in range(ordem//3, ordem - ordem//3):
            for j in range(ordem//3, ordem - ordem//3):
                matriz[i][j] = 1

        # Ponto central com 4
        matriz[ordem//2][ordem//2] = 4
        
        mostrar_matriz(matriz, ordem)
        print()
     
if __name__ == "__main__":
    main()
# Problmea: [1478] Matriz Quadrada II
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
            if j == 0:
                print(f"{linha[j]:3}", end="")
            else:    
                print(f"{linha[j]:4}", end="")
        print()
    print()

def main():
    
    while True:
        ordem = int(input())
        if ordem == 0:
            break
        matriz = criar_matriz(ordem, ordem)
        
        for i in range(ordem):
            aux1, aux2 = 2, 2
            # diagonal principal
            matriz[i][i] = 1
            # triângulo superior              
            for j in range(i+1, ordem):
                matriz[i][j] = aux1 
                aux1 += 1
            # preencher triângulo inferior
            for j in range(i+1, ordem):
                matriz[j][i] = aux2 
                aux2 += 1
                
        mostrar_matriz(matriz, ordem)
     
if __name__ == "__main__":
    main()
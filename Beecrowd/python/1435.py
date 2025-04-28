# Problmea: [1435] Matriz Quadrada I
# Dificuldade: Iniciante - Nível 2
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
        elemento = 1
        recuo = 0
        
        # Preencher a matriz 
        while recuo != ordem//2 + 1:
            for i in range(recuo, ordem-recuo):
                for j in range(recuo, ordem-recuo):
                    matriz[i][j] = elemento 
            elemento += 1
            recuo += 1
        
        mostrar_matriz(matriz, ordem)
     

if __name__ == "__main__":
    main()
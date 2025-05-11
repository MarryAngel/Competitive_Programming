# Problmea: [1534] Matriz 123
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
        
        # Preencher matriz com 3
        for i in range(ordem):
            for j in range(ordem):
                matriz[i][j] = 3
                
        # Preencher diagonal principal com 1
        for i in range(ordem):
            matriz[i][i] = 1
        
        # Preencher diagonal secundária com 2
        for i in range(ordem):
            matriz[i][ordem-i-1] = 2
        
        mostrar_matriz(matriz, ordem)
     
if __name__ == "__main__":
    main()
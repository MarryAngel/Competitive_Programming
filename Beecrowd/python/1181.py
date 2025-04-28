# Problmea: [1181] Linha na Matriz
# Dificuldade: Iniciante - Nível 3
# Autor: Maria Angélica Krüger Miranda

def criar_matriz(i,j):
    matriz  = []
    for linha in range(i):
        matriz.append([])
        for coluna in range(j):
            matriz[linha].append(0)
    return matriz

def main():
    linha_operacao = int(input())
    operacao = input()
    
    soma = 0
    matriz = criar_matriz(12,12)
    
    for i in range(12):
        for j in range(12):
            elemento = float(input())
            matriz[i][j] = elemento
            
    for i in range(12):
        soma += matriz[linha_operacao][i]   
    
    media = soma / 12           
    
    if operacao == "S":
        print(f"{soma:.1f}")
    else:
        print(f"{media:.1f}")

if __name__ == "__main__":
    main()
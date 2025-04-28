# Problmea: [1183] Acima da Diagonal Principal
# Dificuldade: Iniciante - Nível 4
# Autor: Maria Angélica Krüger Miranda

def criar_matriz(i,j):
    matriz  = []
    for linha in range(i):
        matriz.append([])
        for coluna in range(j):
            matriz[linha].append(0)
    return matriz

def main():
    
    operacao = input()
    
    soma, qtd_elementos = 0, 0
    matriz = criar_matriz(12,12)
    
    for i in range(12):
        for j in range(12):
            elemento = float(input())
            matriz[i][j] = elemento
            
    for i in range(12):
        for j in range(i+1, 12):
            soma += matriz[i][j]  
            qtd_elementos += 1         
    
    if operacao == "S":
        print(f"{soma:.1f}")
    else:
        media = soma / qtd_elementos 
        print(f"{media:.1f}")

if __name__ == "__main__":
    main()
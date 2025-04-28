# Problmea: [1190] Área Direita
# Dificuldade: Iniciante - Nível 1
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
    
    col = 0     
    for i in range(11, 6, -1):
        for j in range(1+col, 11-col):
            soma += matriz[j][i] 
            qtd_elementos += 1         
        col += 1
    
    if operacao == "S":
        print(f"{soma:.1f}")
    else:
        media = soma / qtd_elementos 
        print(f"{media:.1f}")

if __name__ == "__main__":
    main()
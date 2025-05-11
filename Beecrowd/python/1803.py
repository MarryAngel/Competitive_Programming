# Problmea: [1803] Matring
# Dificuldade: Strings - Nível 1
# Autor: Maria Angélica Krüger Miranda

def main():
    matriz = []
    for l in range(4):
        linha = str(input())
        matriz.append(linha)
        
    chave_inicial = ""
    chave_final = ""
    
    # Pegar as chaves
    for i in range(4):
        chave_inicial += matriz[i][0]
        chave_final += matriz[i][-1]
    
    # Pegar os caracteres
    palavra = ""
    for c in range(1, len(matriz[0])-1):
        letra = matriz[0][c] + matriz[1][c] + matriz[2][c] + matriz[3][c]
        letra = int(letra)
        codigo_ascii = (letra * int(chave_inicial) + int(chave_final)) % 257
        letra = chr(codigo_ascii)
        palavra += letra

    print(palavra)

            
if __name__ == "__main__":
    main()
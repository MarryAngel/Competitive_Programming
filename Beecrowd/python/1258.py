# Problmea: [1258] Camisetas
# Dificuldade: Estrutura e Bibliotecas - Nível 4
# Autor: Maria Angélica Krüger Miranda

def main():
    primeiro = True
    while True:
        qtd_casos = int(input())
        if qtd_casos == 0:
            break
        if primeiro:
            primeiro = False
        else:
            print()
        
        camisetas = []
        for caso in range(qtd_casos):
            nome = input()
            cor, tamanho = input().split()
            camiseta = [cor, tamanho, nome]
            camisetas.append(camiseta)
            
        camisetas.sort(key=lambda x: (x[0], -ord(x[1][0]), x[2]))
        for camiseta in camisetas:
            print(camiseta[0], camiseta[1], camiseta[2])
        
        

if __name__ == "__main__":
    main()
# Problema: [1150] - Ultrapassando Z
# Dificuldade: Iniciante - Nível 1
# Autor: Maria Angélica Krüger Miranda

def resolver(soma, x, z, contagem):
    if soma > z:
        return contagem
    return resolver(soma+x, x+1, z, contagem+1)
    
def main():
    valor_x = int(input())
    valor_z = int(input())
    while valor_z <= valor_x:
        valor_z = int(input())
    contagem = 0
    contagem = resolver(0, valor_x, valor_z, contagem)
    print(contagem)

if __name__ == "__main__":
    main()
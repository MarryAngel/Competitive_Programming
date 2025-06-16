# Problema: [1113] - Crescente e Decrescente
# Dificuldade: Iniciante - Nível 1
# Autor: Maria Angélica Krüger Miranda

def main():
    a, b = map(int, input().split())
    if  a == b:
        return
    if a > b:
        print("Decrescente")
    else:
        print("Crescente")
    main()

if __name__ == "__main__":
    main()
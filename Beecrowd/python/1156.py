# Problema: [1156] - Sequência S II
# Dificuldade: Iniciante - Nível 2
# Autor: Maria Angélica Krüger Miranda

def resolver(soma, cima, baixo):
    if cima > 39:
        return soma
    ans = resolver(soma+(cima / (baixo)), cima+2, baixo*2)
    return ans
    
def main():
    soma = 0
    soma = resolver(soma, 1, 1)
    print(f"{soma:.2f}")

if __name__ == "__main__":
    main()
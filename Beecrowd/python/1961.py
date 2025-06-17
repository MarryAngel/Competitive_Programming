# Problema: [1961] - Pula Sapo
# Dificuldade: Iniciante - Nível 2
# Autor: Maria Angélica Krüger Miranda

def resolver(pulo, alturas_canos, indice):
    if indice == len(alturas_canos) - 1:
        return True
    if abs(alturas_canos[indice] - alturas_canos[indice+1]) > pulo:
        return False
    return resolver(pulo, alturas_canos, indice + 1)

def main():
    pulo, canos = map(int, input().split())
    alturas_canos = list(map(int, input().split()))
    vitoria = resolver(pulo, alturas_canos, 0)
    if vitoria == True:
        print("YOU WIN")
    else:
        print("GAME OVER")
    
if __name__ == "__main__":
    main()
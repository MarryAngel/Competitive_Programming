# Problmea: [1609] Contando Carneirinhos
# Dificuldade: AD-HOC - Nível 4
# Autor: Maria Angélica Krüger Miranda

def main():
    qtd_casos = int(input())
    for caso in range(qtd_casos):
        qtd_carneirinhos = int(input())
        carneirinhos = map(int, input().split())
        carneirinhos = set(carneirinhos)
        print(len(carneirinhos))
            
if __name__ == "__main__":
    main()
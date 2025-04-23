# Problmea: [1235] De Dentro para Fora
# Dificuldade: Strings - Nível 5
# Autor: Maria Angélica Krüger Miranda

def main():
    qtd_casos = int(input())
    for caso in range(qtd_casos):
        frase = input()
        parte1 = frase[:len(frase)//2]
        parte2 = frase[len(frase)//2:]
        
        frase_original = parte1[::-1] + parte2[::-1]
        
        print(frase_original)        

if __name__ == '__main__':
    main()
# Problmea: [1241] Encaixa ou Não II
# Dificuldade: Strings - Nível 2
# Autor: Maria Angélica Krüger Miranda

def main():
    qtd_casos = int(input())
    
    for caso in range(qtd_casos):
        palavra, sufixo = input().split()
        encaixar = True
        
        # inverter a palavra e o sufixo
        palavra_invertida = palavra[::-1]
        sufixo_invertido = sufixo[::-1]
        
        if len(sufixo_invertido) > len(palavra_invertida):
            encaixar = False
        else:
            for pos, caracter in enumerate(sufixo_invertido):
                if palavra_invertida[pos] != caracter:
                    encaixar = False
                    break
        
        print("encaixa" if encaixar else "nao encaixa")
        
if __name__ == "__main__":
    main()

# Problmea: [1234] Sentença Dançante
# Dificuldade: Strings - Nível 3
# Autor: Maria Angélica Krüger Miranda

def resolver(frase):
    frase_dancante = ""
    upper = True

    for pos, caracter in enumerate(frase):
        if caracter == " ":
            frase_dancante += " "
            continue
        elif upper == True:
            frase_dancante += caracter.upper()
            upper = False
        else:
            frase_dancante += caracter.lower()
            upper = True
    
    print(frase_dancante)

def main():
    while True:
        try:
            frase = input()
            resolver(frase)
        except EOFError:
            break

if __name__ == "__main__":
    main()
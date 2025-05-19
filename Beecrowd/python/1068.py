# Problmea: [1068] Balanço de Parênteses I
# Dificuldade: Estruturas e Bibliotecas - Nível 5
# Autor: Maria Angélica Krüger Miranda

def check_parentheses(expressao):
    pilha = []
    for char in expressao:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if not pilha:
                return False
            pilha.pop()
    return len(pilha) == 0

def main():
    while True:
        try:
            expressao = input()
        except EOFError:
            break
        if check_parentheses(expressao):
            print("correct")
        else:
            print("incorrect")

if __name__ == "__main__":
    main()
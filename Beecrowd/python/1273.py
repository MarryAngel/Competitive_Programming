# Problmea: [1273] Justificador
# Dificuldade: Strings - Nível 3
# Autor: Maria Angélica Krüger Miranda

def justificar(lista_palavras):
    maior_palavra = 0
    for palavra in lista_palavras:
        if len(palavra) > maior_palavra:
            maior_palavra = len(palavra)
    
    palavras_justificadas = []
    for palavra in lista_palavras:
        if len(palavra) < maior_palavra:
            qtd_espacos = maior_palavra - len(palavra)
            nova_palavra = " " * qtd_espacos + palavra
            palavras_justificadas.append(nova_palavra)
        else:
            palavras_justificadas.append(palavra)

    return palavras_justificadas

def main():
    n_palavras = int(input())
    while n_palavras > 0:
        
        lista_palavras = []
        for i in range(n_palavras):
            palavra = input()
            lista_palavras.append(palavra)
        
        justificadas =justificar(lista_palavras)
        print(f"\n".join(justificadas))
        
        n_palavras = int(input())
        
        if n_palavras > 0:
            print()
    
if __name__ == "__main__":
    main()
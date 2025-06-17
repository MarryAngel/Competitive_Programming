# Problema: [1251] Diga-me a Frequência
# Dificuldade: Estruturas e Bibliotecas - Nível 6
# Autor: Maria Angélica Krüger Miranda

def selection_sort(dicionario) -> list:
    lista = list(dicionario.items())
    for i in range(len(lista)):
        min_index = i
        for j in range(i+1, len(lista)):
            chave_i, valor_i = lista[min_index]
            chave_j, valor_j = lista[j]
            if valor_j < valor_i:
                min_index = j
            elif valor_j == valor_i:
                if chave_j > chave_i:
                    min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

def main():
    aux = False
    
    while True:
        try:
            texto = input()
        except EOFError:
            break
        
        frequencia = {}
        
        for caracter in texto:
            if not ord(caracter) in frequencia:
                frequencia[ord(caracter)] = 1
            else:
                frequencia[ord(caracter)] += 1
                
        frequencia_ordenada = selection_sort(frequencia)
        
        if aux:
            print()
        aux = True
        
        for elemento in frequencia_ordenada:
            print(f"{elemento[0]} {elemento[1]}")
        
        

if __name__ == '__main__':
    main()
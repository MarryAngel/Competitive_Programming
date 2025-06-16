<<<<<<< HEAD
# Problmea: [1251] Diga-me a Frequência
# Dificuldade: Estruturas e Bibliotecas - Nível 6
# Autor: Maria Angélica Krüger Miranda

def selection_sort(frequencia: dict) -> list:
    # transformar o dicionário em uma lista de pares (chave, valor)
    frequencia = list(frequencia.items())
    
    for i in range(len(frequencia)):
        min_index = i
        for j in range(i + 1, len(frequencia)):
            chave_i, valor_i = frequencia[i]
            chave_j, valor_j = frequencia[j]
            # desempate: pela frequência
            if valor_j < valor_i:
                min_index = j
            elif valor_j == valor_i:
                # desempate: pelo valor ASCII
                if chave_j > chave_i:
                    min_index = j
            frequencia[i], frequencia[min_index] = frequencia[min_index], frequencia[i]
    
    # transformar a lista de pares de volta em um dicionário
    return frequencia
    
def main():
    
=======
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
>>>>>>> 40a5e64bc5861e6eda666a650db3cd36456d6f55
    aux = False
    
    while True:
        try:
            texto = input()
        except EOFError:
            break
        
        frequencia = {}
        
<<<<<<< HEAD
        # Montar dicionário de frequências por caracter
        for caracter in texto:
            if ord(caracter) not in frequencia:
=======
        for caracter in texto:
            if not ord(caracter) in frequencia:
>>>>>>> 40a5e64bc5861e6eda666a650db3cd36456d6f55
                frequencia[ord(caracter)] = 1
            else:
                frequencia[ord(caracter)] += 1
                
<<<<<<< HEAD
        # Ordenar da menor para maior frequência -> se empate, maior valor ASCII
        frequencia_ordenada = selection_sort(frequencia)      
=======
        frequencia_ordenada = selection_sort(frequencia)
>>>>>>> 40a5e64bc5861e6eda666a650db3cd36456d6f55
        
        if aux:
            print()
        aux = True
        
        for elemento in frequencia_ordenada:
            print(f"{elemento[0]} {elemento[1]}")
<<<<<<< HEAD
        
                

if __name__ == "__main__":
=======
              
if __name__ == '__main__':
>>>>>>> 40a5e64bc5861e6eda666a650db3cd36456d6f55
    main()
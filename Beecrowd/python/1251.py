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
    
    aux = False
    
    while True:
        try:
            texto = input()
        except EOFError:
            break
        
        frequencia = {}
        
        # Montar dicionário de frequências por caracter
        for caracter in texto:
            if ord(caracter) not in frequencia:
                frequencia[ord(caracter)] = 1
            else:
                frequencia[ord(caracter)] += 1
                
        # Ordenar da menor para maior frequência -> se empate, maior valor ASCII
        frequencia_ordenada = selection_sort(frequencia)      
        
        if aux:
            print()
        aux = True
        
        for elemento in frequencia_ordenada:
            print(f"{elemento[0]} {elemento[1]}")
        
                

if __name__ == "__main__":
    main()
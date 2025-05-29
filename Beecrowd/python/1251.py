# Problema: [1251] Diga-me a Frequência
# Dificuldade: Estruturas e Bibliotecas - Nível 6
# Autor: Maria Angélica Krüger Miranda


def selection_sort(carnes, validades):
    for i in range(len(validades)-1):
        min_index = i
        for j in range(i+1, len(validades)):
            if validades[j] < validades[min_index]:
                min_index = j
        validades[i], validades[min_index] = validades[min_index], validades[i]
        carnes[i], carnes[min_index] = carnes[min_index], carnes[i]
        
    return carnes, validades

def main():
    while True:
        try:
            texto = input()
        except EOFError:
            break
        
        
       


if __name__ == '__main__':
    main()
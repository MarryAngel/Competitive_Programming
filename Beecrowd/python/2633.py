# Problema: [2633] Churras no Yuri
# Dificuldade: Estruturas e Bibliotecas - Nível 2
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
            qtd_pecas = int(input())
        except EOFError:
            break
        
        validades = []
        carnes = []
        
        for i in range(qtd_pecas):
            carne, validade = input().split()
            validades.append(int(validade))
            carnes.append(carne)
        carnes_ord, validades_ord =selection_sort(carnes, validades)
        print(*carnes_ord, sep=" ")


if __name__ == '__main__':
    main()
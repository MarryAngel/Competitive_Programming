# Problmea: [1168] LED
# Dificuldade: Strings - Nível 3
# Autor: Maria Angélica Krüger Miranda

def main():
    qtd_casos = int(input())
    
    # quantidade de leds por número: 0 a 9
    leds_por_numero = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    
    for caso in range(qtd_casos):
        valor = input()
        qtd_leds = 0
        
        for numero in valor:
            numero = int(numero)
            qtd_leds += leds_por_numero[numero]
            
        print(qtd_leds, "leds")

if __name__ == "__main__":
    main()
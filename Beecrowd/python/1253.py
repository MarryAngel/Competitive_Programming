# Problmea: [1253] Cifra de César
# Dificuldade: Strings - Nível 3
# Autor: Maria Angélica Krüger Miranda

def main():
    qtd_casos = int(input())
    
    for caso in range(qtd_casos):
        palavra_codificada = input()
        deslocamento = int(input())
        palavra_decifrada = ""
        
        for pos, caracter in enumerate(palavra_codificada):
            codigo_ascii = ord(caracter)
            codigo_decifrado = codigo_ascii - deslocamento
            
            # A = 65, Z = 90
            if codigo_decifrado < 65:
                codigo_decifrado += 26
            
            caracter_decifrado = chr(codigo_decifrado)
            palavra_decifrada += caracter_decifrado
            
        print(palavra_decifrada)

if __name__ == "__main__":
    main()
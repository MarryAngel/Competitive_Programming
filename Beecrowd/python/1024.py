# Problmea: [1024] Criptografia
# Dificuldade: Strings - Nível 5
# Autor: Maria Angélica Krüger Miranda

def camada1(frase: str) -> str:
    codigo = ""
    deslocamento = 3
    
    for  caracter in frase:
        if ord(caracter) >= 65 and ord(caracter) <= 90:
            codigo += chr(ord(caracter) + deslocamento)
        elif ord(caracter) >= 97 and ord(caracter) <= 122:
            codigo += chr(ord(caracter) + deslocamento)
        else:
            codigo += caracter
            
    return codigo
    
def camada2(frase: str) -> str:
    codigo = frase[::-1]
    return codigo

def camada3(frase: str) -> str:
    codigo = ""
    deslocamento = - 1
    # separar a frase na metade
    meio = len(frase) // 2
    parte1, parte2 = frase[:meio], frase[meio:]
    
    aux = ""
    for caracter in parte2:
        aux += chr(ord(caracter) + deslocamento)
    
    codigo = parte1 + aux
    
    return codigo

def criptografar(frase: str) -> str:
    frase_criptografada = ""
    frase_criptografada = camada1(frase)
    frase_criptografada = camada2(frase_criptografada)
    frase_criptografada = camada3(frase_criptografada)
    return frase_criptografada

def main():
    qtd_casos = int(input())

    for caso in range(qtd_casos):
        frase = input()
        print(criptografar(frase))
    
if __name__ == "__main__":
    main()
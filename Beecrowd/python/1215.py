# Problmea: [1215] Primeiro Dicionário de Andy
# Dificuldade: Estruturas e Bibliotecas - Nível 6
# Autor: Maria Angélica Krüger Miranda

def verificar_letra(caracter):
    if ('a' <= caracter <= 'z') or ('A' <= caracter <= 'Z'):
        return True
    return False

def montar_dicionario(dic_andy: set, texto: str) -> set:
    
    novo_texto = ""
    
    for pos, caracter in enumerate(texto):
        if verificar_letra(caracter):
            novo_texto += caracter.lower()
        else:
            novo_texto += " "
    
    palavras = novo_texto.split()
    
    for palavra in palavras:
        if palavra.isalpha():
            dic_andy.add(palavra)
    
    return dic_andy

def mostrar_dicionario(dic: set) -> None:
    for palavra in sorted(dic):
        print(palavra)

def main():
    dic_andy = set()
    while True:
        try:
            texto = input()
            if texto == "":
                continue
            dic_andy = montar_dicionario(dic_andy, texto)
        except EOFError:
            break
    mostrar_dicionario(dic_andy)

if __name__ == "__main__":
    main()
# Problmea: [1239] Atalho Bloggo
# Dificuldade: Strings - Nível 3
# Autor: Maria Angélica Krüger Miranda

def resolver(texto) -> str:
    texto_final = ""
    italico = 0
    negrito = 0
    for caracter in texto:
        if caracter == "_":
            if italico % 2 == 0:
                texto_final += "<i>"
            else:
                texto_final += "</i>"
            italico += 1
            
        elif caracter == "*":
            if negrito % 2 == 0:
                texto_final += "<b>"
            else:
                texto_final += "</b>"
            negrito += 1
            
        else:
            texto_final += caracter
    
    return texto_final
    

while True:
    try:
        texto = input()
        texto_final = resolver(texto)
        print(texto_final)
    except EOFError:
        break
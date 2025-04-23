# Problmea: [1120] Revisão de Contrato
# Dificuldade: Strings - Nível 5
# Autor: Maria Angélica Krüger Miranda

while True:
    digito, numero = input().split()
    
    if digito == '0' and numero == '0':
        break
    
    saida = ""
    
    for caracter in numero:
        if caracter != digito:
            saida += caracter
    
    if saida == "":
        saida = "0"
    else:
        saida = int(saida)
    print(saida)  
    
    
# Problema: [2868] Errrou!
# Dificuldade: AD-HOC - Nível 1
# Autor: Maria Angélica Krüger Miranda

testes = int(input())

for i in range(testes):
    expressao = input().split()
    operador = expressao[1]
    
    if operador == "+":
        valor_esperado = int(expressao[0]) + int(expressao[2])
    elif operador == "-":
        valor_esperado = int(expressao[0]) - int(expressao[2])
    else:
        valor_esperado = int(expressao[0]) * int(expressao[2])
    
    erro  = abs(int(expressao[4]) - valor_esperado)
    
    print(f"E{erro*'r'}ou!")
    
   
        
    
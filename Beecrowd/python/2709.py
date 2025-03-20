# # Problema: [2709] As Moedas de Robbie
# # Dificuldade: Iniciante - Nível 9
# # Autor: Maria Angélica Krüger Miranda

while True:
    try:
        qtd_moedas = int(input())
        valores = []
        for i in range(qtd_moedas):
            valor = int(input())
            valores.append(valor)
        salto = int(input())

        # inverter a lista para pilha
        aux_valores = []
        for i in range(qtd_moedas-1, -1, -1):
            aux_valores.append(valores[i])
        valores = aux_valores
        
        soma = 0
                
        for i in range(0, qtd_moedas, salto):
            soma += valores[i]

       # verificar se soma é primo com Crivo de Eratóstenes
        primo = []
        for i in range(soma + 1):
            primo.append(True)
        primo[0] = primo[1] = False

        for p in range(2, soma + 1):
            if primo[p]:
                for k in range(p*p, soma +1, p):
                    primo[k] = False
                    
        if primo[soma] == True:
            print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
        else:
            print("Bad boy! I’ll hit you.")
             
    except EOFError:
        break

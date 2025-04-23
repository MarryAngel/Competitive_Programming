# Problmea: [1332] Um-Dois-Três
# Dificuldade: Strings - Nível 2
# Autor: Maria Angélica Krüger Miranda

def resolver():
    qtd_casos = int(input())
    
    for i in range(qtd_casos):
        palavra = input()
        qtd_erros = 0
        
        if len(palavra) == 5:
            resposta = 3
            
        else:
            palavra_aux = "one"
            for pos, caractere in enumerate(palavra_aux):
                if palavra[pos] != caractere:
                    qtd_erros += 1
                if qtd_erros <= 1:
                    resposta = 1
                else:
                    resposta = 2
                    
        print(resposta)
      
        

if __name__ == "__main__":
    resolver()
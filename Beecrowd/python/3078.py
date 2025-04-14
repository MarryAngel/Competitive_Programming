# Problmea: [3078] Só o Ouro
# Dificuldade: Matemática - Nível 8
# Autor: Maria Angélica Krüger Miranda

def calcular_b(n):
    b = n % 257
    return b

def calcular_c(n):
    c = n % 193
    return c

def processar_qualidade(qtd_sementes):
    # O valor de d sempre será 4, resultando em uma equação quadrática
    # essa equação quadrática pode ser trabalhar como uma função de segundo grau
    # x^4 + bx^2 + c -> m^2 + bm + c 
    # agora basta ver o sinal do delta e o sinal das suas raízes
    
    b = calcular_b(qtd_sementes)
    c = calcular_c(qtd_sementes)
    delta = (b**2) - 4*c
    
    if delta < 0:
        return "So o ouro"
    
    # verificar o sinal de pelo menos uma raiz
    raiz = delta**0.5 - b
    if raiz > 0: 
        return "Regular"
    elif raiz == 0:
        return "Bom"
    else:
        return "So o ouro"
    
def resolver():
    while True:
        qtd_sementes= int(input())
        if qtd_sementes < 0:
            break
        qualidade = processar_qualidade(qtd_sementes)  
        print(qualidade)
        
if __name__ == "__main__":
    resolver()
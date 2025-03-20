# Problema: [2313] Qual Triângulo
# Dificuldade: Iniciante - Nível 3
# Autor: Maria Angélica Krüger Miranda

a, b, c = map(float, input().split())

validade = True

if a >= b + c:
    print("Invalido")
    validade = False
elif b >= a + c:
    print("Invalido")
    validade = False
elif c >= a + b:
    print("Invalido")
    validade = False
    
if validade:
    if (a==b) and (a==c) and (b==c):
        print("Valido-Equilatero")
    elif (a!=b) and (a!=c) and (b!=c):
        print("Valido-Escaleno")
    elif (a==b) or (a==c) or (b==c):
        print("Valido-Isoceles")
        
if validade:
    if (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == a**2 + b**2):
        print("Retangulo: S")
    else:
        print("Retangulo: N")
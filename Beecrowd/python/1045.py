# Problema: [1045] Tipos de Triângulos
# Dificuldade: Iniciante - Nível 4
# Autor: Maria Angélica Krüger Miranda

a, b, c = map(float, input().split())

if a >= b and a >= c:
    maior = a
    if b >= c:
        menor, meio = c, b
    else:
        menor, meio = b, c
elif b >= a and b >= c:
    maior = b
    if a >= c:
        menor, meio = c, a
    else:
        menor, meio = a, c
else:
    maior = c
    if a >= b:
        menor, meio = b, a
    else:
        menor, meio = a, b
        
if maior >= menor + meio:
    print("NAO FORMA TRIANGULO")
else:
    if maior**2 == menor**2 + meio**2:
        print("TRIANGULO RETANGULO")
    if maior**2 > meio**2 + menor**2:
        print("TRIANGULO OBTUSANGULO")
    if maior**2 < meio**2 + menor**2:
        print("TRIANGULO ACUTANGULO")
    if maior == meio == menor:
        print("TRIANGULO EQUILATERO")
    elif (maior == meio) or (maior == menor) or (meio == menor):
        print("TRIANGULO ISOSCELES")

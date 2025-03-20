# Problema: [1036] Fórmula de Bhaskara
# Dificuldade: Iniciante - Nível 3
# Autor: Maria Angélica Krüger Miranda

a, b, c = map(float, input().split())

delta = (b**2) - (4*a*c)

if delta > 0 and a != 0:
    r1 = (-b + delta**(1/2)) / (2*a)
    r2 = (-b - delta**(1/2)) / (2*a)
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")
else:
    print("Impossivel calcular" )
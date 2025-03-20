# Problema: [1013] O Maior

# Dificuldade: Iniciante - Nível 3
# Autor: Maria Angélica Krüger Miranda

a, b, c = map(int, input().split())
maior=(a+b+abs(a-b))/2
maior=(maior+c+abs(maior-c))/2
print(f"{int(maior)} eh o maior")
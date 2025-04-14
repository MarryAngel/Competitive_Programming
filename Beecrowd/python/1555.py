# Problema: [1555] Funções
# Dificuldade: Matemática - Nível 1
# Autor: Maria Angélica Krüger Miranda

def f_rafael(x, y):
    return (3*x)**2 + y**2

def f_beto(x, y):
    return 2*(x**2) + (5*y)**2

def f_carlos(x, y):
    return y**3 - 100*x

qtd_casos = int(input())

for i in range(qtd_casos):
    x, y = map(int, input().split())
    rafael = f_rafael(x, y)
    beto = f_beto(x, y)
    carlos = f_carlos(x, y)
    
    if rafael > beto and rafael > carlos:
        print("Rafael ganhou")
    elif beto > rafael and beto > carlos:
        print("Beto ganhou")
    else:
        print("Carlos ganhou")
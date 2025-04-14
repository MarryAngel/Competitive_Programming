# Problmea: [1176] Fibonacci em Vetor
# Dificuldade: Iniciante - Nível 3
# Autor: Maria Angélica Krüger Miranda

def calcular_fibonacci(n):
    fib = [0, 1]
    
    for i in range(2, 61):
        fib.append(fib[i-1] + fib[i-2])
        
    return fib[n]
        
    
def resolver():
    qtd_casos = int(input())
    for i in range(qtd_casos):
        n = int(input())
        fib = calcular_fibonacci(n)
        print(f"Fib({n}) = {fib}")
        
if __name__ == "__main__":
    resolver()
    
    
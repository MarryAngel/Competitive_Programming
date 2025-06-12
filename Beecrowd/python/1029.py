# Problmea: [1029] Fibonacci, Quantas Chamadas?
# Dificuldade: Paradigmas - Nível 4
# Autor: Maria Angélica Krüger Miranda

def fibonacci(dici: dict, x: int, chamadas: int):
    # Verificar se o valor já foi calculado
    if x in dici:
        return dici, dici[x][0], dici[x][1]
    
    # Como não está no dicionário, calcular o valor e adicione ao dicionário
    if x == 0:
        dici[x] = (0, 0)
        return dici, 0, 0
    elif x == 1:
        dici[x] = (1, 0)
        return dici, 1, 0
    else:
        dici, fib1, chamadas1 = fibonacci(dici, x - 1, chamadas)
        dici, fib2, chamadas2 = fibonacci(dici, x - 2, chamadas)
        dici[x] = (fib1 + fib2, chamadas1 + chamadas2 + 2)
        return dici, dici[x][0], dici[x][1]
        
def main():
    
    fib_valor = {}
    fib_valor, _, _ = fibonacci(fib_valor, 40, 0)
       
    qtd_casos = int(input())
    
    for caso in range(qtd_casos):
        valor = int(input())
        resultado = fib_valor[valor][0]
        num_chamadas = fib_valor[valor][1]
        print(f"fib({valor}) = {num_chamadas} calls = {resultado}")

if __name__ == '__main__':
    main()
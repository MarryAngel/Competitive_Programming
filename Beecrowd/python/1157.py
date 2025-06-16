# Problema: [1157] - Divisores I
# Dificuldade: Iniciante - Nível 1
# Autor: Maria Angélica Krüger Miranda

def calcular_divisores(valor, divisor, lista) -> list:
    """Calcular os divisores de forma recursiva."""
    if divisor == 0:
        return []
    if valor % divisor == 0:
        lista.append(divisor)
    calcular_divisores(valor, divisor - 1, lista) 
    return lista
    
def main():
    valor = int(input())
    divisores = []
    divisores = calcular_divisores(valor, valor, divisores)
    print(*divisores[::-1], sep='\n')

if __name__ == '__main__':
    main()
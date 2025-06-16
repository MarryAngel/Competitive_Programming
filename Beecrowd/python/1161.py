# Problema: [1161] - Soma de Fatoriais
# Dificuldade: Matemática - Nível 5
# Autor: Maria Angélica Krüger Miranda

# Calcular o fatorial e armazenar em um dicionário
def fatorial(fat, n):
    fat[0] = 1
    fat[1] = 1
    for i in range(2, n + 1):
        fat[i] = fat[i - 1] * i
    return fat

def main():
    fat = {}
    fat = fatorial(fat, 20)
    
    while True:
        try:
            m, n = map(int, input().split())
        except EOFError:
            break
        soma = fat[m] + fat[n]
        print(soma)
    
if __name__ == '__main__':
    main()
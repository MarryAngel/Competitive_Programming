# Problema: [1143] - Quadrado e ao Cubo
# Dificuldade: Iniciante - Nível 1
# Autor: Maria Angélica Krüger Miranda

def resolver(valor, contador, lista):
    if contador == 0:
        return []
    resp = (contador, contador**2, contador**3)
    lista.append(resp)
    resolver(valor, contador-1, lista)
    return lista[::-1]

def main():
    valor = int(input())
    resposta = resolver(valor, valor, [])
    for r in resposta:
        print(*r)

if __name__ == "__main__":
    main()
# Problmea: [1281] Ida à Feira
# Dificuldade: Estruturas e Bibliotecas - Nível 3
# Autor: Maria Angélica Krüger Miranda

def adicionar_produtos(qtd) -> dict:
    produtos = {}
    for n in range(qtd):
        produto, preco = input().split()
        produtos[produto] = float(preco)
    return produtos

def comprar(produtos) -> float:
    qtd_compras = int(input())
    total = 0.0
    for n in range(qtd_compras):
        produto, qtd = input().split()
        if produto in produtos:
            total += produtos[produto] * int(qtd)
    return total

def main():
    qtd_casos = int(input())
    
    for caso in range(qtd_casos):
        qtd_produtos = int(input())
        produtos = adicionar_produtos(qtd_produtos)
        total = comprar(produtos)    
        print(f"R$ {total:.2f}")    

if __name__ == "__main__":
    main()
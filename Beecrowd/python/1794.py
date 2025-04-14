# Problema: [1794] Lavanderia
# Dificuldade: Ad-Hoc - Nível 1
# Autor: Maria Angélica Krüger Miranda

def processar_lavagem(qtd: int, min_l: int, max_l: int, min_s: int, max_s:int) -> bool:
    check = True
    if (min_l <= qtd <= max_l) and (min_s <= qtd <= max_s):
        check = True
    else: 
        check = False
    return check  

qtd_pecas = int(input())
min_lavadora, max_lavadora = map(int, input().split())
min_secadora, max_secadora = map(int, input().split())

possibilidade = processar_lavagem(qtd_pecas, min_lavadora, max_lavadora, min_secadora, max_secadora)

if possibilidade:
    print("possivel")
else:
    print("impossivel")
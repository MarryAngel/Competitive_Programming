# Problema: [1038] Lanche
# Dificuldade: Iniciante - Nível 1
# Autor: Maria Angélica Krüger Miranda

codigo, qtd = input().split() 
qtd = int(qtd)
codigo = int(codigo)

if codigo == 1:
    print(f"Total: R$ {qtd*4.00:.2f}")
elif codigo == 2:
    print(f"Total: R$ {qtd*4.50:.2f}")
elif codigo == 3:
    print(f"Total: R$ {qtd*5.00:.2f}")
elif codigo == 4:
    print(f"Total: R$ {qtd*2.00:.2f}")
elif codigo == 5:
    print(f"Total: R$ {qtd*1.50:.2f}")
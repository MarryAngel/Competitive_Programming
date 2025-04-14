# Problmea: [3040] A Árvore de Natal
# Dificuldade: Iniciante - Nível 1
# Autor: Maria Angélica Krüger Miranda

def processar_arvore():
    altura, diametro, qtd_galhos = map(int, input().split())
    if (200 <= altura <= 300) and (diametro >= 50) and (qtd_galhos >= 150):
        return "Sim"
    else:
        return "Nao"

def resolver():
    qtd_casos = int(input())
    for i in range(qtd_casos):
        aceita = processar_arvore()  
        print(aceita)
    

if __name__ == "__main__":
    resolver()
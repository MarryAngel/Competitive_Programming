# Problmea: [3302] Resposta Certa
# Dificuldade: Iniciante - Nível 1
# Autor: Maria Angélica Krüger Miranda

def resolver():
    qtd_casos = int(input())
    for i in range(qtd_casos):
        resposta = input()
        print(f"resposta {i+1}: {resposta}")

if __name__ == "__main__":
    resolver()
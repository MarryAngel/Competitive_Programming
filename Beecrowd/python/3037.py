# Problmea: [3037] Jogando Dardos por Distância
# Dificuldade: Iniciante - Nível 2
# Autor: Maria Angélica Krüger Miranda

def processar_jogo():
    pontos_maria = 0
    pontos_joao = 0
    for i in range(6):
        if i < 3:
            ponto, distancia = map(int, input().split())
            pontos_joao += (ponto * distancia)
        else:
            ponto, distancia = map(int, input().split())
            pontos_maria += (ponto * distancia)
            
    if pontos_joao > pontos_maria:
        return "JOAO"
    else:
        return "MARIA"

def resolver():
    qtd_casos = int(input())
    for _ in range(qtd_casos):
        vencedor = processar_jogo()
        print(vencedor)
    
if __name__ == "__main__":
    resolver()
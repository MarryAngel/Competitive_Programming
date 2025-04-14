# Problema: [1397] Jogo do Maior
# Dificuldade: AD-HOC - Nível 1
# Autor: Maria Angélica Krüger Miranda

def processar_partidas(qtd_partidas: int) -> int:
    soma1 = 0
    soma2 = 0
    for i in range(qtd_partidas):
        ponto1, ponto2 = map(int, input().split())
        if ponto1 > ponto2:
            soma1 += 1
        elif ponto2 > ponto1:
            soma2 += 1
        else:
            soma1, soma2 = soma1, soma2
    return soma1, soma2
    

def jogo_maior():
    while True:
        qtd_partidas = int(input())
        if qtd_partidas == 0:
            break
        pontos1, pontos2 =processar_partidas(qtd_partidas)
        print(pontos1, pontos2)

if __name__ == "__main__":
    jogo_maior()

# Problmea: [1873] Pedra-papel-tesoura-lagarto-spock
# Dificuldade: Strings - Nível 2
# Autor: Maria Angélica Krüger Miranda

# A posição i ganha da posição i+1
preferencias = ["tesoura", "papel", "pedra", "lagarto", "spock", "tesoura", "lagarto", "papel", "spock", "pedra", "tesoura"]

def jogar(player1: str, player2: str) -> str:
    global preferencias
    if player1 == player2:
        return "empate"
    for i in range(len(preferencias)):
        if player1 == preferencias[i] and player2 == preferencias[i+1]:
            return "rajesh"
        elif player2 == preferencias[i] and player1 == preferencias[i+1]:
            return "sheldon"
    return "empate"

def resolver():
    qtd_casos = int(input())
  
    for i in range(qtd_casos):
        opt_rajesh, opt_sheldon = map(str, input().split())
        vencedor = jogar(opt_rajesh, opt_sheldon)
        print(vencedor)
  
if __name__ == "__main__":
    resolver()
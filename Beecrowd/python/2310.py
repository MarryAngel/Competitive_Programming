# Problmea: [2310] Voleibol
# Dificuldade: Iniciante - Nível 2
# Autor: Maria Angélica Krüger Miranda

def processar_taxa(tentativas: int, sucessos: int) -> float:
    taxa = (sucessos * 100) / tentativas
    return taxa

def resolver():
    qtd_jogadores = int(input())
    total_saques, total_bloqueios, total_ataques = 0, 0, 0
    sucessos_saques, sucessos_bloqueios, sucessos_ataques = 0, 0, 0
    for _ in range(qtd_jogadores):
        nome = input()
        tent_saque, tent_bloqueio, tent_ataque = map(int, input().split())
        sucesso_saque, sucesso_bloqueio, sucesso_ataque = map(int, input().split())
        total_saques += tent_saque
        total_bloqueios += tent_bloqueio
        total_ataques += tent_ataque
        sucessos_saques += sucesso_saque
        sucessos_bloqueios += sucesso_bloqueio
        sucessos_ataques += sucesso_ataque
    taxa_saque = processar_taxa(total_saques, sucessos_saques)
    taxa_bloqueio = processar_taxa(total_bloqueios, sucessos_bloqueios)
    taxa_ataque = processar_taxa(total_ataques, sucessos_ataques)
    print(f"Pontos de Saque: {taxa_saque:.2f} %.")
    print(f"Pontos de Bloqueio: {taxa_bloqueio:.2f} %.")
    print(f"Pontos de Ataque: {taxa_ataque:.2f} %.")

if __name__ == "__main__":
    resolver()
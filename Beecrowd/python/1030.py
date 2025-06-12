# Problema: [1030] - A Lenda de Flavious Josephus
# Dificuldade: Ad-Hoc - Nível 4
# Autor: Maria Angélica Krüger Miranda

import sys
sys.setrecursionlimit(10010)

def solver_josephus(qtd: int, salto: int) -> int:
    if qtd == 1:
        return 1
    else:
        return (solver_josephus(qtd - 1, salto) + salto - 1) % qtd + 1

def main():
    qtd_casos = int(input())
    for caso in range(qtd_casos):
        qtd_pessoas, salto = map(int, input().split())
        sobrevivente = solver_josephus(qtd_pessoas, salto)
        print(f"Case {caso + 1}: {sobrevivente}")

if __name__ == '__main__':
    main()
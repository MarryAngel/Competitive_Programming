# Problmea: [1953] Roberto e a Sala Desenfreda
# Dificuldade: AD-HOC - Nível 2
# Autor: Maria Angélica Krüger Miranda

def processar_chamada(qtd: int) -> tuple:
    epr, ehd, intrusos = 0, 0, 0
    for i in range(qtd):
        n_matricula, curso = map(str, input().split())
        if curso == "EPR":
            epr += 1
        elif curso == "EHD":
            ehd += 1
        else:
            intrusos += 1
    return epr, ehd, intrusos
    

def resolver():
    try: 
        while True:
            qtd_alunos = int(input())
            epr, ehd, intrusos = processar_chamada(qtd_alunos)  
            print(f"EPR: {epr}")
            print(f"EHD: {ehd}")
            print(f"INTRUSOS: {intrusos}")
                
    except EOFError:
        return

if __name__ == "__main__":
    resolver()
# Problmea: [2018] Olimpíadas de Natal
# Dificuldade: Estruturas e Bibliotecas - Nível 4
# Autor: Maria Angélica Krüger Miranda

def montar_placar(placar):
    
    pais_ouro = input()
    pais_prata = input()
    pais_bronze = input()
    
    # Adicionar os países caso não esteja no placar
    if not placar.get(pais_ouro):
        placar[pais_ouro] = [1, 0, 0]
    else:
        placar[pais_ouro][0] += 1
        
    if not placar.get(pais_prata):
        placar[pais_prata] = [0, 1, 0]
    else:
        placar[pais_prata][1] += 1
        
    if not placar.get(pais_bronze):
        placar[pais_bronze] = [0, 0, 1]
    else:
        placar[pais_bronze][2] += 1

    return placar
    
def ordenar(placar: dict) -> dict:
    placar_ordenado = sorted(placar.items(), key=lambda x: (-x[1][0], -x[1][1], -x[1][2], x[0]))
    return placar_ordenado

def mostrar_placar(placar):
    print("Quadro de Medalhas")
    for pais, medalhas in placar:
        ouro = medalhas[0]
        prata = medalhas[1]
        bronze = medalhas[2]
        print(f"{pais} {ouro} {prata} {bronze}")

def main():
    placar = {}
    
    while True:
        try:
            modalidade = input()
        except EOFError:
            break
        placar = montar_placar(placar)
           
    placar_ordenado = ordenar(placar)    
    mostrar_placar(placar_ordenado)

if __name__ == "__main__":
    main()
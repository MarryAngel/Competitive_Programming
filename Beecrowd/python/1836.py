# Problmea: [1836] Pokémon!
# Dificuldade: AD-HOC - Nível 3
# Autor: Maria Angélica Krüger Miranda

def calcular_hp(iv, bhp, ev, nivel):
    HP =  10 + ((50+iv+bhp+(ev**0.5)/8)*nivel)/50
    return HP
    
def calcular_atributo(iv, bs, ev, nivel):
    S = 5 + ((iv+bs+(ev**0.5)/8)*nivel)/50
    return S

def processar_atributos(nivel):
    nivel = int(nivel)
    for i in range(4):
        bs, iv, ev = map(int, input().split())
        if i == 0:
            HP = calcular_hp(iv, bs, ev, nivel)
            print(f"HP: {int(HP)}")
        elif i == 1:
            at = calcular_atributo(iv, bs, ev, nivel)
            print(f"AT: {int(at)}")
        elif i == 2:
            df = calcular_atributo(iv, bs, ev, nivel)
            print(f"DF: {int(df)}")
        else:
            sp = calcular_atributo(iv, bs, ev, nivel)
            print(f"SP: {int(sp)}")
    
def resolver():
    qtd_casos = int(input())
    for i in range(qtd_casos):
        pokemon, nivel = map(str, input().split())
        print(f"Caso #{i+1}: {pokemon} nivel {nivel}")
        processar_atributos(nivel)   
        
if __name__ == "__main__":
    resolver()
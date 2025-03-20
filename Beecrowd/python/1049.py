# Problema: [1049] Animal
# Dificuldade: Iniciante - Nível 3
# Autor: Maria Angélica Krüger Miranda

nivel1 = input()
nivel2 = input()
nivel3 = input()

if nivel1 == 'vertebrado':
    if nivel2 == 'ave':
        if nivel3 == 'carnivoro':
            print("aguia")
        else:
            print("pomba")
    else:
        if nivel3 == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if nivel2 == "inseto":
        if nivel3 == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if nivel3 == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")
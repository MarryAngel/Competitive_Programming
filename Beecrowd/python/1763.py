# Problmea: [1763] Tradutor do Papai Noel
# Dificuldade: Estruturas e Bibliotecas - Nível 3
# Autor: Maria Angélica Krüger Miranda

def tradutor() -> dict:
    dic = {
        "brasil":              "Feliz Natal!",
        "alemanha":            "Frohliche Weihnachten!",
        "austria":             "Frohe Weihnacht!",
        "coreia":              "Chuk Sung Tan!",
        "espanha":             "Feliz Navidad!",
        "grecia":              "Kala Christougena!",
        "estados-unidos":      "Merry Christmas!",
        "inglaterra":          "Merry Christmas!",
        "australia":           "Merry Christmas!",
        "portugal":            "Feliz Natal!",
        "suecia":              "God Jul!",
        "turquia":             "Mutlu Noeller",
        "argentina":           "Feliz Navidad!",
        "chile":               "Feliz Navidad!",
        "mexico":              "Feliz Navidad!",
        "antardida":           "Merry Christmas!",
        "canada":              "Merry Christmas!",
        "irlanda":             "Nollaig Shona Dhuit!",
        "belgica":             "Zalig Kerstfeest!",
        "italia":              "Buon Natale!",
        "libia":               "Buon Natale!",
        "siria":               "Milad Mubarak!",
        "marrocos":            "Milad Mubarak!",
        "japao":               "Merii Kurisumasu!"
    }
    return dic

def main():
    dados = tradutor()
    while True:
        try:
            pais = input()
            if pais in dados:
                print(dados[pais])
            else:
                print("--- NOT FOUND ---")
        except EOFError:
            break


if __name__ == "__main__":
    main()
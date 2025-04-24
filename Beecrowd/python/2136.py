# Problmea: [2136] Amigos do Habay
# Dificuldade: Estruturas e Bibliotecas - Nível 4
# Autor: Maria Angélica Krüger Miranda

def main():
    amigos_habbay = set()
    nao_amigos_habbay = set()
    escolhido = False
    nome_escolhido = ""
    
    while True:
        entrada = input()
        if entrada == "FIM":
            break
        
        nome, participacao = entrada.split()
        
        if participacao == "YES":
            amigos_habbay.add(nome)
        else:
            nao_amigos_habbay.add(nome)  
            
        if participacao == "YES" and not escolhido:
            nome_escolhido = nome
            escolhido = True
        elif participacao == "YES" and len(nome) > len(nome_escolhido):
            nome_escolhido = nome
        
    amigos_habbay = sorted(amigos_habbay)
    nao_amigos_habbay = sorted(nao_amigos_habbay)    

    for nome in amigos_habbay:
        print(nome)
    for nome in nao_amigos_habbay:
        print(nome)
    print(f"\nAmigo do Habay:\n{nome_escolhido}")    

if __name__ == "__main__":
    main()
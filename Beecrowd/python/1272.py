# Problmea: [1272] Mensagem Oculta
# Dificuldade: Strings - Nível 3
# Autor: Maria Angélica Krüger Miranda

def main():
    qtd_casos = int(input())
    
    for i in range(qtd_casos):
        mensagem = input().split()
        mensagem_oculta = []
        for palavra in mensagem:
            if palavra != "":
                mensagem_oculta.append(palavra[0])
        print("".join(mensagem_oculta))
        
if __name__ == "__main__":
    main()
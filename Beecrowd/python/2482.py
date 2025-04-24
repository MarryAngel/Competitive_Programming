# Problmea: [2482] Etiquetas de Noel
# Dificuldade: Estruturas e Bibliotecas - Nível 2
# Autor: Maria Angélica Krüger Miranda

def main():
    qtd_traducoes = int(input())
    
    traducoes = {}
    
    # adicionar as traduções no dicionário
    for n in range(qtd_traducoes):
        idioma = input()
        palavra = input()
        traducoes[idioma] = palavra
    
    qtd_criancas = int(input())
    
    # ler os nomes e idiomas das crianças
    for n in range(qtd_criancas):
        nome = input()
        idioma = input()
        print(nome)
        print(traducoes[idioma])
        print()

if __name__ == "__main__":
    main()
# Problmea: [1261] Pontos de Feno
# Dificuldade: Estruturas e Bibliotecas - Nível 2
# Autor: Maria Angélica Krüger Miranda

hay_point = {}

while True:
    try:
        n_hay_points, n_descricoes = map(int, input().split())
        
        # adicionar os pontos de feno no dicionário
        for n in range(n_hay_points):
            cargo, valor = input().split()
            hay_point[cargo] = int(valor)
            
        # ler as descrições
        for n in range(n_descricoes):
            texto = ""
            linha = input()
            
            # ler a entrada até ponto final
            while linha != ".":
                texto += linha + " "
                linha = input()
        
            texto = texto.split()
            valor = 0
            
            # calcular o valor total
            for palavra in texto:
                if palavra in hay_point:
                    valor += hay_point[palavra]
                    
            print(valor)
            
    except EOFError:
        break
# Problmea: [1424] Problema Fácil de Rujia Liu?
# Dificuldade: Estruturas e Bibliotecas - Nível 8
# Autor: Maria Angélica Krüger Miranda

def main():
    while True:
        try:
            qtd_elementos, qtd_consultas = map(int, input().split())            
        except EOFError:
            break
        
        elementos = list(map(int, input().split()))
            
        # Montar dicionário de [elemento] = posições que ele aparece
        pos_ocorrencias = {}
        for pos, elemento in enumerate(elementos):
            if elemento not in pos_ocorrencias:
                pos_ocorrencias[elemento] = []
            pos_ocorrencias[elemento].append(pos + 1)
            
        # Realizar as consultas
        for consulta in range(qtd_consultas):
            ocorrencia, valor = map(int, input().split())

            if valor in pos_ocorrencias:
                if ocorrencia <= len(pos_ocorrencias[valor]):
                    print(pos_ocorrencias[valor][ocorrencia - 1])
                else:
                    print(0)
            else:
                print(0)

if __name__ == "__main__":
    main()
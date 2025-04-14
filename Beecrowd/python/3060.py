# Problmea: [3060] Parcelamento Sem Juros
# Dificuldade: Iniciante - Nível 2
# Autor: Maria Angélica Krüger Miranda

def mostrar_parcelas(qtd_parcelas: int, parcelas: list[int]):
    for i in range(qtd_parcelas):
        print(parcelas[i])

def processar_parcelas(valor: int, qtd_parcelas: int):
    resto = valor % qtd_parcelas
    valor_min = valor // qtd_parcelas
    parcelas = []
    for i in range(qtd_parcelas):
        if i < resto:
            parcelas.append(valor_min +1)
        else:
            parcelas.append(valor_min)
    return parcelas
    

def resolver():
    valor = int(input())
    qtd_parcelas = int(input())
    parcelas = processar_parcelas(valor, qtd_parcelas)
    mostrar_parcelas(qtd_parcelas, parcelas)
    
if __name__ == "__main__":
    resolver()
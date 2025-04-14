# Problema: [1091] Divisão da Nlogônia
# Dificuldade: Ad-Hoc - Nível 1
# Autor: Maria Angélica Krüger Miranda

def processar_local(x_divisor: int, y_divisor: int, x_residencia: int, y_residencia: int) -> str:
    if x_residencia == x_divisor or y_residencia == y_divisor:
        return "divisa"
    elif x_residencia < x_divisor and y_residencia < y_divisor:
        return "SO"
    elif x_residencia < x_divisor and y_residencia > y_divisor:
        return "NO"
    elif x_residencia > x_divisor and y_residencia < y_divisor:
        return "SE"
    elif x_residencia > x_divisor and y_residencia > y_divisor:
        return "NE"
    elif x_residencia < x_divisor and y_residencia == y_divisor:
        return "N"
    elif x_residencia > x_divisor and y_residencia == y_divisor:
        return "S"
    elif x_residencia == x_divisor and y_residencia < y_divisor:
        return "O"
    elif x_residencia == x_divisor and y_residencia > y_divisor:
        return "L"


while True:
    qtd_consultas = int(input())
    if qtd_consultas == 0:
        break
    x_divisor, y_divisor = map(int, input().split())
    for i in range(qtd_consultas):
        x_residencia, y_residencia = map(int, input().split())
        local = processar_local(x_divisor, y_divisor, x_residencia, y_residencia)
        print(local)

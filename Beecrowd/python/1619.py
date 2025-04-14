# Problema: [1619] Diferença entre Datas
# Dificuldade: AD-HOC - Nível 4
# Autor: Maria Angélica Krüger Miranda

dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def ordenar_data(data1, data2):
    inicio, fim = data1, data2
    
    # separar as informações
    ano_i, mes_i, dia_i = map(int, inicio.split('-'))
    ano_f, mes_f, dia_f = map(int, fim.split('-'))
    
    if ano_f < ano_i:
        inicio, fim = fim, inicio
    elif ano_f == ano_i:
        if mes_f < mes_i:
            inicio, fim = fim, inicio
        elif mes_f == mes_i:
            if dia_f < dia_i:
                inicio, fim = fim, inicio
    
    return inicio, fim

def verificar_bissexto(ano):
    bissexto = False
    if (ano % 400 == 0) or (ano % 4 == 0 and ano%100 != 0):
        bissexto = True
    return bissexto

def transcorrer_dias(dia, mes, ano):
    dias = 0
    for i in range(1970, ano):
        dias += 365 if not verificar_bissexto(i) else 366
    for i in range(1, mes):
        if i == 2 and verificar_bissexto(ano):
            dias += dias_por_mes[i] + 1
        else: 
            dias += dias_por_mes[i]

    dias += dia
    return dias

def calcular_diferenca(inicio, fim):
    dif = 0
    
    # separar as informações
    ano_i, mes_i, dia_i = map(int, inicio.split('-'))
    ano_f, mes_f, dia_f = map(int, fim.split('-'))

    dias_inicio = transcorrer_dias(dia_i, mes_i, ano_i)
    dias_fim = transcorrer_dias(dia_f, mes_f, ano_f)
    
    dif = dias_fim - dias_inicio
    
    return dif

def resolver():
    qtd_casos = int(input())
    for i in range(qtd_casos):
        # entrada dos dados
        data1, data2 = map(str, input().split())

        # definir inicio e fim
        inicio, fim = ordenar_data(data1, data2)
            
        # calcular a diferença entre as datas
        diferenca = calcular_diferenca(inicio, fim)
        
        # imprimir o resultado
        print(diferenca)

if __name__ == "__main__":
    resolver()
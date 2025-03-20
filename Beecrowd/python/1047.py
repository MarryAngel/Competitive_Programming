# Problema: [1047] Tempo de Jogo com Minutos
# Dificuldade: Iniciante - Nível 9
# Autor: Maria Angélica Krüger Miranda

hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

if hora_final > hora_inicial:
    if minuto_final >= minuto_inicial:
        print(f"O JOGO DUROU {hora_final - hora_inicial} HORA(S) E {minuto_final - minuto_inicial} MINUTO(S)")
    else:
        print(f"O JOGO DUROU {hora_final - hora_inicial - 1} HORA(S) E {minuto_final - minuto_inicial + 60} MINUTO(S)")
elif hora_final < hora_inicial:
    if minuto_final >= minuto_inicial:
        print(f"O JOGO DUROU {hora_final - hora_inicial + 24} HORA(S) E {minuto_final - minuto_inicial} MINUTO(S)")
    else:
        print(f"O JOGO DUROU {hora_final - hora_inicial + 24 - 1} HORA(S) E {minuto_final - minuto_inicial + 60} MINUTO(S)")  
else:
    if minuto_final > minuto_inicial:
        print(f"O JOGO DUROU 0 HORA(S) E {minuto_final - minuto_inicial} MINUTO(S)")
    elif minuto_final < minuto_inicial:
        print(f"O JOGO DUROU {hora_final - hora_inicial + 24 - 1} HORA(S) E {minuto_final - minuto_inicial + 60} MINUTO(S)")
    else:
        print(f"O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
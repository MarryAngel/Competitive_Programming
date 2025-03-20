# Problema: [1019] Conversão de Tempo
# Dificuldade: Iniciante - Nível 1
# Autor: Maria Angélica Krüger Miranda

tempo_total_segundo = int(input())

horas= tempo_total_segundo//3600
minutos = (tempo_total_segundo % 3600) // 60
segundos = (tempo_total_segundo % 3600) % 60

print(f"{horas}:{minutos}:{segundos}")

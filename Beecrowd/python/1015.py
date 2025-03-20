# Problema: [1015] Distância Entre Dois Pontos
# Dificuldade: Iniciante - Nível 1
# Autor: Maria Angélica Krüger Miranda

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
distancia = ((x2-x1)**2+(y2-y1)**2)**0.5
print(f"{distancia:.4f}")
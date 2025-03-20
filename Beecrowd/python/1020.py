# Problema: [1020] Idade em Dias
# Dificuldade: Iniciante - Nível 2
# Autor: Maria Angélica Krüger Miranda

dias = int(input())

print(f"{dias//365} ano(s)")
print(f"{(dias%365)//30} mes(es)")
print(f"{(dias%365)%30} dia(s)")
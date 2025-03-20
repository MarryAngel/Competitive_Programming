# Problema: [1038] Média 3
# Dificuldade: Iniciante - Nível 5
# Autor: Maria Angélica Krüger Miranda

n1, n2, n3, n4 = map(float, input().split())

media = (n1*2 + n2*3 + n3*4 + n4)/10

print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
elif media >= 5.0 and media < 7.0:
    print("Aluno em exame.")
    nota_exame = float(input())
    media_final = (media + nota_exame)/2
    print(f"Nota do exame: {nota_exame:.1f}")
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media_final:.1f}")
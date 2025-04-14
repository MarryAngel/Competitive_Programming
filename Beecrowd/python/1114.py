# Problema: [1114] Senha Fixa
# Dificuldade: Iniciante - Nível 1
# Autor: Maria Angélica Krüger Miranda

while True:
    try:
        senha = int(input())
        senha_correta = 2002
        if senha == senha_correta:
            print("Acesso Permitido")
            break
        else:
            print("Senha Invalida")
    except EOFError:
        break
        
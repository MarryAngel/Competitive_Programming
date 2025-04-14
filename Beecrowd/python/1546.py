# Problema: [1546] Feedback
# Dificuldade: Ad-Hoc - Nível 1
# Autor: Maria Angélica Krüger Miranda

def processar_responsavel(categoria: int) -> str:
    if categoria == 1:
        return "Rolien"
    elif categoria == 2:
        return "Naej"
    elif categoria == 3:
        return "Elehcim"
    elif categoria == 4:
        return "Odranoel"

qtd_casos = int(input())

for i in range(qtd_casos):
    qtd_feedbacks = int(input())
    for j in range(qtd_feedbacks):
        categoria = int(input())
        responsavel = processar_responsavel(categoria)
        print(responsavel)
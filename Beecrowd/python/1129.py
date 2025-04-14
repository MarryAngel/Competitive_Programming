# Problema: [1129] Leitura Ótica
# Dificuldade: Ad-Hoc - Nível 1
# Autor: Maria Angélica Krüger Miranda

def corrigir(correcao: list[str]) -> str:
    alternativas = ["A", "B", "C", "D", "E"]
    resposta = []
    for i in range(5):
        if correcao[i] == "preto":
            resposta.append(alternativas[i])
            
    if len(resposta) != 1:
        return "*"
    else:
        return resposta[0]  

def processar_alternativa(gabarito: list[str]) -> str:
    alternativa = ""
    correcao = []
    
    for i in range(5):
        if int(gabarito[i]) <= 127:
            correcao.append("preto")
        else:
            correcao.append("branco")
    alternativa = corrigir(correcao)
    return alternativa

while True:
    qtd_questoes = int(input())
    
    if qtd_questoes == 0:
        break
    
    for i in range(qtd_questoes):
        gabarito = input().split()
        resposta = processar_alternativa(gabarito)
        print(resposta)
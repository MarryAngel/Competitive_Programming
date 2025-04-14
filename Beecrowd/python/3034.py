# Problmea: [3034] O Caso Douglas
# Dificuldade: AD-HOC - Nível 2
# Autor: Maria Angélica Krüger Miranda

def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def processar_ataques(qtd_consultas):
    ataques = []
    for i in range(qtd_consultas):
      caso = int(input())+1
      if (caso%7 == 0) and (caso%2!=0) and primo(caso+2):
          ataques.append("Yes")
      else:
          ataques.append("No")   
    return ataques
    

def resolver():
    qtd_consultas = int(input())
    ataque = processar_ataques(qtd_consultas)
    for i in range(qtd_consultas):
        print(ataque[i])
    
if __name__ == "__main__":
    resolver()
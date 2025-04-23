# Problmea: [1238] Combinador
# Dificuldade: Strings - Nível 3
# Autor: Maria Angélica Krüger Miranda

def main():
    qtd_casos = int(input())
    
    for caso in range(qtd_casos):
        palavra1, palavra2 = input().split()
        palavra_final = ""
        pos = 0
        
        while pos < len(palavra1) and pos < len(palavra2):
            palavra_final += palavra1[pos] + palavra2[pos]
            pos += 1
        
        if pos < len(palavra1):
            palavra_final += palavra1[pos:]
        elif pos < len(palavra2):
            palavra_final += palavra2[pos:]
        
        print(palavra_final)    

if __name__ == "__main__":
    main()
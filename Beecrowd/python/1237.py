# Problmea: [1237] Comparação de Substring
# Dificuldade: Strings - Nível 6
# Autor: Maria Angélica Krüger Miranda

def maior_substring(palavra1, palavra2):
    maior_substring = ""
    
    # palavra2 será sempre a menor palavra
    if len(palavra2) > len(palavra1):
        palavra1, palavra2 = palavra2, palavra1
    
    # encontrar a maior substring comum
    for i in range(len(palavra2)):
        for j in range(i + 1, len(palavra2) + 1):
            sub = palavra2[i:j]
            if sub in palavra1 and len(sub) > len(maior_substring):
                maior_substring = sub
                
    return len(maior_substring)

if __name__ == "__main__":
    try:
        while True:
            palavra1 = input()
            palavra2 = input()
            print(maior_substring(palavra1, palavra2))
    except EOFError:
        pass
# Problmea: [2460] Fila
# Dificuldade: AD-HOC - Nível 5
# Autor: Maria Angélica Krüger Miranda

def main():
    qtd_pessoas = int(input())
    ids_fila = input().split()
    qtd_removidos = int(input())
    id_removido = input().split()
    
    for id in id_removido:
        if id in ids_fila:
            ids_fila.remove(id)
            
    fila = " ".join(map(str, ids_fila))
    print(fila)
    
if __name__ == "__main__":
    main()
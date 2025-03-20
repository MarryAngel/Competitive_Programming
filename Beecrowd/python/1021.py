# Problema: [1021] Notas e Moedas
# Dificuldade: Iniciante - Nível 6
# Autor: Maria Angélica Krüger Miranda

valor = float(input())
nota = int(valor)
moeda = int((valor - nota)*100)
dif = round((valor - nota)*100) - (valor - nota)*100
if abs(dif) < 1e-7:
    moeda = round((valor - nota)*100)


print('NOTAS:')
print(f"{int(nota//100)} nota(s) de R$ 100.00")
print(f"{int(nota%100//50)} nota(s) de R$ 50.00")
print(f"{int(nota%100%50//20)} nota(s) de R$ 20.00")
print(f"{int(nota%100%50%20//10)} nota(s) de R$ 10.00")
print(f"{int(nota%100%50%20%10//5)} nota(s) de R$ 5.00")
print(f"{int(nota%100%50%20%10%5//2)} nota(s) de R$ 2.00")
print('MOEDAS:')
print(f"{int(nota%100%50%20%10%5%2)} moeda(s) de R$ 1.00")
print(f"{int(moeda//50)} moeda(s) de R$ 0.50")
print(f"{int(moeda%50//25)} moeda(s) de R$ 0.25")
print(f"{int(moeda%50%25//10)} moeda(s) de R$ 0.10")
print(f"{int(moeda%50%25%10//5)} moeda(s) de R$ 0.05")
print(f"{int(moeda%50%25%10%5)} moeda(s) de R$ 0.01")
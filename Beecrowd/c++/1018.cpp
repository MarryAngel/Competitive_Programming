// Problema: [1018] Cédulas
// Dificuldade: Iniciante - Nível 4
// Autor: Maria Angélica Krüger Miranda

#include<bits/stdc++.h>

using namespace std;

void fastIO(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
}

using namespace std;

int main(){
    fastIO();
    int notas100, notas50, notas20, notas10, notas5, notas2, notas1, valor;
    cin >> valor;
    notas100 = valor/100;
    notas50 = (valor%100)/50;
    notas20 = ((valor%100)%50)/20;
    notas10 = (((valor%100)%50)%20)/10;
    notas5 = ((((valor%100)%50)%20)%10)/5;
    notas2 = (((((valor%100)%50)%20)%10)%5)/2;
    notas1 = ((((((valor%100)%50)%20)%10)%5)%2);
    printf("%d\n",valor);
    printf("%d nota(s) de R$ 100,00\n", notas100); 
    printf("%d nota(s) de R$ 50,00\n", notas50);
    printf("%d nota(s) de R$ 20,00\n", notas20);
    printf("%d nota(s) de R$ 10,00\n", notas10);
    printf("%d nota(s) de R$ 5,00\n", notas5);
    printf("%d nota(s) de R$ 2,00\n", notas2);
    printf("%d nota(s) de R$ 1,00\n", notas1);
    return 0;
}
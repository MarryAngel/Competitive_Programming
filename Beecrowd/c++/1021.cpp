// Problema: [1021] Notas e Moedas
// Dificuldade: Iniciante - Nível 6
// Autor: Maria Angélica Krüger Miranda

#include<bits/stdc++.h>

using namespace std;

void fastIO(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
}

using namespace std;

int main (){
    double valor;
    cin >> valor;
    int aux, notas100, notas50, notas20, notas10, notas5, notas2, notas1;
    int moedas50, moedas25, moedas10, moedas5, moedas1;
    double moedas;
    aux = valor/1;
    notas100 = aux/100;
    notas50 = aux%100/50;
    notas20 = aux%100%50/20;
    notas10 = aux%100%50%20/10;
    notas5 = aux%100%50%20%10/5;
    notas2 = aux%100%50%20%10%5/2;
    notas1 = aux%100%50%20%10%5%2/1;
    aux = notas100*100 + notas50*50 + notas20*20 + notas10*10 + notas5*5 + notas2*2 + notas1*1;
    moedas = (valor - aux)*100;
    aux = moedas/1;
    moedas50 = aux/50;
    moedas25 = aux%50/25;
    moedas10 = aux%50%25/10;
    moedas5 = aux%50%25%10/5;
    moedas1 = aux%50%25%10%5/1;
    cout << "NOTAS:\n";
    cout << notas100 << " nota(s) de R$ 100.00\n";
    cout << notas50 << " nota(s) de R$ 50.00\n";
    cout << notas20 << " nota(s) de R$ 20.00\n";
    cout << notas10 << " nota(s) de R$ 10.00\n";
    cout << notas5 << " nota(s) de R$ 5.00\n";
    cout << notas2 << " nota(s) de R$ 2.00\n";
    cout << "MOEDAS:\n";
    cout << notas1 << " moeda(s) de R$ 1.00\n";
    cout << moedas50 << " moeda(s) de R$ 0.50\n";
    cout << moedas25 << " moeda(s) de R$ 0.25\n";
    cout << moedas10 << " moeda(s) de R$ 0.10\n";
    cout << moedas5 << " moeda(s) de R$ 0.05\n";
    cout << moedas1 << " moeda(s) de R$ 0.01\n";
    return 0;
}
//Problema: [1010] Cálculo Simples
//Dificuldade: Iniciante - Nível 3
//Autor: Maria Angélica Krüger Miranda

#include<bits/stdc++.h>

using namespace std;

void fastIO(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
}

int main(){
    fastIO();
    int cod1, cod2, qtd1, qtd2;
    double valor1, valor2, total;
    cin >> cod1 >> qtd1 >> valor1;
    cin >> cod2 >> qtd2 >> valor2;
    total = (qtd1*valor1)+(qtd2*valor2);
    printf("VALOR A PAGAR: R$ %.2lf\n", total);
    return 0;
}
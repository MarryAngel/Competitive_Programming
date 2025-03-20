//Problema: [1009] Salário com Bônus
//Dificuldade: Iniciante - Nível 2
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
    string nome;
    double salario, vendas, total;
    cin >> nome >> salario >> vendas;
    total = (vendas*0.15)+salario;
    printf("TOTAL = R$ %.2lf\n", total);
    return 0;
}
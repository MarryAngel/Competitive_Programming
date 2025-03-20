// Problema: [1014] Consumo
// Dificuldade: Iniciante - Nível 1
// Autor: Maria Angélica Krüger Miranda

#include<bits/stdc++.h>

using namespace std;

void fastIO(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
}

int main(){
    fastIO();
    int distancia;
    double combustivel_gasto;
    cin >> distancia >> combustivel_gasto;
    printf("%.3lf km/l\n", distancia/combustivel_gasto);
    return 0;
}
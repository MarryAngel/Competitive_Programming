// Problema: [1017] Gasto de Combustível
// Dificuldade: Iniciante - Nível 1
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
    int tempo_viagem, velocidade;
    double distancia, litros;
    cin >> tempo_viagem >> velocidade;
    distancia = tempo_viagem * velocidade;
    litros = distancia/12;
    printf("%.3lf\n", litros);
    return 0;
}
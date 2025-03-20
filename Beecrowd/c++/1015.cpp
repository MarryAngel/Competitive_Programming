// Problema: [1015] Distância Entre Dois Pontos
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
    double x1, y1, x2, y2, distancia;
    cin >> x1 >> y1 >> x2 >> y2;
    distancia = sqrt(pow((x2-x1),2)+pow((y2-y1),2));
    printf("%.4lf\n", distancia);
    return 0;
}
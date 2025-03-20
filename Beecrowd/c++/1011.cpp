//Problema: [1011] Esfera
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
    double raio, PI, volume;
    PI = 3.14159;
    cin >> raio;
    volume = (4.0/3.0)*PI*pow(raio,3);
    printf("VOLUME = %.3lf\n", volume);
    return 0;
}
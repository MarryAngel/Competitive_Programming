//Problema: [1002] Área do Círculo
//Dificuldade: Iniciante - Nível 4
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

    double raio, area;
    double pi = 3.14159;

    cin >> raio;
    area=pi*raio*raio;
    printf("A=%.4f\n",area );

    return 0;
}
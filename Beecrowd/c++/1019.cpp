// Problema: [1019] Conversão de Tempo
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

int main (){
    int segundos;
    cin >> segundos;
    int horas, minutos;
    minutos = segundos/60;
    horas = minutos/60;
    cout << horas << ":" << minutos%60 << ":" << segundos%60 << endl;
    return 0;
}
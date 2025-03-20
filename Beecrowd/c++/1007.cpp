//Problema: [1007] Diferença
//Dificuldade: Iniciante - Nível 1
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
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    printf("DIFERENCA = %d\n", (a*b-c*d));
    return 0;
}
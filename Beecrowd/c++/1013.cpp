//Problema: [1013] O Maior
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
    int a, b, c, maior;
    cin >> a >> b >> c;
    maior = (a+b+abs(a-b))/2;
    maior = (maior+c+abs(maior-c))/2;
    printf("%d eh o maior\n", maior);
    return 0;
}
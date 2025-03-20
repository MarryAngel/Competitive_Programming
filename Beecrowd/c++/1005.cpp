//Problema: [1005] Média 1
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
    double a, b, media;
    cin >> a >> b;
    media = (a * 3.5 + b*7.5) / 11;
    printf("MEDIA = %.5f\n", media);
    return 0;
}
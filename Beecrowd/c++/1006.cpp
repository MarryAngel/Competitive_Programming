//Problema: [1006] Média 2
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
    double a, b, c, media;
    cin >> a >> b >> c;
    media = (a*2 + b*3 + c*5) / 10;
    printf("MEDIA = %.1f\n", media);
    return 0;
}
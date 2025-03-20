//Problema: [1012] Área
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
    double a, b, c, PI;
    PI = 3.14159;
    cin >> a >> b >> c;
    printf("TRIANGULO: %.3lf\n", a*c/2.0);
    printf("CIRCULO: %.3lf\n", PI*pow(c,2));
    printf("TRAPEZIO: %.3lf\n", (a+b)*c/2.0);
    printf("QUADRADO: %.3lf\n", pow(b,2));
    printf("RETANGULO: %.3lf\n", a*b);
    return 0;
}
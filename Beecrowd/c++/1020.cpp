// Problema: [1020] Idade em Dias
// Dificuldade: Iniciante - Nível 2
// Autor: Maria Angélica Krüger Miranda

#include<bits/stdc++.h>

using namespace std;

void fastIO(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    // cout.tie(0);
}

using namespace std;

int main (){
    int idade_dias;
    cin >> idade_dias;
    int ano, mes;
    ano = idade_dias/365;
    mes = (idade_dias-ano*365)/30;
    idade_dias = idade_dias - ano*365 - mes*30;
    printf("%d ano(s)\n%d mes(es)\n%d dia(s)\n", ano, mes, idade_dias);
    return 0;
}
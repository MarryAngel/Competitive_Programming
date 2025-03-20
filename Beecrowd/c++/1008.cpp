//Problema: [1008] Salário
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
    int id, qtd_horas;
    double valor_hora, salario;
    cin >> id >> qtd_horas >> valor_hora;
    salario = qtd_horas * valor_hora;
    printf("NUMBER = %d\nSALARY = U$ %.2lf\n", id, salario);
    return 0;
}
// Problema: 1016] Distância
// Dificuldade: Iniciante - Nível 1
// Autor: Maria Angélica Krüger Miranda

// Lógica: O próprio exercício comenta que a distância entre os carros X e Y é de 1km a cada 2 minutos.
// Para que o carro X alcance Y, ele precisa percorrer a diferença entre eles, que é a relação mencionada acima.

#include<bits/stdc++.h>

using namespace std;

void fastIO(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
}

using namespace std;

int main(){
    fastIO();
    int distancia;
    cin >> distancia;
    cout << distancia*2 << " minutos" << endl;
    return 0;
}
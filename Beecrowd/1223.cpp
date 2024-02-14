#include<bits/stdc++.h>

using namespace std;

int a=0, b=0, c=0;

void eq_reta(int x1, int y1, int x2, int y2)
{
    a = y1 - y2;
    b = x2 - x1;
    c = x1*y2 - y1*x2;
}

double dist_ponto_reta(int x, int y){
    return abs(a*x + b*y + c) / (sqrt(a*a + b*b));
}

int main(){

    int n, l, h, yi, xf, yf, xa, ya;
    double dist, dist_parede, dist_min;

    while(cin>>n){
        cin>>l>>h;
        for(int i=0; i<n; i++){
            cin>>yi>>xf>>yf;

            if( i == 0){
                dist_min = l - xf;
                xa = xf;
                ya = yf;
                continue;
            }    
            
            if(i % 2 == 0){
                eq_reta(0, yi, xf, yf);
                dist_parede = l - xf;
            }else{
                eq_reta(l, yi, xf, yf);
                dist_parede = xf;
            }

            dist = dist_ponto_reta(xa, ya);

            cout << "Dist_min antigo: " << dist_min << endl;
            cout << "Dist: " << dist << endl;
            cout << "Dist_parede: " << dist_parede << endl;

            if(dist < dist_min)
                dist_min = dist;
            if(dist_parede < dist_min)
                dist_min = dist_parede;

            xa = xf;
            ya = yf;

             cout << "Dist_min atual: " << dist_min << endl;

        }

        cout << fixed << setprecision(2);
        cout << dist_min << endl;
    }

    return 0;
}
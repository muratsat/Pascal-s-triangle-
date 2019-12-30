#include <iostream>
using namespace std;
int f(int n){
    if(n <= 1) return 1;
    else return n * f(n-1);
}
int C(int n, int k){ 
    return f(n) / f(k) / f(n-k);
}
int g(int n){
    int s = 0;
    while(n > 0) {
        n /= 10; 
        s++;
    }
    return s;
}
int h(int n){
    int s = 0;
    for(int k = 0; k <= n; k++){
        s += 1 + g(C(n,k));
        if(k == n) s--;
    }
    return s;
}
int main(){
    int N;
    cin>>N;
    for(int n = 0; n <= N; n++){
        int m = (h(N) - h(n));
        for(int i = 0; i < m/2; i++) cout<<' ';
        for(int k = 0; k <= n; k++){
            cout<<C(n, k)<<' ';
        }
        cout<<endl;
    } 
}

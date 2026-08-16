#include <iostream>
using namespace std;

int GCM(int n, int m){
    int temp = 0;
    int result = 1;
    if(n > m){
        temp = n;
        n = m;
        m = temp;
    }
    for(int i = 1; i <= m; i++){
        if(n % i == 0 && m % i == 0){
            result = i;
            result = result * (n / i) * (m / i);
        }
    }
    return result;
}

int main() {
    int n = 0, m = 0;
    
    cin >> n >> m;

    cout << GCM(n, m);
    return 0;
}
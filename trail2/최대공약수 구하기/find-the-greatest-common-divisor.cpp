#include <iostream>
using namespace std;

int gcd(int n, int m){
    int result = 1;
    for(int i = 1; i <= m; i++){
        if(n % i == 0 && m % i == 0){
            result = i;
        }
    }
    return result;
}
int main() {
    int n = 0, m = 0;

    cin >> n >> m;
    cout << gcd(n, m);
    return 0;
}
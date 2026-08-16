#include <iostream>
using namespace std;

int gcd(int n, int m){
    int array[m];
    int result = 1;
    if(n > m){
        int temp = 0;
        temp = n;
        n = m;
        m = temp;
    }
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
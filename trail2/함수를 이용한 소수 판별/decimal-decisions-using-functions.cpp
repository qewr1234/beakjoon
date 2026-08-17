#include <iostream>
using namespace std;

bool find_prime(int n){
    if(n == 1){
        return false;
    }
    for(int i = 2; i < n; i++){
        if(n % i == 0){
            return false;
        }
    }
    return true;
}

int main() {
    int a = 0, b = 0, count = 0;

    cin >> a >> b;

    for(int i = a; i <= b; i++){
        if(find_prime(i)){
            count += i;
        }
    }
    cout << count;

    return 0;
}
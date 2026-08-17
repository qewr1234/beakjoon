#include <iostream>
using namespace std;

int print_power(int a, int b){
    int result = 1;
    for(int i = 1; i <= b; i++){
        result *= a;
    }
    return result;
}

int main() {
    int a = 0, b = 0;

    cin >> a >> b;

    cout << print_power(a, b);
    return 0;
}
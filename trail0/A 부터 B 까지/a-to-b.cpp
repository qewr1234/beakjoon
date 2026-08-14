#include <iostream>
using namespace std;

int main() {
    int a, b = 0;
    cin >> a >> b;

    while(a <= b){
        if(a % 2 == 0){
            cout << a << " ";
            a = a+3;
        }
        else{
            cout << a << " ";
            a = a*2;
        }
    }
    return 0;
}
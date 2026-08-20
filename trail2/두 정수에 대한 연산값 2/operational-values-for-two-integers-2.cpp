#include <iostream>
using namespace std;

void Swap(int &a, int &b){
    if(a > b){
        a *= 2;
        b += 10;
    }
    else if(a < b){
        a += 10;
        b *= 2;
    }
}

int main() {
    int a = 0, b = 0;

    cin >> a >> b;

    Swap(a, b);

    cout << a << " " << b << endl;
    return 0;
}
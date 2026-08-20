#include <iostream>
using namespace std;

void cal(int &a, int &b){
    if(a > b){
        a += 25;
        b *= 2;
    }
    else if(a < b){
        b += 25;
        a *= 2;
    }
}

int main() {
    int a = 0, b = 0;

    cin >> a >> b;

    cal(a, b);

    cout << a << " " << b << endl;
    return 0;
}
#include <iostream>
using namespace std;

int main() {
    int a = 5, b = 6, c = 7;
    int temp = 0;

    temp = a;
    a = c;
    c = temp;

    temp = b;
    b = c;
    c = temp;

    cout << a << "\n" << b << "\n" << c;
    return 0;
}
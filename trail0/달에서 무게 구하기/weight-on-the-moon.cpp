#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    double weight = 13, gravity = 0.165;
    cout << weight << " * ";
    cout.setf(ios::fixed);
    cout.precision(6);
    cout << gravity << " = " << weight * gravity << endl;

    return 0;
}




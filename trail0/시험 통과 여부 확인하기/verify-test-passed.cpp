#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a = 0;

    cin >> a;

    if(a >= 80){
        cout << "pass" << endl;
    }
    else{
        cout << 80-a << " more score" << endl;
    }
    return 0;
}
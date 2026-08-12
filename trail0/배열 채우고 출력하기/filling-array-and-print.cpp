#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    char Array[10];

    for(int i = 0; i < 10; i++){
        cin >> Array[i];
    }
    for(int i = 9; i >= 0; i--){
        cout << Array[i];
    }
    return 0;
}
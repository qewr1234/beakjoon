#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int Num = 0;

    cin >> Num;
    int Array[Num] = {};
    for(int i = 0; i < Num; i++){
        cin >> Array[i];
    }
    
    for(int i = 0; i < Num; i++){
        cout << Array[i] * Array[i] << " ";
    }
    return 0;
}
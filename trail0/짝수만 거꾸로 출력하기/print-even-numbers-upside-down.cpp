#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int Num = 0;

    cin >> Num;
    int array[Num] = {};

    for(int i = 0; i < Num; i++){
        cin >> array[i];
    }
    for(int j = Num-1; j >= 0; j--){
        if(array[j] % 2 == 0){
            cout << array[j] << " ";
        }
    }
    return 0;
}
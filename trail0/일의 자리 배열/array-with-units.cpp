#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b, x;
    int array[20];

    cin >> a >> b;
    array[0] = a;
    array[1] = b;

    for(int i = 0; i < 10; i++){
        array[i+2] = array[i + 1] + array[i];
        if(array[i+2] >= 10){
            array[i+2] = array[i+2] - 10;
        }
        cout << array[i] << " ";
    }
    return 0;
}
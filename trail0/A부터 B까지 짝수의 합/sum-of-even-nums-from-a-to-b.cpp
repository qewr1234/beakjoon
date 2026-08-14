#include <iostream>
using namespace std;

int main() {
    int a, b = 0;

    cin >> a >> b;
    int array[b];
    int total = 0;

    for(int i = a; i <= b; i++){
        array[i] = i;
    }
    for(int i = a; i <= b; i++){
        if(array[i] % 2 == 0){
            total += i;
        }
    }
    cout << total;
    return 0;
}
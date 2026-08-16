#include <iostream>
using namespace std;

int main() {
    int array[4][4] = {};

    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            cin >> array[i][j];
        }
    }
    for(int i = 0; i < 4; i++){
        int total = 0;
        for(int j = 0; j < 4; j++){
            total += array[i][j];
        }
        cout << total << endl;
    }
    return 0;
}
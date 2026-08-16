#include <iostream>
using namespace std;

int main() {
    int array_1[3][3];
    int array_2[3][3];
    int array_3[3][3];

    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            cin >> array_1[i][j];
        }
    }
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            cin >> array_2[i][j];
        }
    }

    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            array_3[i][j] = array_1[i][j] * array_2[i][j];
            cout << array_3[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
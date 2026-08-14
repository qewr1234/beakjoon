#include <iostream>
using namespace std;

int main() {
    int num_1 = 0;
    int num_2 = 0;
    int array[10];

    for(int i = 0; i < 10; i++){
        cin >> array[i];
    }
    for(int i = 0; i < 10; i++){
        if(array[i] % 3 == 0){
            num_1 += 1;
        }
        if(array[i] % 5 == 0){
            num_2 += 1;
        }
    }    
    cout << num_1 << " " << num_2 << endl;
    return 0;
}
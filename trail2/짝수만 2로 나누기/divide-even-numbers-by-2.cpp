#include <iostream>
using namespace std;

void DivEvenNum(int n, int x[]){
    for(int i = 0; i < n; i++){
        if(x[i] % 2 == 0){
            x[i] = x[i] / 2;
        }
    }

}

int main() {
    int n = 0;

    cin >> n;

    int array[n];
    
    for(int i = 0; i < n; i++){
        cin >> array[i];
    }
    DivEvenNum(n, array);

    for(int i = 0; i < n; i++){
        cout << array[i] << " ";
    } 

    return 0;
}
#include <iostream>
using namespace std;

int main() {
    int N = 0;

    cin >> N;

    for(int i = N; i >= 1; i--){
        for(int j = 0; j < i; j++){
            cout << "*" << " ";
        }
        cout << endl;
    }
    return 0;
}
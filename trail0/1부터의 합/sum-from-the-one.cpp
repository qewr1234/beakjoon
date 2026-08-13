#include <iostream>
using namespace std;

int main() {
    int N = 0;
    int total = 0;

    cin >> N;

    for(int i = 0; i <= 100; i++){
        total += i;
        if(total >= N){
            cout << i;
            break;
        }
    }
    return 0;
}
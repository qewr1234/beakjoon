#include <iostream>
using namespace std;

int main() {
    int N = 0;

    cin >> N;
    
    for(int j = 0; j < N; j++){
        int a = 0, b = 0;
        cin >> a >> b;
        int total = 0;

        for(int i = a; i <= b; i++){
            if(i % 2 == 0){
                total += i;
            }
        }
        cout << total << endl;
    }
    return 0;
}
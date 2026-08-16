#include <iostream>
using namespace std;

int main() {
    int N = 0;
    int cnt = 0;

    cin >> N;

    for(int i = 1; i <= N; i++){
        for(int j = 1; j <= i; j++){
            cnt += 1;
            cout << cnt << " ";
        }
        cout << endl;
    }
    return 0;
}
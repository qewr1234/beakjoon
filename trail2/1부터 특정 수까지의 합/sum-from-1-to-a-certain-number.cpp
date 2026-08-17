#include <iostream>
using namespace std;


int sum(int N){
    int result = 0;
    for(int i = 1; i <= N; i++){
        result += i;
    }
    return result / 10;
}
int main() {

    int N = 0;

    cin >> N;

    cout << sum(N);
    
    return 0;
}
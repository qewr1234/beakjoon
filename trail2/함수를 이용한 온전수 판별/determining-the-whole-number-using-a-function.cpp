#include <iostream>
using namespace std;

bool isPerfectNumber(int n){
    if(n % 2 == 0 || n % 10 == 5 || (n % 3 == 0 && n % 9 != 0) ){
        return false;
    }
    else{
        return true;
    }
}

int main() {
    int a = 0, b = 0;
    int count = 0;

    cin >> a >> b;

    for(int i = a; i <= b; i++){
        if(isPerfectNumber(i) == true){
            count++;
        }
    }
    cout << count;
    return 0;
}
#include <iostream>
using namespace std;

bool CheckPrimeNum(int n){
    for(int i = 2; i < n; i++){
        if(n % i == 0){
            return false;
        }
    }
    return true;
}

bool CheckEvenNum(int n){
    int result = 0;
    while(n > 0){
        result += n % 10;
        n /= 10;
    }
    if(result % 2 == 0){
        return true;
    }
    else{
        return false;
    }
}

int main() {
    int a = 0, b = 0;
    int count = 0;

    cin >> a >> b;

    for(int i = a; i <= b; i++){
        if(CheckPrimeNum(i)){
            if(CheckEvenNum(i)){
                count++;
            }
        }
    }
    cout << count;
    return 0;
}
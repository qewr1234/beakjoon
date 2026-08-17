#include <iostream>
using namespace std;

bool check_num(int num){
    while(num > 0){
        if(num % 10 == 3 || num % 10 == 6 || num % 10 == 9){
            return true;
        }
        num /= 10;
    }
    return false;
}

int find_num(int a, int b){
    int count = 0;

    for(int i = a; i <= b; i++){
        if(i % 3 == 0 || check_num(i)){
            count += 1;
        }
    }
    return count;
}

int main(){
    int a = 0, b = 0;

    cin >> a >> b;

    cout << find_num(a, b);

    return 0;
}
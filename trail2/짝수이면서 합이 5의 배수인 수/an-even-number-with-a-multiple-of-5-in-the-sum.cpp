#include <iostream>
using namespace std;

string find_num(int n){
    int a = 0, b = 0;
    a = n/10;
    b = n%10;
    if(n % 2 == 0 && (a+b) % 5 == 0){
        return "Yes";
    }
    else{
        return "No";
    }
}
int main() {
    int n = 0;

    cin >> n;

    cout << find_num(n);
    return 0;
}
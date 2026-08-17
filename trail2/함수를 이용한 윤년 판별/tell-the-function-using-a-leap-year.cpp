#include <iostream>
using namespace std;


bool leaf_year(int n){
    if(n % 100 == 0 && n % 400 != 0){
        return false;
    }
    if(n % 4 == 0){
        return true;
    }
    else{
        return false;
    }
}

int main() {
    int year = 0;

    cin >> year;

    if(leaf_year(year) == 1){
        cout << "true";
    }
    else{
        cout << "false";
    }
    return 0;
}
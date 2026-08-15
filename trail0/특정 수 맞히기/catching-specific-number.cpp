#include <iostream>
using namespace std;

int main() {
    int number = 0;

    while(true){
        cin >> number;
        if(number < 25){
            cout << "Higher" << endl;
        }
        else if(number > 25){
            cout << "Lower" << endl;
        }
        else{
            cout << "Good" << endl;
            break;
        }
    }
    return 0;
}
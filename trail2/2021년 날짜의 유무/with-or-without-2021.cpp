#include <iostream>
using namespace std;

bool CheckMonthDay(int month, int day){
    if(month == 2){
        if(day <= 28){
            return true;
        }
    }
    if(month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12){
        if(day <= 31){
            return true;
        }
    }
    if(month == 4 || month == 6 || month == 9 || month == 11){
        if(day <= 30){
            return true;
        }
    }
    return false;
}

int main() {
    int month = 0, day = 0;

    cin >> month >> day;

    if(CheckMonthDay(month, day)){
        cout << "Yes";
    }
    else{
        cout << "No";
    }

    return 0;
}
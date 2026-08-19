#include <iostream>
using namespace std;

bool CheckLeafYear(int y){
    if(y % 4 == 0){
        if(y % 400 == 0){
            return true;
        }
        if(y % 100 != 0){
            return true;
        }
    }
    return false;
}

bool CheckDay(int year, int month, int day){
    if(CheckLeafYear(year)){
        if(month == 2 && day <= 29){
            return true;
        }
    }
    else{
        if(month == 2 && day <= 28){
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

string CheckSeason(int month){
    if(month == 3 || month == 4 || month == 5){
        return "Spring";
    }
    if(month == 6 || month == 7 || month == 8){
        return "Summer";
    }
    if(month == 9 || month == 10 || month == 11){
        return "Fall";
    }
    if(month == 12 || month == 1 || month == 2){
        return "Winter";
    }
    else{
        return "-1";
    }
}

int main() {
    int year = 0, month = 0, day = 0;

    cin >> year >> month >> day;

    if(CheckDay(year, month, day)){
        cout << CheckSeason(month);
    }
    else{
        cout << "-1";
    }
    return 0;
}
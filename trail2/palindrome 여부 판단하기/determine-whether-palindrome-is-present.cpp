#include <iostream>
#include <string>
using namespace std;

bool CheckString(string &str){
    int length = str.length();
    
    for(int i = 0; i < length / 2; i++){
        if(str[i] != str[length - 1 - i]){
            return false;
        }
    }
    return true;
}

int main() {
    string str = "";

    cin >> str;

    if(CheckString(str)){
        cout << "Yes";
    }
    else{
        cout << "No";
    }
    return 0;
}
#include <iostream>
#include <string>
using namespace std;

bool CheckStr(string str){
    int length = str.length();
    
    for(int i = 0; i < length; i++){
        if(str[0] != str[i]){
            return true;
        }
    }
    return false;

}

int main() {
    string str;

    cin >> str;

    if(CheckStr(str)){
        cout << "Yes";
    }
    else{
        cout << "No";
    }

    return 0;
}
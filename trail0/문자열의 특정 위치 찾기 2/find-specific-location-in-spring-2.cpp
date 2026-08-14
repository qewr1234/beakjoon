#include <iostream>
using namespace std;

int main() {
    string array[5] = {"apple", "banana", "grape", "blueberry", "orange"};
    int total = 0;
    char input = 0;

    cin >> input;

    for(int i = 0; i < 5; i++){
        if(array[i][2] == input || array[i][3] == input){
            cout << array[i] << endl;
            total += 1;
        }
    }
    cout << total;
    return 0;
}
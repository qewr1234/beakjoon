#include <iostream>
#include <string>
#include <algorithm>
#include <functional>

using namespace std;

int main() {
    int n = 0;

    cin >> n;

    string str[n] = {};

    for(int i = 0; i < n; i++){
        cin >> str[i];
    }

    sort(str, str + n);

    for(int i = 0; i < n; i++){
        cout << str[i] << endl;
    }

    return 0;
}
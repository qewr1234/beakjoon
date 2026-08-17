#include <iostream>
using namespace std;

int find_min(int a, int b, int c){
    int min = 0;
    if(a <= b && a <= c){
        min = a;
    }
    else if(b <= a && b <= c){
        min = b;
    }
    else if(c <= a && c <= b){
        min = c;
    }
    return min;
}
int main() {
    int a = 0, b = 0, c = 0;

    cin >> a >> b >> c;

    cout << find_min(a, b, c);
    return 0;
}
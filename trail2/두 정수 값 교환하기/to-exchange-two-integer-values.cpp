#include <iostream>
using namespace std;

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
    cout << *a << " " << *b << endl;

}

int main() {
    int a = 0, b = 0;

    cin >> a >> b;

    swap(&a, &b);
    
    return 0;
}
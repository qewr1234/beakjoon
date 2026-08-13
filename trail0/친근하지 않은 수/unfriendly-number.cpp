#include <iostream>
using namespace std;

int main() {
    
    int num = 0;
    int count = 0;
    cin >> num;

    int array[num];
    for(int i = 0; i <= num; i++){
        if(i % 2 == 0|| i % 3 == 0 || i % 5 == 0){
            continue;
        }
        else{
            count += 1;
        }
    }
    cout << count;
    return 0;
}
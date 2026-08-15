#include <iostream>
using namespace std;

int main() {
    int start, end = 0;
    int total = 0;

    cin >> start >> end;

    for(int i = start; i <= end; i++){
        int count = 0;
       for(int j = 1; j <= end; j++){
            if(i % j == 0){
                count += 1;
            }
       }
       if(count == 3){
            total += 1;
       }
    }
    cout << total;
    return 0;
}
#include <iostream>
#include <algorithm>
using namespace std;

void Swap(int n, int arr[]){
    sort(arr, arr + n);
}

int main() {
    int n = 0;

    cin >> n;

    int arr[n];

    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }

    Swap(n, arr);

    for(int i = 0; i < n; i++){
        cout << arr[i] << " ";
    }

    cout << endl;

    for(int i = n - 1; i >= 0; i--){
        cout << arr[i] << " ";
    }

    return 0;
}
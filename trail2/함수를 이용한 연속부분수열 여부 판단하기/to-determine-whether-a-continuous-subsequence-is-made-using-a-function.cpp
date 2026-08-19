#include <iostream>
using namespace std;

bool CheckNum(int a[], int b[], int n1, int n2) {
    if (n2 > n1) {
        return false;
    }

    for (int i = 0; i <= n1 - n2; i++) {
        bool check = true;

        for (int j = 0; j < n2; j++) {
            if (a[i + j] != b[j]) {
                check = false;
                break;
            }
        }

        if (check) {
            return true;
        }
    }

    return false;
}

int main() {
    int n1 = 0, n2 = 0;

    cin >> n1 >> n2;

    int a[100];
    int b[100];

    for (int i = 0; i < n1; i++) {
        cin >> a[i];
    }

    for (int i = 0; i < n2; i++) {
        cin >> b[i];
    }

    if (CheckNum(a, b, n1, n2)) {
        cout << "Yes";
    }
    else {
        cout << "No";
    }

    return 0;
}
#include <iostream>
using namespace std;

int function_add(int a, int b){
    return a + b;
}
int function_sub(int a, int b){
    return a - b;
}
int function_mul(int a, int b){
    return a * b;
}
int function_div(int a, int b){
    return a / b;
}

int main() {
    int a = 0, b = 0;
    char o = 0;

    cin >> a >> o >> b;

    if(o == '+'){
        cout << a << " " << o << " " << b << " = " << function_add(a, b);
    }
    else if(o == '-'){
        cout << a << " " << o << " " << b << " = " << function_sub(a, b);
    }
    else if(o == '*'){
        cout << a << " " << o << " " << b << " = " << function_mul(a, b);
    }
    else if(o == '/'){
        cout << a << " " << o << " " << b << " = " << function_div(a, b);
    }
    else{
        cout << "False";
    }
    return 0;
}
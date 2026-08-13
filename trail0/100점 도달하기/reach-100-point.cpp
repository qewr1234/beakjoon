#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int score = 0;
    cin >> score;

    for(int i = score; i <= 100; i++){
        if(score >= 90){
            cout << "A" << " ";
            score += 1;
        }
        else if(score >= 80){
            cout << "B" << " ";
            score += 1;
        }
        else if(score >= 70){
            cout << "C" << " ";
            score += 1;
        }
        else if(score >= 60){
            cout << "D" << " ";
            score += 1;
        }
        else if(score < 60){
            cout << "F" << " ";
            score += 1;
        }
    }
    return 0;
}
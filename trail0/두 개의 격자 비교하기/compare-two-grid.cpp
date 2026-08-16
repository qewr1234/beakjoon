#include <iostream>
using namespace std;

int main() {
    int N = 0, M = 0;

    cin >> N >> M;
    int array[2][N][M];

    for(int i = 0; i < 2; i++){
        for(int j = 0; j < N; j++){
            for(int k = 0; k < M; k++){
                cin >> array[i][j][k];
            }
        }
    }
    for(int j = 0; j < N; j++){
        for(int k = 0; k < M; k++){
            if(array[0][j][k] == array[1][j][k]){
                cout << "0" << " ";
            }
            else{
                cout << "1" << " ";
            }
        }
        cout << endl;
    }
    return 0;
}
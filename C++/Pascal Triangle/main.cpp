#include <iostream>

using namespace std;

int main(){
    int row;
    cout << "Enter a row number :";
    cin >> row;
    cout << "\n";
    for (int i = 1 ; i <= row ; i++){
        for (int l = row - i ; l >= 0 ; l--){
            cout << "  ";
        }
        int value = 1;
        for (int j = 1 ; j <= i ; j++){
            cout << value << "   ";
            value = (value * (i - j) / j);
            
        }
        cout << "\n";
    }
    return 0;
}
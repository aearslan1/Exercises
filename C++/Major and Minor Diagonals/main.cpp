#include <iostream>

using namespace std;

int main(){
    //preparing matrix
    const int const_row = 9;
    const int const_col = 9;
    int matrix[const_row][const_col] = {0};

    //minor
    for (int row = 0; row < const_row; row++){
        for (int col = 0; col < const_col; col++){
            if (row == col){
                matrix[row][col] = 1;
            }
        }
    }
    
    //major
    for (int row = 0; row < const_row; row++){
        for (int col = 0; col < const_col; col++){
            if (row + col == const_col - 1){
                matrix[row][col] = 1;
            }
        }
    }
    //print matrix
    for (int row = 0; row < const_row; row++){
        for (int col = 0; col < const_col; col++){
            cout << matrix[row][col] << "  ";
        }
        cout << "\n";
    }

    return 0;
}
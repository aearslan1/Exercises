#include <iostream>

using namespace std;

int main(){
    //example 1
    cout << "EXAMPLE 1" << endl;
    const int const_row = 5;
    const int const_col = 5;
    int matrix[const_row][const_col];

    for (int row = 0; row < const_row; row++){
        for (int col = 0; col < const_col; col++){
            matrix[row][col] = row + col;
        }
    }

    for (int row = 0; row < const_row; row++){
        for (int col = 0; col < const_col; col++){
            cout << matrix[row][col] << " ";
        }
        cout << endl;
    }

    //example 2
    cout << "\nEXAMPLE 2" << endl;
    int matrix_2[4][4] = {
        {1,2,3,4},
        {4,3,2,1},
        {5,4,3,6},
        {1,2,3,5}};

    int row_sum = 0;
    int col_sum = 0;
    
    for (int row = 0; row < 4; row++){
        for (int col = 0; col < 4; col++){
            cout << matrix_2[row][col] << " ";
        }
        cout << endl;
    }
    cout << "\n";
    for (int row = 0; row < 4; row++){
        for (int col = 0; col < 4; col++){
            row_sum += matrix_2[row][col];
            col_sum += matrix_2[col][row];
        }
        cout << "The sum of the "<< row << "th row = " << row_sum << endl;
        cout << "The sum of the "<< row << "th col = " << col_sum << endl;
        cout << "\n";
        col_sum = 0;
        row_sum = 0;

    }
    return 0;
}
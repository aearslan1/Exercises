#include <iostream>
#include <time.h>
#include <cstdlib>

using namespace std;



class Game{
    char arr[3][3] = {{' ', ' ', ' '}, {' ', ' ', ' '}, {' ', ' ', ' '}};
    char player_char;
    char other_char;
    public:

        Game(char player_char, char other_char){
            this->player_char = player_char;
            this->other_char = other_char;

        }

        void play(int row, int col, char character){
            if ((row < 3 && row >= 0) && (col < 3 && col >= 0)){
                arr[row][col] = character;
            }


        }

        void show(){
            for (int row = 0; row < 3; row++){
                for (int col = 0; col < 3; col++){
                    cout << "[" << arr[row][col] << "] ";
                }
                cout << "\n\n";
            }
        }

        bool is_victory(char& charachter){
            int row_count, col_count;
            int cross_count_1 = 0, cross_count_2 = 0;

            //kazanma kontrolü

            for (int row = 0; row < 3; row++){

                row_count = col_count = 0;

                for (int col = 0; col < 3; col++){
                    if (arr[row][col] == charachter)
                        row_count++;

                    if (arr[col][row] == charachter)
                        col_count++;

                    if (row == col && arr[row][col] == charachter)
                        cross_count_1++;

                    if (row + col == 2 && arr[row][col] == charachter)
                        cross_count_2++;
                }

                if (row_count >= 3 || col_count >= 3 || cross_count_1 >= 3 || cross_count_2 >= 3)
                    return true;

                row_count = col_count = 0;
            }
            return false;
        }

        static void menu(){
            cout << "[XOX GAME]\n\n1.Start game\n2.Menu\n3.Quit\n\n";
        }

        void gameLoop(){
            int row, col;

            while(true){

                show();

                while(true){
                    cout << "\nEnter a row and column(row col): ";
                    cin >> row >> col;
                    if ((row < 0 || row > 2 || col < 0 || col > 2) || arr[row][col] != ' '){
                        cout << "\n\nunvalid option, enter a numbers between 0 and 2\n\n";
                        continue;
                    }
                    break;
                }

                int c_row = -1;
                int c_col = -1;


                play(row, col, player_char);

                while (true){
                    c_row = rand() % 3;
                    c_col = rand() % 3;
                    if ((c_row < 0 || c_row > 2 || c_col < 0 || c_col > 2) || arr[c_row][c_col] != ' '){
                        continue;

                    }
                    else{
                        break;
                    }
                }

                play(c_row, c_col, other_char);

                if (is_victory(player_char)){
                    show();
                    cout << "Player wins!" << endl;
                    break;

                }
                else if (is_victory(other_char)){
                    show();
                    cout << "Computer wins!" << endl;
                }
            }
        }

};
int main(){
    srand(time(0));
    char choice;
    Game::menu();
    while(true){
        cout << ">>> ";
        cin >> choice;

        switch(choice){
            case '1':{
                Game game('X', 'O');
                game.gameLoop();
                continue;
            }

            case '2':{
                cout << "\n";
                Game::menu();
                continue;
            }

            case '3':
                break;

            default:
                cout << "\n\nunvalid option, try again\n\n";
                continue;
        }
        break;
    }
}


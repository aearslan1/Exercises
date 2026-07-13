#include <iostream>

using namespace std;

int main(){
    int n,fibN = 0,prevVal = 1;
    cout << "n :";
    cin >> n;

    for (int i = 1 ; i <= n ; i++){
        fibN += prevVal;
        prevVal = fibN - prevVal;
        printf("The %dth number of the fibonnaci sequence : %d\n",i,fibN);
    } 
    return 0;
}
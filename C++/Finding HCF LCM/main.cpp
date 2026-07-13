#include <iostream>
#include <climits>

using namespace std;

int main(){
    int a,b,gcd = 1,lcm;
    cout << "Enter a number :";
    cin >> a;
    cout << "Enter another number :";
    cin >> b;

    int minNumber = min(a,b);
    for (int i = 1; i <= minNumber ; i++){
        if (a % i == 0 && b % i == 0){
            if (i > gcd){
                gcd = i;
            }
        }
    }
    //a * b = gcd * lcm

    lcm = a * b / gcd;
    printf("\ngcd(%d,%d) = %d\n",a,b,gcd);
    printf("lcm(%d,%d) = %d\n",a,b,lcm);
    return 0;
}
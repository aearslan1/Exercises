#include <iostream>

using namespace std;

int main(){
	float numberA,numberB;
	char op;
	
	cout << "Enter a number :";
	cin >> numberA;
	cout << "Enter a another number :";
	cin >> numberB;         
	cout << "Enter a operator (+ - * /) :";
	cin >> op;

	switch(op){
		case '+':
			cout << numberA << " + " << numberB << " = " << numberA + numberB << endl;
			break;
		case '-':
			cout << numberA << " - " << numberB << " = " << numberA - numberB << endl;
			break;
		case '*':
			cout << numberA << " * " << numberB << " = " << numberA * numberB << endl;
			break;
		case '/':
			if (numberB == 0){
				cout << "Can't divide by zero." << endl;
				break;
			}
			cout << numberA << " / " << numberB << " = " << numberA / numberB << endl;
			break;
		default:
			cout << "Invalid operator,please enter a valid operator." << endl;
			break;
	}

	return 0;

}

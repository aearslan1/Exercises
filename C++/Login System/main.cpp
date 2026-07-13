#include <iostream>

using namespace std;
void appLauncher(){ //buraya giriş doğruysa başlatmak istediğiniz uygulamayı yazmanız gerek.
	int x;
	while(true){
		cout << ">>";
		cin >> x;
		if (x == 0){
			break;
		}
	}
	
}
int main(){
	const string staticUsername = "admin";
	const string staticPassword = "123456a";
	
	string loginUsername,loginPassword;
	bool loginStatus = false;
	int attemptCount = 5;

	while(attemptCount > 0){
		cout << "Enter username :";
		getline(cin,loginUsername);
		
		cout << "Enter password :";
		getline(cin,loginPassword);

		if (loginUsername == staticUsername && loginPassword == staticPassword){
			cout << "Login succsesful , welcome " << loginUsername << "!" << endl;
			loginStatus = true;
			break;
		}else{
			attemptCount--;
			cout << "Login failed,please try again(you have " << attemptCount << " attempt left)"<< endl;
		}
		
	}

	if (loginStatus){
		appLauncher();
	}else{
		cout << "Unfortunately, you have no attempts left; please try again later." << endl;
	}
	return 0;
}

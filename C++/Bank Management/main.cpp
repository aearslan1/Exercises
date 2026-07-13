#include <iostream>

using namespace std;

int main() {
    float moneyAmount = 5000;
    cout << "BANKA YONETIM UYGULAMASI\n\n<menu>\n1-Bakiye Sorgulama\n2-Para Cekme\n3-Para Yukleme\n4-Menu\n5-Cikis\n\n";
    
    while (true)
    {
        char option;
        cout << ">> ";
        cin >> option;

        switch (option)
        {
            case '1':{
                cout << "(Hesabinizida '" << moneyAmount << "' TL para var)"<< endl;
                continue;
            }

            case '2':{
                float amountReceived;
                cout << "<para cekme>\n(Cekmek istediginiz miktari yaziniz) >> ";
                cin >> amountReceived;
                if (amountReceived <= 0){
                    cout << "(Para cekme islemi iptal edildi)" << endl;
                }
                else if (amountReceived <= moneyAmount){
                    moneyAmount -= amountReceived;
                    cout << "('" << amountReceived << "' TL basariyla cekildi,hesabinizda '" << moneyAmount << "' TL para kaldi)" << endl;
                }
                else{
                    cout << "(Hesabinizda '" << amountReceived << "' TL para yok,lütfen '" << moneyAmount << "' TL'den daha az bir para girin)" << endl;
                }

                continue;
            }

            case '3':{
                float amountGiven;
                cout << "<para yukleme>\n(Yuklemek istediginiz miktari yaziniz) >> ";
                cin >> amountGiven;
                if (amountGiven <= 0){
                    cout << "(Para yukleme islemi iptal edildi)" << endl;
                }
                else{
                    moneyAmount += amountGiven;
                    cout << "(Hesabiniza '" << amountGiven << "' TL basariyla eklendi,hesabinizda '" << moneyAmount << "' TL paraniz var)" << endl;
                }
                
                continue;
            }

            case '4':{
                cout << "\n<menu>\n1-Bakiye Sorgulama\n2-Para Cekme\n3-Para Yukleme\n4-Menu\n5-Cikis\n\n";
                continue;
            }

            case '5':{
                break;
            }

        }
        cout << "..." << endl;
        break; 
    }

}

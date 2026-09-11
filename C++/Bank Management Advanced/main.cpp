#include "libs/functions.h"
#include <vector>
/*
    Çerçeveler:
        ║ ═ ╔ ╗ ╚ ╝
*/ 
using namespace std;

class Account{
    protected:
        string name;
        string country;
        string birth;
        string ID;
        
        float balance;
        bool is_current = false;


    public:
        Account(string name, string country, string birth_day, string birth_month, string birth_year, float balance){
            this->name = name;
            this->country = country;
            this->birth = birth_day + birth_month + birth_year;
            this->ID = this->country + "-" + this->name + this->birth;
            this->balance = balance;
        }

        virtual ~Account() = default;

        void get_info(){
            
            string id_info = " ID : " + this->ID + " ";
            string name_info = " name : " + this->name;
            string country_info = " country : " + this->country;
            string balance_info = " balance : " + flt::low_float(to_string(this->balance));
            string is_current_info = " current : " + boolean::turn_string(this->is_current);

            int top_corner_lenght = id_info.length();

            name_info += str::n_string(top_corner_lenght - name_info.length(), " ");
            country_info += str::n_string(top_corner_lenght - country_info.length(), " ");
            balance_info += str::n_string(top_corner_lenght - balance_info.length(), " ");
            is_current_info += str::n_string(top_corner_lenght - is_current_info.length(), " ");
            
            cout << "╔";
            write::n_write(top_corner_lenght, "═"); cout << "╗" << "\n"; 
            cout << "║" << id_info << "║" << "\n";
            cout << "║" << name_info << "║" << "\n";
            cout << "║" << country_info << "║" << "\n";
            cout << "║" << balance_info << "║" << "\n";
            cout << "║" << is_current_info << "║" << "\n";
            cout << "╚";
            write::n_write(top_corner_lenght, "═"); cout << "╝" << "\n";
        }
        string get_id(){
            return this->ID;
        }
        virtual void pull_money(float amount) = 0;
        virtual void send_money(Account* account, float amount) = 0;
        friend class CurrentAccount;
        friend class SavingsAccount;
        friend class AccountList;
};

class CurrentAccount : public Account{
    private:
        float limit = 2000.0;
    public:    
        CurrentAccount(string name, string country, string birth_day, string birth_month, string birth_year, float balance) : Account(name, country, birth_day, birth_month, birth_year, balance){
            this->is_current = true;
        }

        void pull_money(float amount){
            if (amount <= balance + this->limit){
                write::one_panel_string(flt::low_float(to_string(amount)) + "TL successfully withdrawn");
                balance -= amount;
            }
            else
                write::one_panel_string("Failed to withdraw money, no " + flt::low_float(to_string(amount)) + "TL in your account");
        }
        
        void send_money(Account* account, float amount){
            if (amount <= balance + this->limit){
                write::one_panel_string(flt::low_float(to_string(amount)) + "TL successfully sent");
                this->balance -= amount;
                account->balance += amount;
            }
            else
                write::one_panel_string("Failed to sent money, no " + flt::low_float(to_string(amount)) + "TL in your account");
        }
                  
};

class SavingsAccount : public Account{
    public:
        SavingsAccount(string name, string country, string birth_day, string birth_month, string birth_year, float balance) : Account(name, country, birth_day, birth_month, birth_year, balance) {
            this->is_current = false;
        }
        
        void pull_money(float amount){
            if (amount <= this->balance){
                write::one_panel_string(flt::low_float(to_string(amount)) + "TL successfully withdrawn");
                balance -= amount;
            }
            else
                write::one_panel_string("Failed to withdraw money, no " + flt::low_float(to_string(amount)) + "TL in your account");
        }
        void send_money(Account* account, float amount){
            if (amount <= balance){
                write::one_panel_string(flt::low_float(to_string(amount)) + "TL successfully sent");
                this->balance -= amount;
                account->balance += amount;
            }
            else
                write::one_panel_string("Failed to sent money, no " + flt::low_float(to_string(amount)) + "TL in your account");
        }
};

class AccountList{
    protected:
        vector<Account*> account_list;
    public:
        ~AccountList(){
            for (Account* acc : account_list){
                delete acc;
        }
}
        void append(Account* account){
            account_list.push_back(account);
        }

        void del(string ID){
            Account* account = this->get_user(ID);
            
            for (int i = 0; i < account_list.size(); i++){
                if(account == account_list[i]){
                    delete account_list[i];
                    account_list.erase(account_list.begin() + i);
                    break;
                }
            }
        }
        int size(){
            return account_list.size();
        }

        vector<Account*> get(){
            return account_list;
        }

        Account* get_user(string ID){
            for (int i = 0; i < account_list.size(); i++){
                if(ID == account_list[i]->get_id()){
                    return account_list[i];
                }
            }
            return nullptr;

        }
        
    
};

namespace cli{
    void create_account(AccountList& account_list){
        string name = write::input("NAME");
        string country = write::input("COUNTRY");
        string birth_day = write::input("BIRTH DAY");
        string birth_month = write::input("BIRTH MONTH");
        string birth_year = write::input("BIRTH YEAR");
        string balance = write::input("BALANCE"); 
        string is_current = write::input("IS CURRENT(N, default current)");

        Account* account;
        
        if(is_current == "N"){
            write::one_panel_string("Creating Saving Account");
            account = new SavingsAccount(name ,country, birth_day, birth_month, birth_year, stof(balance));
        }

        else{
            write::one_panel_string("Creating Current Account");
            account = new CurrentAccount(name, country, birth_day, birth_month, birth_year, stof(balance));
        }

        
        account_list.append(account);
        
        
    }
    void delete_account(AccountList& account_list){
        vector<Account*> accounts = account_list.get();
        string ID = write::input("ACCOUNT ID");
        Account* account = account_list.get_user(ID);

        if (account != nullptr){
            account_list.del(ID);
        }
        else
            write::one_panel_string("'" + ID + "'" + " does not match any user");
    }
    void show_account(AccountList& account_list){
        vector<Account*> accounts = account_list.get();

        for (int i = 0; i < account_list.size(); i++){
            if (accounts[i] != nullptr){
                accounts[i]->get_info();
            }
        }
    }
    void send_money(AccountList& account_list){
        vector<Account*> accounts = account_list.get();
        string sender_ID = write::input("SENDER ID");
        Account* sender_account = account_list.get_user(sender_ID);
        if (sender_account != nullptr){
            string receiver_ID = write::input("RECEIVER ID");
            Account* receiver = account_list.get_user(receiver_ID);

            if (receiver != nullptr){
                float amount = stof(write::input("AMOUNT"));
                sender_account->send_money(receiver, amount);
            }
            else
                write::one_panel_string("'" + receiver_ID + "'" + " does not match any user");
        }
        else 
            write::one_panel_string("'" + sender_ID + "'" + " does not match any user");
        
    }
    
}

int main(){
    AccountList account_list;
    write::menu("ADVANCED BANK MANAGER", {"Create Account", "Delete Account", "Send Money", "Show Accounts" ,"Menu", "Quit"});
    
    cout << "\n";

    while (true){
        char choice;

        cout << ">> ";
        choice = cin.get();
        cin.ignore(100, '\n');
        switch (choice)
        {

            case '1':
                cli::create_account(account_list);
                continue;
                
            case '2':
                cli::delete_account(account_list);
                continue;

            case '3':
                cli::send_money(account_list);
                continue;
            
            case '4':
                cli::show_account(account_list);
                continue;
            
            case '5':
                write::menu("ADVANCED BANK MANAGER", {"Create Account", "Delete Account", "Send Money", "Show Accounts" ,"Menu", "Quit"});
                continue;

            case '6':
                break;

            default:
                continue;
        }
        break;
    }
}